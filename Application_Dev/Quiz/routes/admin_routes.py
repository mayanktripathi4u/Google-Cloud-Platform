from flask import Blueprint, request, jsonify
from models import db, Subject, Question, Option

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/subjects', methods=['POST'])
def add_subject():
    data = request.json
    new_subject = Subject(name=data['name'])
    db.session.add(new_subject)
    db.session.commit()
    return jsonify({'message': 'Subject added successfully'}), 201

@admin_bp.route('/questions', methods=['POST'])
def add_question():
    data = request.json
    new_question = Question(
        subject_id=data['subject_id'],
        question_text=data['question_text'],
        question_type=data['question_type'],
        correct_answer=data['correct_answer']
    )
    db.session.add(new_question)
    db.session.commit()
    if data['question_type'] in ['MCQ', 'Multi-Select']:
        for option in data['options']:
            new_option = Option(question_id=new_question.id, option_text=option)
            db.session.add(new_option)
        db.session.commit()
    return jsonify({'message': 'Question added successfully'}), 201


# @app.route('/admin/subjects', methods=['POST'])
# def add_subject():
#     data = request.json
#     new_subject = Subject(name=data['name'])
#     db.session.add(new_subject)
#     db.session.commit()
#     return jsonify({'message': 'Subject added successfully'}), 201

# @app.route('/admin/questions', methods=['POST'])
# def add_question():
#     data = request.json
#     new_question = Question(
#         subject_id=data['subject_id'],
#         question_text=data['question_text'],
#         question_type=data['question_type'],
#         correct_answer=data['correct_answer']
#     )
#     db.session.add(new_question)
#     db.session.commit()
#     # Add options if the question type is MCQ or Multi-Select
#     if data['question_type'] in ['MCQ', 'Multi-Select']:
#         for option in data['options']:
#             new_option = Option(question_id=new_question.id, option_text=option)
#             db.session.add(new_option)
#         db.session.commit()
#     return jsonify({'message': 'Question added successfully'}), 201



