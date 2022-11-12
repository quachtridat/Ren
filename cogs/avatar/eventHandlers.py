from redbot.core.commands import commands

from .eventsCore import AvatarEventsCore


class AvatarEventHandlers(AvatarEventsCore):
    @commands.Cog.listener("on_user_update")
    async def _evtNewAvatar(self, oldUser, updatedUser):
        await self.evtNewAvatar(oldUser, updatedUser, invokingEvt=self._evtNewAvatar)
