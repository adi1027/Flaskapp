
class Config:
SECRET_KEY'] = '0943eb52672340e1162dc8cce842f6'
 SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
  MAIL_SERVER"] = 'smtp.gmail.com'
   MAIL_PORT"] = 465
   MAIL_USE_SSL"] = False
    app.config["MAIL_USE_TLS "] = False

    app.config["MAIL_USERNAME"] = os.environ.get('EMAIL_USER')
    app.config["MAIL_PASSWORD"] = os.environ.get('EMAIL_PASS')
