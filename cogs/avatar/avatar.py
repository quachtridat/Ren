"""Download avatars when people change them."""
from redbot.core import commands
from redbot.core.bot import Red

from .commands import AvatarCommands
from .events import AvatarEvents


class Avatar(commands.Cog, AvatarCommands, AvatarEvents):
    """The Avatar collector."""

    def __init__(self, bot: Red):
        super().__init__(bot)
