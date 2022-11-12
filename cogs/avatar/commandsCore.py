from redbot.core.commands.commands import Command
from redbot.core.commands.context import Context

from .core import AvatarCore


class AvatarCommandsCore(AvatarCore):
    async def cmdSaveAvatars(self, ctx: Context, invokingCmd: Command = None):
        """Save all avatars in the current guild."""
        async with ctx.typing():
            for member in ctx.guild.members:
                await self.saveAvatar(member)
            await ctx.send("Saved all avatars!")
