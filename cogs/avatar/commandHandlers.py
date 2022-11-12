from redbot.core import checks, commands
from redbot.core.commands.context import Context

from .commandsCore import AvatarCommandsCore


class AvatarCommandHandlers(AvatarCommandsCore):
    @commands.group(name="avatar")
    @checks.mod_or_permissions()
    @commands.guild_only()
    async def _grpAvatar(self, ctx: Context):
        """Avatar commands."""

    @_grpAvatar.command(name="save")
    async def _cmdSaveAvatars(self, ctx: Context):
        await self.cmdSaveAvatars(ctx, invokingCmd=self._cmdSaveAvatars)
