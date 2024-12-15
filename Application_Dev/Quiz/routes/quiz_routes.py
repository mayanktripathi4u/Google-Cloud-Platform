from flask import Blueprint, request, jsonify
from models import db, Quiz, QuizQuestion, Question, UserQuiz
from sqlalchemy.sql.expression import func

quiz_bp = Blueprint('quiz_bp', __name__)

@quiz_bp.route('/generate', methods=['POST'])
def generate_quiz():
    data = request.json
    subject_id = data['subject_id']
    num_of_questions = data['num_of_questions']
    time_limit = data['time_limit']

    questions = Question.query.filter_by(subject_id=subject_id).order_by(func.random()).limit(num_of_questions).all()
    if len(questions) < num_of_questions:
        return jsonify({'message': 'Not enough questions available'}), 400

    new_quiz = Quiz(subject_id=subject_id, num_of_questions=num_of_questions, time_limit=time_limit)
    db.session.add(new_quiz)
    db.session.commit()

    for question in questions:
        quiz_question = QuizQuestion(quiz_id=new_quiz.id, question_id=question.id)
        db.session.add(quiz_question)
    db.session.commit()

    return jsonify({'quiz_id': new_quiz.id, 'message': 'Quiz generated successfully'}), 201

@quiz_bp.route('/submit', methods=['POST'])
def submit_quiz():
    data = request.json
    user_id = data['user_id']
    quiz_id = data['quiz_id']
    answers = data['answers']

    score = 0
    for question_id, user_answer in answers.items():
        question = Question.query.get(question_id)
        if question.correct_answer == user_answer:
            score += 1

    user_quiz = UserQuiz(user_id=user_id, quiz_id=quiz_id, score=score)
    db.session.add(user_quiz)
    db.session.commit()

    return jsonify({'message': 'Quiz submitted successfully', 'score': score}), 200
