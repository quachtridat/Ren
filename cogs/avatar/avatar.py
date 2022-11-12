"""Download avatars when people change them."""
from redbot.core import commands
from redbot.core.bot import Red

from .commandHandlers import AvatarCommandHandlers
from .eventHandlers import AvatarEventHandlers


class Avatar(commands.Cog, AvatarCommandHandlers, AvatarEventHandlers):
    """The Avatar collector."""

    def __init__(self, bot: Red):
        super().__init__(bot)
