# Быстрый старт

## 1. Создайте .env файл
```bash
cp .env.example .env
```

Заполните токены в `.env`:
- `TELEGRAM_BOT_TOKEN` - получите у @BotFather
- `MAPILLARY_TOKEN` - получите на mapillary.com/developer
- `WEBAPP_URL` - пока оставьте пустым

## 2. Разместите index.html на GitHub Pages

### Вариант A: Через веб-интерфейс GitHub
1. Создайте новый репозиторий на github.com
2. Загрузите файл `index.html`
3. Settings → Pages → Source: main branch → Save
4. Скопируйте URL (например: `https://username.github.io/tggeo`)
5. Вставьте URL в `.env` как `WEBAPP_URL`

### Вариант B: Через командную строку
```bash
# Инициализируйте Git (если еще не сделано)
git init
git add index.html
git commit -m "Add WebApp"

# Создайте репозиторий на GitHub и подключите
git remote add origin https://github.com/username/tggeo.git
git push -u origin main

# Включите GitHub Pages в настройках репозитория
```

## 3. Установите зависимости и запустите бота
```bash
pip install -r requirements.txt
python bot.py
```

## 4. Протестируйте
1. Найдите вашего бота в Telegram
2. Отправьте `/start`
3. Нажмите "🎮 Играть"
4. Играйте!

---

## Альтернатива: Быстрый тест с ngrok (для разработки)

Если хотите быстро протестировать без GitHub Pages:

```bash
# Терминал 1: запустите простой HTTP сервер
python -m http.server 8000

# Терминал 2: запустите ngrok
ngrok http 8000

# Скопируйте ngrok URL в .env как WEBAPP_URL
# Например: WEBAPP_URL=https://abc123.ngrok-free.app

# Терминал 3: запустите бота
python bot.py
```

**Важно:** ngrok URL меняется при каждом перезапуске. Для production используйте GitHub Pages!
