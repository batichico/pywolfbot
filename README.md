# PyWolfBot

PyWolfBot is a Telegram bot created with Errbot to simulate the "Castronegro" board game on the messaging platform.

## Description

This bot allows users to play the Castronegro board game directly from Telegram. It provides functionalities to manage game sessions, handle game events, and maintain a log of users and activities.

## Directory Structure

pywolfbot/
├── app/
│ └── users.json
├── bot.py
├── docker-compose.yml
├── Dockerfile
├── functions/
│ ├── json_logic.py
│ ├── user_handler.py
│ └── utils.py
├── .gitignore
├── plugins/
│ └── events/
│ ├── start.py
│ └── welcomes.py
├── README.md
├── requirements.txt
└── .github/
└── workflows/
└── ci.yaml
└── config/
└── env_variables.env
└── errbot_config_vars.py


## Deployment

### Requirements

- Python 3.x
- Docker

### Deployment Instructions

To create the project's directory structure with a single command, use the following:

> [!WARNING]
> Be cautious when executing commands in your terminal. The command below will create and modify files in your system.

```bash
mkdir -p pywolfbot/{app,functions,plugins/events,.github/workflows/config} && \
touch pywolfbot/{bot.py,docker-compose.yml,Dockerfile,.gitignore,README.md,requirements.txt} && \
touch pywolfbot/app/users.json && \
touch pywolfbot/functions/{json_logic.py,user_handler.py,utils.py} && \
touch pywolfbot/plugins/events/{start.py,welcomes.py} && \
mkdir -p pywolfbot/.github/config && \
touch pywolfbot/.github/workflows/ci.yaml && \
touch pywolfbot/.github/config/{env_variables.env,errbot_config_vars.py}
```

This command will create the necessary directory structure and files for the PyWolfBot project in a single step.

If you encounter issues or want to contribute, please create an issue in the repository.

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for more details.
