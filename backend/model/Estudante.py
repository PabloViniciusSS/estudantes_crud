from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Estudante(db.Model):
    id = db.Column('id',db.Integer, primary_ket=True, autoincrement=True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)