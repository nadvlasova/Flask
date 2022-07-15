from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from flask_blog_green.config import Config
from flask_mail import Mail


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from flask_blog_green.main.routes import main
    from flask_blog_green.users.routes import users
    from flask_blog_green.posts.routes import posts
    from flask_blog_green.errors.handers import errors

    from flask_blog_green.main import routes
    from flask_blog_green import models

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    return app
