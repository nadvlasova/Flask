
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'

    # Прописать настройки для яндекса или mail.
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    # Именно от этого отправителя пользователь будет получать письма
    # о восстановлении пароля.
    MAIL_USERNAME = "nadezhda.study@yandex.ru"
    MAIL_PASSWORD = "Study_mail123"
