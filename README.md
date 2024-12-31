# Quiz Bot Project

## Overview

This project is a Telegram Quiz Bot designed to offer users an engaging learning experience through various topics, passages, and multiple-choice questions. Users can select topics, read passages, answer questions, and track their progress, with the bot evaluating their responses.

## Features

- Interactive quizzes on topics like Nature, Science, History, and Literature.
- Automatic user registration via Telegram IDs.
- Dynamic question generation from a database.
- Real-time scoring and feedback for answers.
- Modular and extensible architecture.

## Technologies Used

- **Python**: Core programming language.
- **SQLAlchemy**: ORM for database operations.
- **MySQL**: Database for storing user data, topics, passages, and questions.
- **Telegram Bot API**: Interface for user interaction.
- **uuid**: For generating unique session IDs.
- **Logging**: For tracking application events and errors.

## Setup Instructions

### Prerequisites

1. Python 3.12.2 or higher.
2. MySQL database.
3. Required Python libraries (install using the following command):
   ```bash
   pip install -r requirements.txt
   ```
4. Telegram Bot Token (obtain from [BotFather](https://core.telegram.org/bots#botfather)).

### Project Structure

```plaintext
.
├── database.py        # Database setup and session management
├── db_init.py         # Script to initialize the database schema
├── models.py          # Database models
├── preload_data.py    # Script to preload data into the database
├── bot.py             # Main bot logic and handlers
├── requirements.txt   # Python dependencies
└── README.md          # Documentation (this file)

```

### Database Configuration

Set up your MySQL database and update the `DATABASE_URI` in `database.py` with your credentials:

```python
DATABASE_URI = "mysql+pymysql://<username>:<password>@<host>:<port>/<database>"
```

### Database Initialization

Run the following command to initialize the database:

```bash
python database.py
```

### Data Preloading

Preload topics, passages, and questions into the database by running:

```bash
python preload_data.py
```

### Running the Bot

Start the bot with:

```bash
python bot.py
```

## How It Works

### User Flow

1. **Start the Bot**:

   - Users type `/start` to begin interacting with the bot.
   - New users are automatically registered.
   - Users choose a topic from a dynamically generated list.

2. **Topic Selection**:

   - After selecting a topic, the bot displays a related passage.
   - Questions associated with the passage are presented sequentially.

3. **Answering Questions**:

   - Users respond by selecting options.
   - The bot evaluates responses and provides instant feedback.

4. **Scoring**:
   - At the end of the quiz, the bot displays the user's total score.

### Data Model

The database includes the following tables:

- **Users**: Stores user information.
- **Sessions**: Tracks user quiz sessions.
- **Topics**: Represents quiz topics.
- **Passages**: Stores passages linked to topics.
- **Questions**: Contains questions and their options.
- **UserInteractions**: Records user responses and scores.

### Telegram Bot Integration

The bot interacts with users via the Telegram Bot API, utilizing the following handlers:

- **CommandHandler**:
  - `/start`: Initializes the quiz and registers the user.
- **CallbackQueryHandler**:
  - Manages topic selection and question responses.



## Troubleshooting

- **Database Connection Issues**:
  - Verify the `DATABASE_URI` and ensure MySQL is running.
- **Bot Token Errors**:
  - Confirm the token's validity and activity.
- **Unhandled Exceptions**:
  - Check the logs for detailed error messages.

