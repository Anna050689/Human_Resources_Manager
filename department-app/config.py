class Configuration(object):
    """This class sets configuration settings."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:BeHappy01112017@localhost/human_resources_department'
    SQLALCHEMY_TRACK_MODIFICATIONS = False