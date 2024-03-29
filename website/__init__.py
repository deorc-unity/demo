from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'relatedToHbbb1234oPppWea' #Encrypt or secure cookies or session data
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #app.config['SQLALCHEMY_DATABASE_URI'] = "sgreign.mysql.pythonanywhere-services.com"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://erqkdvcbnqzxvv:3f7c4f143994897241b97f42cf2e7a75886af3ae0c1893b4401b902e92a8a554@ec2-52-54-200-216.compute-1.amazonaws.com:5432/d48n7q6ppofipj'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Linking

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
    
