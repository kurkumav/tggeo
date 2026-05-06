# 🚀 Деплой на Render.com (бесплатно)

## Шаг 1: Подготовка

### 1.1 Создайте GitHub репозиторий
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/ваш-username/tggeo.git
git push -u origin main
```

### 1.2 Разместите WebApp на GitHub Pages
1. Перейдите в Settings → Pages
2. Source: Deploy from a branch → main → / (root) → Save
3. Подождите 2-3 минуты
4. Скопируйте URL: `https://ваш-username.github.io/tggeo`

## Шаг 2: Деплой бота на Render

### 2.1 Создайте аккаунт
1. Перейдите на [render.com](https://render.com)
2. Зарегистрируйтесь через GitHub (быстрее)

### 2.2 Создайте новый Web Service
1. Нажмите **New +** → **Web Service**
2. Подключите ваш GitHub репозиторий `tggeo`
3. Настройте:
   - **Name**: `tggeo-bot` (или любое имя)
   - **Region**: Frankfurt (ближе к России)
   - **Branch**: `main`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
   - **Instance Type**: Free

### 2.3 Добавьте переменные окружения
В разделе **Environment Variables** добавьте:

| Key | Value |
|-----|-------|
| `TELEGRAM_BOT_TOKEN` | Ваш токен от @BotFather |
| `WEBAPP_URL` | `https://ваш-username.github.io/tggeo` |
| `MAPILLARY_TOKEN` | Ваш токен от Mapillary |

### 2.4 Деплой
1. Нажмите **Create Web Service**
2. Подождите 2-3 минуты (первый деплой)
3. Проверьте логи: должно быть "Бот запущен..."

## Шаг 3: Проверка

1. Откройте бота в Telegram
2. Отправьте `/start`
3. Нажмите "🎮 Играть"
4. Если WebApp открылся — всё работает!

## 🔥 Лайфхак: Бот без засыпания

Бесплатный tier Render засыпает после 15 минут неактивности. Чтобы бот работал 24/7:

### Вариант 1: Cron-Job.org (рекомендуется)
1. Зарегистрируйтесь на [cron-job.org](https://cron-job.org)
2. Создайте новый cronjob:
   - **URL**: `https://ваш-сервис.onrender.com` (URL вашего Render сервиса)
   - **Interval**: Every 10 minutes
   - **Title**: Keep TGGeo Bot Alive
3. Сохраните

### Вариант 2: UptimeRobot
1. Зарегистрируйтесь на [uptimerobot.com](https://uptimerobot.com)
2. Add New Monitor:
   - **Monitor Type**: HTTP(s)
   - **URL**: `https://ваш-сервис.onrender.com`
   - **Monitoring Interval**: 5 minutes
3. Сохраните

### Вариант 3: Healthcheck endpoint (продвинутый)
Добавьте в `bot.py` простой HTTP сервер для пингов (опционально).

## 📊 Мониторинг

### Логи на Render
1. Откройте ваш сервис на Render
2. Перейдите в **Logs**
3. Смотрите в реальном времени

### Проверка работы
```bash
# Проверьте что бот отвечает
curl https://api.telegram.org/bot<ваш_токен>/getMe
```

## 🔄 Обновление

После изменений в коде:
```bash
git add .
git commit -m "Описание изменений"
git push
```

Render автоматически задеплоит новую версию!

## ⚠️ Важные моменты

### Лимиты бесплатного tier
- ✅ 750 часов в месяц (достаточно для 1 сервиса 24/7)
- ✅ Засыпает после 15 мин неактивности (решается cron-job)
- ✅ Просыпается за ~30 секунд при первом запросе
- ✅ 100 GB bandwidth в месяц (более чем достаточно)

### Безопасность
- ❌ Никогда не коммитьте `.env` файл
- ✅ Все секреты только в Environment Variables на Render
- ✅ `.env` уже в `.gitignore`

### Если что-то не работает
1. Проверьте логи на Render
2. Убедитесь что все 3 переменные окружения добавлены
3. Проверьте что GitHub Pages активирован
4. Подождите 2-3 минуты после первого деплоя

## 🎉 Готово!

Теперь ваш бот работает 24/7 бесплатно!

### Полезные ссылки
- Render Dashboard: https://dashboard.render.com
- GitHub Pages: https://ваш-username.github.io/tggeo
- Логи бота: https://dashboard.render.com/web/ваш-сервис/logs
- Telegram бот: https://t.me/ваш_бот

## 💡 Альтернативы Render

Если Render не подходит:
- **Railway.app** - $5 кредитов в месяц бесплатно
- **Fly.io** - 3 бесплатных VM
- **Heroku** - больше не бесплатный
- **VPS** - $4-6/месяц (DigitalOcean, Hetzner)

---

Нужна помощь? Создайте issue в репозитории!
