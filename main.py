#!/usr/bin/python3
from JetLagBot import JetLagBot
from discord import Intents
from pathlib import Path

token_path = Path(__file__).parent.joinpath("token.txt").absolute()


intents = Intents.default()
intents.message_content = True
intents.members = True

def main():
    bot = JetLagBot(intents=intents)
    bot.run(get_token())

def get_token() -> str:
    with open(token_path, 'r') as file:
        return file.read().strip()

if __name__ == "__main__":
    main()