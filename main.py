from bot import AeroATCBot
import logging
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN: str = os.environ["DISCORD_TOKEN"]

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

if __name__ == "__main__":
    bot = AeroATCBot()
    bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)