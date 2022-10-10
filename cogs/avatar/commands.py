from redbot.core import checks, commands
from redbot.core.commands.context import Context

from .commandsCore import AvatarCommandsCore


class AvatarCommands(AvatarCommandsCore):
    @commands.group(name="avatar")
    @checks.mod_or_permissions()
    @commands.guild_only()
    async def _avatar(self, ctx: Context):
        """Avatar commands."""

    @_avatar.command(name="save")
    async def _saveAvatars(self, ctx: Context):
        await super()._saveAvatars(ctx, self._saveAvatars)
