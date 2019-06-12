[![HitCount](http://hits.dwyl.io/AdityaTelange/Python-Telegram-Bot-SAMPLE-STRUCTURE.svg)](http://hits.dwyl.io/AdityaTelange/Python-Telegram-Bot-SAMPLE-STRUCTURE)

# Python-Telegram-Bot [SAMPLE-STRUCTURE]

A sample Structure for creating Telegram Bots in Python3 Using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## Installing
```bash
$ clone https://github.com/AdityaTelange/Python-Telegram-Bot-SAMPLE-STRUCTURE

$ pip3 install -r requirements.txt
```
Edit .env file 

```
MODE= <'prod'|'dev'>
TOKEN= <token given by BotFather>
OWNER_ID= <chat_id of owner>

# only for 'prod' MODE
DOMAIN= < domain of hosted server, uses WEB-HOOK>
APP_NAME= < appname, subdomain of hosted server >
```
Ex
```
MODE= 'prod'
TOKEN= 'xxxxxxxxx:qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'
OWNER_ID= 000000000

# only for 'prod' MODE
DOMAIN= 'heroku.com'
APP_NAME= 'mybot'
```
so webhook is at `mybot.heroku.com/xxxxxxxxx:qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq`

## Running

```
python3 server.py
```
