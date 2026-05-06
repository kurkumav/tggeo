import asyncio
import json
import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from geopy.distance import geodesic
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Конфигурация
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в переменных окружения")
if not WEBAPP_URL:
    raise ValueError("WEBAPP_URL не найден в переменных окружения")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    """Обработчик команды /start"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 Играть",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )

    await message.answer(
        "🌍 Мини GeoGuessr\n\n"
        "Угадай место по фотографии!\n"
        "Нажми 'Играть' чтобы начать.",
        reply_markup=keyboard
    )
    logger.info(f"Пользователь {message.from_user.id} запустил бота")


@dp.message(F.web_app_data)
async def handle_webapp_data(message: Message):
    """Обработчик данных из WebApp"""
    try:
        logger.info(f"Получены данные от пользователя {message.from_user.id}")

        data = json.loads(message.web_app_data.data)

        # Валидация данных
        required_fields = ["guess_lat", "guess_lon", "real_lat", "real_lon"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Отсутствует поле: {field}")

        guess_lat = float(data["guess_lat"])
        guess_lon = float(data["guess_lon"])
        real_lat = float(data["real_lat"])
        real_lon = float(data["real_lon"])

        # Вычисление расстояния
        guess = (guess_lat, guess_lon)
        real = (real_lat, real_lon)
        distance = geodesic(guess, real).km

        # Расчет очков (максимум 5000, минимум 0)
        score = max(0, int(5000 - distance))

        # Определение точности
        if distance < 1:
            accuracy = "🎯 Невероятно точно!"
        elif distance < 10:
            accuracy = "🎖️ Отлично!"
        elif distance < 100:
            accuracy = "👍 Хорошо!"
        elif distance < 500:
            accuracy = "👌 Неплохо!"
        else:
            accuracy = "🤔 Попробуй еще раз!"

        await message.answer(
            f"{accuracy}\n\n"
            f"📏 Расстояние: {distance:.2f} км\n"
            f"🏆 Очки: {score}\n\n"
            f"Сыграй еще раз! /start"
        )

        logger.info(
            f"Пользователь {message.from_user.id}: "
            f"расстояние={distance:.2f}км, очки={score}"
        )

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON: {e}")
        await message.answer(
            "⚠️ Ошибка обработки данных.\n"
            "Попробуй еще раз: /start"
        )
    except ValueError as e:
        logger.error(f"Ошибка валидации данных: {e}")
        await message.answer(
            "⚠️ Некорректные данные.\n"
            "Попробуй еще раз: /start"
        )
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}", exc_info=True)
        await message.answer(
            "⚠️ Произошла ошибка.\n"
            "Попробуй еще раз: /start"
        )


@dp.message()
async def handle_unknown(message: Message):
    """Обработчик неизвестных команд"""
    await message.answer(
        "Используй /start чтобы начать игру!"
    )


async def health_check(request):
    """Health check endpoint для Render"""
    return web.Response(text="OK")


async def main():
    """Запуск бота и веб-сервера"""
    logger.info("Бот запущен...")

    # Запуск веб-сервера для health check
    app = web.Application()
    app.router.add_get('/', health_check)
    app.router.add_get('/health', health_check)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.getenv('PORT', 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logger.info(f"Health check сервер запущен на порту {port}")

    # Запуск бота
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}", exc_info=True)
    finally:
        await bot.session.close()
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
