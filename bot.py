import discord

class AeronauticaATCBot(discord.Client):

    def __init__(self, intents):
        super().__init__(intents=intents)

    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)