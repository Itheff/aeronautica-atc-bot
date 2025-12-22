from discord import Interaction, Role, Member
from enum import Enum
from typing import List

class Permissions(Enum):
    NONE = []
    ABASSADOR_ONLY = [1175138965054042212]
    DIRECTORS_ONLY = [1175138965054042212, 1180831972440944750]
    STAFF_ONLY = [1292556748774838405]
    CONTROLLERS_ONLY = [1168202336942948393]
    VERIFIED_ONLY = [1120128265668022292]

async def check_permissions(ctx: Interaction, permissions: Permissions) -> bool:
    # This first check is to make sure that the command was run in the server, as the ctx.user attribute would be a User
    # object if the command was run in someones' DM's (somehow). It also shuts up PyRight type-checking.
    if isinstance(ctx.user, Member):
        member_roles: List[Role] = ctx.user.roles
        for perm_role in permissions.value:
            for member_role in member_roles:
                if member_role.id == perm_role:
                    return True
        await ctx.response.send_message("You do not have permission to run this command", ephemeral=True)
        return False
    else:
        await ctx.response.send_message("Command can only be run in the Aeronautica ATC server")
        return False