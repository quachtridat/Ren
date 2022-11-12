from typing import Coroutine

from .core import AvatarCore


class AvatarEventsCore(AvatarCore):
    async def evtNewAvatar(self, oldUser, updatedUser, invokingEvt: Coroutine = None):
        """Listener for user updates."""
        if oldUser.avatar == updatedUser.avatar:
            return

        self.logger.info(
            "%s#%s (%s) updated their avatar, saving image",
            updatedUser.name,
            updatedUser.discriminator,
            updatedUser.id,
        )
        await self.saveAvatar(updatedUser)
