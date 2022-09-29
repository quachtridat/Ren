from redbot.core import checks, commands
from redbot.core.commands.context import Context

from .commandsCore import RespectsCommandsCore


class RespectsCommands(RespectsCommandsCore):
    """Command handlers."""

    @commands.bot_has_permissions(send_messages=True, manage_messages=True)
    @commands.command(name="f")
    @commands.guild_only()
    async def plusF(self, ctx: Context):
        """Pay your respects."""
        await super().plusF(ctx, invokingCommand=self.plusF)

    @checks.mod_or_permissions(manage_messages=True)
    @commands.group(name="setf")
    @commands.guild_only()
    async def setf(self, ctx: Context):
        """Respect settings."""

    @setf.command(name="messages", aliases=["msgs"])
    @commands.guild_only()
    async def setfMessages(self, ctx: Context, messages: int):
        """Set the number of messages that must appear before a new respect is paid.

        Parameters:
        -----------
        messages: int
            The number of messages between messages.  Should be between 1 and 100
        """
        await super().setfMessages(ctx, messages, invokingCommand=self.setfMessages)

    @setf.command(name="show")
    @commands.guild_only()
    async def setfShow(self, ctx: Context):
        """Show the current settings."""
        await super().setfShow(ctx, invokingCommand=self.setfShow)

    @setf.command(name="time", aliases=["seconds"])
    @commands.guild_only()
    async def setfTime(self, ctx: Context, seconds: int):
        """Set the number of seconds that must pass before a new respect is paid.

        Parameters:
        -----------
        seconds: int
            The number of seconds that must pass.  Should be between 1 and 100
        """
        await super().setfTime(ctx, seconds, invokingCommand=self.setfTime)
