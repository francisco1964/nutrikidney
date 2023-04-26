import os

basedir = os.path.abspath(os.path.dirname(__file__))

#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}
#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
class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'data/nutri.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
