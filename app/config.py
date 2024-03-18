import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')

    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')    
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'sandbox.smtp.mailtrap.io') 
    MAIL_PORT = os.environ.get('MAIL_PORT', '25') 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'f0626403b8b10e') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'd488b4cb5e807a')
