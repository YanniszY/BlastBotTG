# BlastBot

**BlastBot** — это Telegram-бот, предназначенный для рассылки сообщений по всем группам, в которых он состоит. Бот позволяет назначенному пользователю легко составлять и отправлять сообщения, включая фотографии (по желанию), во множество чатов одновременно.

![logo](img/logo.jpg)

# Важно!
  - **Бот не будет работать если его нет в группе или у него нет прав на отправление сообщений!**

## Функции

- **Контролируемый доступ**: Только определенный пользователь, чей Telegram ID прописан в коде бота, может управлять ботом для начала рассылки сообщений.
- **Интерактивное создание сообщений**: Пользователь может составить сообщение через удобный пошаговый процесс:
  - Запустить бота с помощью команды `/start`.
  - Использовать инлайн-кнопку для начала создания сообщения.
  - Выбрать фотографию для сообщения (опционально) или пропустить этот шаг.
  - Написать текст сообщения.
  - Просмотреть составленное сообщение, нажав на кнопку "Просмотр сообщения".
  - Начать рассылку сообщения по всем группам, нажав на кнопку "Начать рассылку".

## Начало работы

### Необходимые условия

- Python 3.10+
- Токен Telegram Bot API

### Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/YanniszY/BlastBotTG.git
   cd BlastBotTG
   ```

2. Установите необходимые пакеты Python:

      ```
      pip install -r requirements.txt
      ```
      
3. измените YOUR TOKEN BOT в файле .env на свой токен бота
   ```
   BOT_TOKEN='YOUR BOT TOKEN' # paste your bot token
   ```

4. Измените переменную admin_id в файле handlers/handlers.py
   ```
   admin_id = 0 # telegram admin id
   ```

5. Добавтье группы в файл chat_list.py
    ```
    channel_ids = ["@group1", "@group2", "@group3", "@YourGroupUsername"]
    # Вставтье username группы в лист
    # Если есть только ссылка:
    # Замените https://t.me/ на @
    # Пример: @YourGroupUsername
    ```
  
# Запустите бота:
      
      python bot.py
      
# Использование

  1. **Запуск бота:** Авторизованный пользователь отправляет команду /start в личном чате с ботом.
  2. **Создание сообщения:**
     - Выберите фотографию (по желанию) или пропустите этот шаг.
     - Напишите текст сообщения.
  4. **Просмотр сообщения:** Просмотрите составленное сообщение перед рассылкой.
  5. **Рассылка:** Нажмите кнопку "Начать рассылку", чтобы отправить сообщение во все группы, где состоит бот.
