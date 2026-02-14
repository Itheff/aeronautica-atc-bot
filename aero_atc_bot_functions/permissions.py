from discord import app_commands, Interaction, Member
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Using sets for O(1) lookups
class RoleIDs:
    AMBASSADOR: int = config["permissions"]["ambassador"]
    DIRECTOR: int = config["permissions"]["director"]
    MANAGER: int = config["permissions"]["manager"]
    ATC_STAFF: int = config["permissions"]["atc_staff"]
    EVENT_HOST: int = config["permissions"]["event_host"]
    CONTROLLER: int = config["permissions"]["controller"]
    VERIFIED: int = config["permissions"]["verified"]

class ChannelIDs:
    DEBUG: int = config["channels"]["debug"]
    STAFF_BOT_COMMANDS: int = config["channels"]["staff_bot_commands"]
    BOT_COMMANDS: int = config["channels"]["bot_commands"]
    ATIS: int = config["channels"]["atis"]

def has_role(required_roles: set, admin_bypass: bool = False):
    async def predicate(ctx: Interaction) -> bool:
        if not isinstance(ctx.user, Member):
            await ctx.response.send_message("This command must be used in a server", ephemeral=True)
            return False
        
        # If a command has the admin bypass enabled, any admin can run it regardless of other roles
        # The admin bypass is disabled by default and can be individually toggled for any command
        if admin_bypass and ctx.user.guild_permissions.administrator:
                return True
        
        # Get the IDs of all roles the user currently has
        user_role_ids: set[int] = {role.id for role in ctx.user.roles}
        
        # Check if there is any overlap (intersection) between user roles and required roles
        if not user_role_ids.intersection(required_roles):
            await ctx.response.send_message("You do not have permission to run this command", ephemeral=True)
            return False
            
        return True
    return app_commands.check(predicate)

def in_channel(allowed_channels: set[int]):
    async def predicate(ctx: Interaction) -> bool:
        if ctx.channel_id in allowed_channels:
            return True
        else:
            await ctx.response.send_message("Command cannot be run in this channel", ephemeral=True)
            return False
    return app_commands.check(predicate)