
# Dev config file
class Env:
    """
    Env
    """
    URL = "https://marketing.automizely.io/"


class Account:
    """
    Account
    """
    USER_NAME = "autotest.aftership@gmail.com"
    PASSWORD = "$^*ENCRYPT=Bx4VCABTGGZhf2UuEQ==?&#$"


class AfterShipTool:
    """
    AfterShipTool
    """
    AUTHORIZATION = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJiUVJJakd5QjZMX1dJODd1ZW81dGhKdUdGNXZoZGdNc3NFZDNiLXd6WjY4In0.eyJleHAiOjE2MjcwMDcxNTYsImlhdCI6MTYyNzAwNTM1NiwiYXV0aF90aW1lIjoxNjI3MDA1MzU2LCJqdGkiOiJhOTRhZTE2Ny0wYTc4LTRiOWEtOGRlMS1mNmY5MjYyY2U3ZTUiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmF1dG9taXplbHkuY29tL2F1dGgvcmVhbG1zL2VtcGxveWVlIiwiYXVkIjpbImJyb2tlciIsImFjY291bnQiXSwic3ViIjoiMDE5NTdkYjUyMWVjNDFmNGJkNDJlNGUwNDc1ZmJiYWEiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJhZG1pbi1wb3J0YWwiLCJub25jZSI6IjI2YTU5N2MzLTgxZmMtNDdlMS1iNmRlLWU2YjcyNDdjNWZiOCIsInNlc3Npb25fc3RhdGUiOiIyMDUyOGY5NS0xNDAyLTQ0ZTctODNmMC0wMWM2NTViNmRkNzgiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHBzOi8vYWRtaW4uYXV0b21pemVseS5vcmciLCJodHRwczovL2FkbWluLmF1dG9taXplbHkuZGV2IiwiaHR0cDovL2xvY2FsaG9zdDo4MDAwIiwiaHR0cDovL2xvY2FsaG9zdDozMDAwIiwiaHR0cDovL2xvY2FsaG9zdDo3MDk5Il0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFkbWluLXBvcnRhbCI6eyJyb2xlcyI6WyJhZnRlcnNoaXAtcmVhZGVyIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJGZW5nIExpYW5nLCBKZWZmIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiZi5saWFuZ0BhZnRlcnNoaXAuY29tIiwiZ2l2ZW5fbmFtZSI6IkZlbmciLCJmYW1pbHlfbmFtZSI6IkxpYW5nLCBKZWZmIiwiZW1haWwiOiJmLmxpYW5nQGFmdGVyc2hpcC5jb20ifQ.s8THQ6wsdj3FMDfdoY1S8eZgjQWc1EiPL36XtM1JjayCu04_wCs2sNl2fYtPaRvr9eBjT7AR8644BqgUr0MxlNCgkJqJ2dPKREfrQUyo0AcyjVP30-t4l2TDg3NxAa4hwKFTdBmmAymEQ9W7wRGzfB_TOd7uuJc3dp-7bOM1X2Lf6mRw2YHXX5EOBQV32Bh0hx39OHvQf9iqdkGgk_vPnP7eyw_TbfO2Kk2qBPGk9rAHXPbBgLqWpywbjgYRA-2WcQpF6Cu2h7oxtzeOOT7turzq5ZVo0cDT1MPMbPpPCfx6gcDVbqxGmsIz0KMMQjrvL1zYOUrqUDPdLZ2cgKAMdA"


class TestingConfig(Env, Account, AfterShipTool):
    """
    TestingConfig
    """
    pass
