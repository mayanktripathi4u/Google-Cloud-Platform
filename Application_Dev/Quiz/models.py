from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    quizzes_taken = db.relationship('UserQuiz', back_populates='user')

class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    questions = db.relationship('Question', back_populates='subject')

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(20), nullable=False)
    options = db.relationship('Option', back_populates='question')
    correct_answer = db.Column(db.Text, nullable=False)
    subject = db.relationship('Subject', back_populates='questions')

class Option(db.Model):
    __tablename__ = 'options'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    option_text = db.Column(db.String(200), nullable=False)
    question = db.relationship('Question', back_populates='options')

class Quiz(db.Model):
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    num_of_questions = db.Column(db.Integer, nullable=False)
    time_limit = db.Column(db.Integer, nullable=False)
    questions = db.relationship('QuizQuestion', back_populates='quiz')
    subject = db.relationship('Subject')

class QuizQuestion(db.Model):
    __tablename__ = 'quiz_questions'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    quiz = db.relationship('Quiz', back_populates='questions')
    question = db.relationship('Question')

class UserQuiz(db.Model):
    __tablename__ = 'user_quizzes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    score = db.Column(db.Float)
    taken_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', back_populates='quizzes_taken')
    quiz = db.relationship('Quiz')


# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# db = SQLAlchemy()

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False, unique=True)
#     email = db.Column(db.String(120), nullable=False, unique=True)
#     password = db.Column(db.String(120), nullable=False)
#     quizzes_taken = db.relationship('UserQuiz', back_populates='user')

# class Subject(db.Model):
#     __tablename__ = 'subjects'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False, unique=True)
#     questions = db.relationship('Question', back_populates='subject')

# class Question(db.Model):
#     __tablename__ = 'questions'
#     id = db.Column(db.Integer, primary_key=True)
#     subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
#     question_text = db.Column(db.Text, nullable=False)
#     question_type = db.Column(db.String(20), nullable=False)  # MCQ, Fill in the blanks, Multi-Select
#     options = db.relationship('Option', back_populates='question')
#     correct_answer = db.Column(db.Text, nullable=False)
#     subject = db.relationship('Subject', back_populates='questions')

# class Option(db.Model):
#     __tablename__ = 'options'
#     id = db.Column(db.Integer, primary_key=True)
#     question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
#     option_text = db.Column(db.String(200), nullable=False)
#     question = db.relationship('Question', back_populates='options')

# class Quiz(db.Model):
#     __tablename__ = 'quizzes'
#     id = db.Column(db.Integer, primary_key=True)
#     subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
#     num_of_questions = db.Column(db.Integer, nullable=False)
#     time_limit = db.Column(db.Integer, nullable=False)  # In minutes
#     questions = db.relationship('QuizQuestion', back_populates='quiz')
#     subject = db.relationship('Subject')

# class QuizQuestion(db.Model):
#     __tablename__ = 'quiz_questions'
#     id = db.Column(db.Integer, primary_key=True)
#     quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
#     question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
#     quiz = db.relationship('Quiz', back_populates='questions')
#     question = db.relationship('Question')

# class UserQuiz(db.Model):
#     __tablename__ = 'user_quizzes'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
#     score = db.Column(db.Float)
#     taken_at = db.Column(db.DateTime, default=datetime.utcnow)
#     user = db.relationship('User', back_populates='quizzes_taken')
#     quiz = db.relationship('Quiz')
