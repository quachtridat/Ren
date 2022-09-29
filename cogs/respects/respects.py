"""Respects cog
A replica of +f seen in another bot, except smarter..
"""

from redbot.core.commands import Cog
from .commands import RespectsCommands


class Respects(Cog, RespectsCommands):
    """Pay your respects."""
