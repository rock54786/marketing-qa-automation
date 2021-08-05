
# Prod config file
class Env:
    """
    Env
    """
    URL = "https://admin.aftership.com/"


class Account:
    """
    Account
    """
    USER_NAME = "f.liang@aftership.com"
    PASSWORD = "123456"


class ProductionConfig(Env, Account):
    """
    ProductionConfig
    """
    pass
