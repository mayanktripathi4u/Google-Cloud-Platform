from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from routes.admin_routes import admin_bp
    from routes.user_routes import user_bp
    from routes.quiz_routes import quiz_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(quiz_bp, url_prefix='/quiz')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
