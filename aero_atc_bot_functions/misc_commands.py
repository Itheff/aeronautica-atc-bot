import discord.app_commands, discord.utils
from discord import Interaction, ForumChannel, CategoryChannel
from random import randint
from .permissions import has_role, RoleIDs, in_channel, ChannelIDs

@discord.app_commands.command(description="Ping the bot and it will say \"Pong!\" in response")
@has_role({RoleIDs.VERIFIED})
@in_channel({ChannelIDs.BOT_COMMANDS, ChannelIDs.STAFF_BOT_COMMANDS, ChannelIDs.DEBUG})
async def ping(ctx: Interaction):
    await ctx.response.send_message("Pong!")

@discord.app_commands.command(description="Gives the current time in UTC/GMT")
@has_role({RoleIDs.VERIFIED})
@in_channel({ChannelIDs.BOT_COMMANDS, ChannelIDs.STAFF_BOT_COMMANDS, ChannelIDs.DEBUG})
async def utc(ctx: Interaction):
    await ctx.response.send_message(f"{discord.utils.utcnow().strftime('%H%Mz')}")

@discord.app_commands.command(description="Generate a 4 digit squawk code")
@has_role({RoleIDs.VERIFIED})
@in_channel({ChannelIDs.BOT_COMMANDS, ChannelIDs.STAFF_BOT_COMMANDS, ChannelIDs.DEBUG})
async def generate_squawk(ctx: Interaction):
    squawk: str = ""
    for i in range(4):
        squawk += str(randint(0,7))
    if squawk in {"1200", "7000", "7500", "7600", "7700", "7777", "0000"}:
        await ctx.response.send_message("Unknown error, please try again.", ephemeral=True)
    await ctx.response.send_message(f"Generated squawk code: {squawk}")

@discord.app_commands.command(description="Makes the bot say the given message")
@has_role({RoleIDs.DIRECTOR, RoleIDs.AMBASSADOR})
async def say(ctx: Interaction, message: str):
    if not (isinstance(ctx.channel, ForumChannel) or isinstance(ctx.channel, CategoryChannel)):
        if ctx.channel is not None:
            await ctx.response.send_message("Message sucessfully sent", ephemeral=True, delete_after=3)
            await ctx.channel.send(message)
        else:
            await ctx.response.send_message("An unknown error has occured", ephemeral=True)
    else:
        await ctx.response.send_message("Channel type unsupported", ephemeral=True)