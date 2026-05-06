# 🌍 TGGeo - Telegram GeoGuessr Mini App

Мини-игра в стиле GeoGuessr для Telegram. Угадывайте местоположение по фотографиям из Mapillary!

![Demo](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Особенности

- 🎮 **Интерактивная игра** - угадывайте место по фото
- 🗺️ **Карта мира** - выбирайте точку на карте
- 🎯 **Система очков** - до 5000 очков за точность
- 📊 **Результаты в игре** - расстояние, очки, обе точки на карте
- 🔄 **Играть еще раз** - без перезапуска бота
- 🎨 **Дизайн Telegram** - нативный вид
- 🌐 **8 городов** - Москва, Париж, Нью-Йорк, Токио и другие

## 🚀 Быстрый старт

### Требования

- Python 3.8+
- Telegram Bot Token
- Mapillary API Token
- GitHub аккаунт (для хостинга WebApp)

### 1. Получите токены

#### Telegram Bot Token
1. Откройте [@BotFather](https://t.me/botfather) в Telegram
2. Отправьте `/newbot`
3. Следуйте инструкциям
4. Скопируйте токен

#### Mapillary API Token
1. Зарегистрируйтесь на [mapillary.com](https://www.mapillary.com/)
2. Перейдите в [Developer Settings](https://www.mapillary.com/dashboard/developers)
3. Создайте новое приложение
4. Скопируйте Client Token

### 2. Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/yourusername/tggeo.git
cd tggeo

# Установите зависимости
pip install -r requirements.txt

# Создайте .env файл
cp .env.example .env
```

### 3. Настройка

Отредактируйте `.env`:
```env
TELEGRAM_BOT_TOKEN=ваш_токен_от_botfather
MAPILLARY_TOKEN=ваш_токен_от_mapillary
WEBAPP_URL=https://ваш-username.github.io/tggeo
```

Отредактируйте `index.html` (строка 128):
```javascript
const MAPILLARY_TOKEN = "ваш_токен_от_mapillary";
```

### 4. Разместите WebApp на GitHub Pages

1. Создайте репозиторий на GitHub
2. Загрузите `index.html`
3. Включите GitHub Pages:
   - Settings → Pages → Source: main branch → Save
4. Скопируйте URL в `.env`

### 5. Запустите бота

```bash
python bot.py
```

## 📁 Структура проекта

```
tggeo/
├── bot.py                    # Telegram бот (aiogram)
├── index.html                # WebApp интерфейс (статический)
├── requirements.txt          # Python зависимости
├── Procfile                  # Команда запуска для Render
├── runtime.txt               # Версия Python для Render
├── render.yaml               # Конфигурация Render
├── .env.example              # Пример конфигурации
├── .gitignore                # Git ignore
├── README.md                 # Документация
├── DEPLOY.md                 # Инструкция по деплою
├── FAQ.md                    # Частые вопросы
├── CHECKLIST.md              # Чеклист запуска
└── CLAUDE.md                 # Техническая документация
```

## 🎮 Как играть

1. Найдите бота в Telegram
2. Отправьте `/start`
3. Нажмите "🎮 Играть"
4. Посмотрите на фото
5. Выберите место на карте
6. Нажмите "🎯 Угадать"
7. Увидите результат с очками!
8. Нажмите "🎮 Играть еще раз"

## 📊 Система очков

- **Формула:** `max(0, 5000 - расстояние_в_км)`
- **Максимум:** 5000 очков (точное попадание)
- **Минимум:** 0 очков

**Оценки:**
- < 1 км: 🎯 Невероятно точно!
- < 10 км: 🎖️ Отлично!
- < 100 км: 👍 Хорошо!
- < 500 км: 👌 Неплохо!
- \> 500 км: 🤔 Попробуй еще раз!

## 🗺️ Города в игре

- 🇷🇺 Москва
- 🇷🇺 Санкт-Петербург
- 🇫🇷 Париж
- 🇬🇧 Лондон
- 🇺🇸 Нью-Йорк
- 🇺🇸 Лос-Анджелес
- 🇯🇵 Токио
- 🇸🇬 Сингапур

## 🚀 Деплой (бесплатно!)

### Render.com (рекомендуется)

**Полная инструкция:** см. [DEPLOY.md](DEPLOY.md)

**Быстрый старт:**
1. Загрузите код на GitHub
2. Зарегистрируйтесь на [render.com](https://render.com)
3. Создайте Web Service из вашего репозитория
4. Добавьте переменные окружения (токены)
5. Деплой! 🎉

**Лайфхак:** Используйте [cron-job.org](https://cron-job.org) для пинга каждые 10 минут — бот не будет засыпать.

### Альтернативы
- **Railway.app** - $5 кредитов/месяц
- **Fly.io** - 3 бесплатных VM
- **VPS** - $4-6/месяц (полный контроль)

## 🔧 Настройка для production

### Systemd (Linux)

```bash
sudo nano /etc/systemd/system/tggeo-bot.service
```

```ini
[Unit]
Description=TGGeo Telegram Bot
After=network.target

[Service]
Type=simple
User=yourusername
WorkingDirectory=/path/to/tggeo
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/python bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable tggeo-bot
sudo systemctl start tggeo-bot
```

### Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py .
COPY .env .

CMD ["python", "bot.py"]
```

```bash
docker build -t tggeo-bot .
docker run -d --name tggeo-bot --restart unless-stopped tggeo-bot
```

## 🐛 Решение проблем

### Бот не отвечает
- Проверьте `TELEGRAM_BOT_TOKEN` в `.env`
- Убедитесь что `bot.py` запущен

### WebApp не открывается
- Проверьте `WEBAPP_URL` в `.env`
- Убедитесь что GitHub Pages активирован
- Подождите 2-3 минуты после включения Pages

### Фото не загружается
- Проверьте `MAPILLARY_TOKEN` в `index.html`
- Убедитесь что токен активен
- Попробуйте закрыть и открыть WebApp снова

## 🚀 Возможные улучшения

- [ ] База данных для статистики
- [ ] Глобальный лидерборд
- [ ] Больше городов (50+)
- [ ] Режимы сложности
- [ ] Таймер на угадывание
- [ ] Мультиплеер режим
- [ ] Подсказки (континент, климат)
- [ ] Достижения и награды
- [ ] Своя БД с панорамами (быстрее в 3-5 раз)

## 📄 Лицензия

MIT License - используйте свободно!

## 🤝 Вклад

Pull requests приветствуются! Для больших изменений сначала откройте issue.

## 📧 Поддержка

Если возникли вопросы - создайте issue в репозитории.

## 🙏 Благодарности

- [Mapillary](https://www.mapillary.com/) - за API с панорамами
- [Leaflet.js](https://leafletjs.com/) - за библиотеку карт
- [aiogram](https://aiogram.dev/) - за Telegram Bot framework

---

Сделано с ❤️ для Telegram
