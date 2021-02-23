# simplebot
basic template for people first using discord.py

[![python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/) [![python](https://img.shields.io/badge/discord.py-latest-ff69b4.svg)](https://github.com/Rapptz/discord.py)

* [How To Download](#how-to-download)
* [Setting Up](#setting-up)
* [Running The Bot](#running-the-bot)

## How to download
Make sure you have [discord.py](https://github.com/Rapptz/discord.py) and [Python](https://www.python.org/) installed.

```sh
# Linux/macOS
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```
You can download this Repository / Bot by doing
`
git clone https://github.com/dromzeh/simplebot/
` in a command line.

## Setting Up

Once you have installed discord.py, download the bot.py file. Save it in any location to your liking.
Edit bot.py [DO NOT RUN] - On line 11 - 13, enter in your BOT token, prefix of choice and what you want your bot to play.
Don't have a bot made yet? Go to the [Discord Developer Portal](https://discord.com/developers/applications), make an application. Once made, go onto the "bot" tab. And follow instructions, in the bot tab, you will see your token. DO NOT share this with anyone; don't panic if you do, you can always regenerate a new one.

To invite the bot to your server, get your bot's client id from the developer portal. Use [this website](https://discordapi.com/permissions.html) to generate an invite link to your bot and give it the permissions you want.

## Running The Bot
Once you have invited your bot to the server and filled out bot.py. Run bot.py.
You can do this in different ways, if you're using a text editor; some are built in. 
For windows, you can open a cmd prompt in the same area the bot is located and run
`python bot.py`.

If everything has ran correctly, you'll see a message like `Bot is ready! Logged in as BOT_NAME [CLIENT_ID]`
To view commands, do `help`, where it'll display all commands.

## Crediting
You do not owe any credit, but it is appreciated.
