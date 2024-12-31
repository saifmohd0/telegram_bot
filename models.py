from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, DateTime, BigInteger
from sqlalchemy.orm import relationship
from database import Base

from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String(50), nullable=False)

    sessions = relationship("Session", back_populates="user")
    interactions = relationship("UserInteraction", secondary="sessions", 
                                 primaryjoin="User.id == Session.user_id",
                                 secondaryjoin="Session.id == UserInteraction.session_id",
                                 viewonly=True)

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)  # Match BigInteger
    session_id = Column(String(100), unique=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="sessions")
    interactions = relationship("UserInteraction", back_populates="session")

class UserInteraction(Base):
    __tablename__ = 'user_interactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey('sessions.id'), nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    user_answer = Column(String(255), nullable=False)
    is_correct = Column(Integer, nullable=False)
    score = Column(Float, nullable=False, default=0.0)
    timestamp = Column(DateTime, default=datetime.utcnow)

    session = relationship("Session", back_populates="interactions")
    question = relationship("Question")


class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500), nullable=False)

class Passage(Base):
    __tablename__ = 'passages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    topic_id = Column(Integer, ForeignKey('topics.id'), nullable=False)
    text = Column(Text, nullable=False)
    topic = relationship("Topic", back_populates="passages")

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    passage_id = Column(Integer, ForeignKey('passages.id'), nullable=False)
    question = Column(Text, nullable=False)
    options = Column(String(255), nullable=False)  # Comma-separated options
    correct_option = Column(String(255), nullable=False)
    passage = relationship("Passage", back_populates="questions")

Topic.passages = relationship("Passage", back_populates="topic")
Passage.questions = relationship("Question", back_populates="passage")
