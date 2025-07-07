#!/bin/bash

# Переходим в папку frontend
cd frontend

# Устанавливаем зависимости
npm install

# Собираем frontend
npm run build

# Возвращаемся в корень
cd ..

echo "Frontend build completed!"