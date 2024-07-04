import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5426256591:AAEvazeK7dvvOVn5zJitkZErX7ESo9-s0Kc")

    APP_ID = int(os.environ.get("APP_ID", 25802886))

    API_HASH = os.environ.get("API_HASH", "a1ca0b577d1d9a68e34996e166df5269")