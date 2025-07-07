# 🚀 Развертывание на Vercel - Исправленная конфигурация

## ✅ Что уже настроено:

1. **vercel.json** - Конфигурация для Vercel
2. **api/index.py** - Точка входа для serverless функций
3. **requirements.txt** - Зависимости Python для Supabase
4. **frontend/.env** - URL обновлен для Vercel
5. **backend/.env** - Восстановлена конфигурация Supabase

## 🔧 Что делать дальше:

### В интерфейсе Vercel:

1. **Зайдите в настройки проекта** на vercel.com
2. **Environment Variables** → добавьте переменные:
   ```
   SUPABASE_URL=https://kykzqxoxgcwqurnceslu.supabase.co
   SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt5a3pxeG94Z2N3cXVybmNlc2x1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTQ4NzI0OCwiZXhwIjoyMDY3MDYzMjQ4fQ.wZcC233qDjrIuXn4it1j-YnxHak14v8GqxCCuW6VIb4
   SECRET_KEY=uroki-islama-secret-key-2024
   DATABASE_URL=postgresql://postgres:jsjsjdhsivdusbdis267263733673@db.kykzqxoxgcwqurnceslu.supabase.co:5432/postgres
   USE_POSTGRES=true
   ```

3. **Redeploy** → нажмите "Redeploy" для повторного развертывания

### Если используете Git:

1. Сделайте commit и push изменений:
   ```bash
   git add .
   git commit -m "Fix Vercel configuration for Supabase"
   git push origin main
   ```

2. Vercel автоматически сделает redeploy

## 🔍 Проверка после развертывания:

1. **API тест**: `https://chasa.vercel.app/api/`
2. **Админ вход**: `https://chasa.vercel.app/` → войти как admin@uroki-islama.ru / admin123
3. **Курсы**: `https://chasa.vercel.app/api/courses`

## 🚨 Возможные проблемы и решения:

### Если все еще 404:
- Проверьте, что в Vercel правильно настроены Environment Variables
- Убедитесь, что Build Command пустой (оставьте по умолчанию)
- Root Directory должен быть пустым

### Если ошибка импорта:
- Все нужные файлы скопированы в папку `/api`
- Vercel будет использовать их для serverless функций

## 📂 Структура для Vercel:

```
/
├── api/
│   ├── index.py          # Точка входа для Vercel
│   ├── server.py         # Основной FastAPI сервер
│   ├── models.py         # Модели данных
│   └── *_client.py       # Клиенты баз данных
├── frontend/
│   ├── src/             # React приложение
│   └── package.json     # Зависимости фронтенда
├── vercel.json          # Конфигурация Vercel
└── requirements.txt     # Зависимости Python
```

Теперь все должно работать правильно! 🎉