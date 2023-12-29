import os

BACKEND = 'Telegram'

BOT_DATA_DIR = './data'
BOT_EXTRA_PLUGIN_DIR = './plugins'

# Cargar valores de username y token desde env_variables.env
BOT_IDENTITY = {
    'username': os.getenv('BOT_USERNAME'),
    'token': os.getenv('BOT_TOKEN')
}