import discord.app_commands, discord.utils
from discord import Interaction
import datetime
from typing import List

@discord.app_commands.command()
async def ping(ctx: Interaction):
    await ctx.response.send_message("Pong!")

@discord.app_commands.command()
async def utc(ctx: Interaction):
    await ctx.response.send_message(f"{discord.utils.utcnow().strftime("%H%Mz")}")

# IMPORTANT: ADD COMMAND OBJECT TO THIS LIST OTHERWISE IT WILL NOT BE LOADED AND WILL NOT WORK
ALL_COMMANDS: List[discord.app_commands.Command] = [ping, utc] 