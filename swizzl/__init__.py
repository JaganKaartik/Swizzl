from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from swizzl.services import newsfetch as snf


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdatabase.db'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
admin = Admin(app)


from swizzl.models import User, ViewPosts
from swizzl import routes
from swizzl.routes import MyModelView

admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(ViewPosts, db.session))