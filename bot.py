from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from models import Passage, Question, Session, Topic, User, UserInteraction
from database import db_session
import uuid
from datetime import datetime
import logging
from dotenv import load_dotenv
import os


load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Please set the TELEGRAM_BOT_TOKEN environment variable.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    try:
        telegram_id = update.effective_user.id
        username = update.effective_user.username or "anonymous_user"

        
        user = db_session.query(User).filter_by(id=telegram_id).first()
        if not user:
           
            user = User(id=telegram_id, username=username)
            db_session.add(user)
            db_session.commit()
            await update.message.reply_text("Welcome! You are now registered.")
        else:
            await update.message.reply_text("Welcome back! Please choose a topic.")

      
        session_id = str(uuid.uuid4())
        new_session = Session(user_id=user.id, session_id=session_id)
        context.user_data['session_id'] = session_id
        db_session.add(new_session)
        db_session.commit()

       
        keyboard = [
            [InlineKeyboardButton(topic.name, callback_data=f"topic_{topic.id}")]
            for topic in db_session.query(Topic).all()
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Choose a topic:", reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error in /start command: {e}")
        await update.message.reply_text("Sorry, something went wrong. Please try again.")


async def handle_topic_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
    try:
        query = update.callback_query
        await query.answer()

        data = query.data
        if data.startswith("topic_"):
            topic_id = int(data.split("_")[1])
            context.user_data["topic_id"] = topic_id
            context.user_data["current_question"] = 0
            context.user_data["score"] = 0

         
            passage = db_session.query(Passage).filter_by(topic_id=topic_id).first()
            if passage:
                context.user_data["passage_id"] = passage.id
                await query.message.reply_text(passage.text)
                await send_question(update, context)
            else:
                await query.message.reply_text("No passages available for this topic.")
    except Exception as e:
        logger.error(f"Error while handling topic selection: {e}")
        await query.message.reply_text("An error occurred. Please try again.")


async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
    try:
        question_index = context.user_data["current_question"]
        passage_id = context.user_data["passage_id"]
        questions = db_session.query(Question).filter_by(passage_id=passage_id).all()

        if question_index < len(questions):
            question = questions[question_index]
            context.user_data["current_question_id"] = question.id

          
            keyboard = [
                [InlineKeyboardButton(option, callback_data=f"answer_{option}")]
                for option in question.options.split(",")
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.user_data["correct_option"] = question.correct_option

            
            await update.callback_query.message.reply_text(
                f"Question {question_index + 1}: {question.question}",
                reply_markup=reply_markup
            )
        else:
            await show_score(update, context)
    except Exception as e:
        logger.error(f"Error while sending question: {e}")
        await update.callback_query.message.reply_text("An error occurred. Please try again.")


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    try:
        query = update.callback_query
        await query.answer()

        data = query.data
        selected_option = data.split("_")[1]
        correct_option = context.user_data["correct_option"]
        question_id = context.user_data["current_question_id"]
        session_id = context.user_data["session_id"]


        is_correct = int(selected_option == correct_option)
        user_interaction = UserInteraction(
            session_id=db_session.query(Session).filter_by(session_id=session_id).first().id,
            question_id=question_id,
            user_answer=selected_option,
            is_correct=is_correct,
            score=1.0 if is_correct else 0.0,
            timestamp=datetime.now()
        )
        db_session.add(user_interaction)
        db_session.commit()


        if is_correct:
            context.user_data["score"] += 1
            await query.message.reply_text("Great job! That’s correct!")
        else:
            await query.message.reply_text(f"Incorrect. The correct answer was {correct_option}.")

        context.user_data["current_question"] += 1
        await send_question(update, context)
    except Exception as e:
        logger.error(f"Error while processing answer: {e}")
        await query.message.reply_text("An error occurred. Please try again.")


async def show_score(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        session_id = context.user_data["session_id"]
        session = db_session.query(Session).filter_by(session_id=session_id).first()

        if not session:
            await update.callback_query.message.reply_text("Error: Session not found.")
            return

        interactions = db_session.query(UserInteraction).filter_by(session_id=session.id).all()
        total_score = sum(interaction.score for interaction in interactions)
        total_questions = len(interactions)

        await update.callback_query.message.reply_text(
            f"Your score: {int(total_score)}/{total_questions}. Type /start to try another topic."
        )
    except Exception as e:
        logger.error(f"Error while displaying score: {e}")
        await update.callback_query.message.reply_text("An error occurred. Please try again.")


def main():
   
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(handle_topic_selection, pattern="^topic_"))
        application.add_handler(CallbackQueryHandler(handle_answer, pattern="^answer_"))
        application.run_polling()
    except Exception as e:
        logger.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
