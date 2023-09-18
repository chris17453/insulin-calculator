import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DB_DIR = os.path.join(os.path.dirname(BASE_DIR), "db")
    SECRET_KEY = 'momwehadababyitsaboy'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DB_DIR, 'insulin-calculator.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False