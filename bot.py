from discord.ext.commands.bot import Bot
import discord.utils
from discord import Object, Intents
import aero_atc_bot_functions

class AeroATCBot(Bot):

    # This variable is a bit odd but in order to pass a guild id to the commands, the id must be a discord.py
    # object (small "o"). Thus, we create a basic Object class with the id of the AeroATC server and use that
    aero_atc_guild_id = Object(id=1120012114321494088)
    
    def __init__(self):
        super().__init__(command_prefix=":)", intents=Intents.all())
    
    def run_with_token(self):
        file = open("token.txt", "r")
        token = file.read()
        self.run(token=token)

    async def add_all_commands(self):
        for command in aero_atc_bot_functions.ALL_COMMANDS:
            self.tree.add_command(command, guild=self.aero_atc_guild_id)
        await self.tree.sync(guild=self.aero_atc_guild_id)
        print("Commands have been loaded")
    
    async def on_ready(self):
        print(f"Logged in as {self.user} at {discord.utils.utcnow().time()}")
        await self.add_all_commands()