# Discord PyFun

discord-pyfun is a collection of bot plugins and services that interact with a Discord Server. This is a playground of sorts.

## Getting Started
Clone the repository & navigate to the project
```bash
git clone https://github.com/ShantzPantz/discord-pyfun.git && cd discord-pyfun
```

First we must create a config.py configuration file from the config.py.template.
```bash
cp src/config.py.template src/config.py
```

Edit the newly created config.py to include your Discord API key and any additional API keys that are required.

## Requirements

- Python 3.4+

Install Python Requirements
```bash
pip install -r requirements.txt
```

## Run the bot
```bash
cd src
python main.py
```

Heavily inspired by a Facebook Messenger bot: [https://github.com/sentriz/steely](https://github.com/sentriz/steely)
