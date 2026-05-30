from flask import Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_bcrypt import Bcrypt # type: ignore
from flask_login import LoginManager # type: ignore
from flask_mail import Mail # type: ignore
from config import Config # type: ignore

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)

from flask_auth import routes
if __name__ == '__main__':
    app.run(debug=True)
from flask_auth import db
db.create_all()

