from flask import Blueprint, jsonify
from models import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/<int:user_id>/dashboard', methods=['GET'])
def user_dashboard(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    quizzes = [{'quiz_id': q.quiz_id, 'score': q.score, 'taken_at': q.taken_at} for q in user.quizzes_taken]
    return jsonify({'username': user.username, 'quizzes_taken': quizzes}), 200


# @app.route('/quiz/generate', methods=['POST'])
# def generate_quiz():
#     data = request.json
#     subject_id = data['subject_id']
#     num_of_questions = data['num_of_questions']
#     time_limit = data['time_limit']
    
#     # Fetch random questions from the selected subject
#     questions = Question.query.filter_by(subject_id=subject_id).order_by(func.random()).limit(num_of_questions).all()
#     if len(questions) < num_of_questions:
#         return jsonify({'message': 'Not enough questions available'}), 400

#     new_quiz = Quiz(subject_id=subject_id, num_of_questions=num_of_questions, time_limit=time_limit)
#     db.session.add(new_quiz)
#     db.session.commit()

#     # Link questions to the quiz
#     for question in questions:
#         quiz_question = QuizQuestion(quiz_id=new_quiz.id, question_id=question.id)
#         db.session.add(quiz_question)
#     db.session.commit()

#     return jsonify({'quiz_id': new_quiz.id, 'message': 'Quiz generated successfully'}), 201


# @app.route('/quiz/submit', methods=['POST'])
# def submit_quiz():
#     data = request.json
#     user_id = data['user_id']
#     quiz_id = data['quiz_id']
#     answers = data['answers']  # Dict {question_id: user_answer}

#     # Calculate the score
#     score = 0
#     for question_id, user_answer in answers.items():
#         question = Question.query.get(question_id)
#         if question.correct_answer == user_answer:
#             score += 1

#     # Save User Quiz Result
#     user_quiz = UserQuiz(user_id=user_id, quiz_id=quiz_id, score=score)
#     db.session.add(user_quiz)
#     db.session.commit()

#     return jsonify({'message': 'Quiz submitted successfully', 'score': score}), 200


# @app.route('/user/<int:user_id>/dashboard', methods=['GET'])
# def user_dashboard(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({'message': 'User not found'}), 404

#     quizzes = [{'quiz_id': q.quiz_id, 'score': q.score, 'taken_at': q.taken_at} for q in user.quizzes_taken]
#     return jsonify({'username': user.username, 'quizzes_taken': quizzes}), 200
