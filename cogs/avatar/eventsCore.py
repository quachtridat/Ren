from .core import AvatarCore


class AvatarEventsCore(AvatarCore):
    async def newAvatarListener(self, oldUser, updatedUser, invokingEventListener=None):
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
