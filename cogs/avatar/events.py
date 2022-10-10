from redbot.core.commands import commands

from .eventsCore import AvatarEventsCore


class AvatarEvents(AvatarEventsCore):
    @commands.Cog.listener("on_user_update")
    async def newAvatarListener(self, oldUser, updatedUser):
        await super().newAvatarListener(
            oldUser, updatedUser, invokingEventListener=self.newAvatarListener
        )
