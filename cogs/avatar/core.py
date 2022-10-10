from datetime import datetime
import logging
import os
import pathlib

import discord

from redbot.core import data_manager
from redbot.core.bot import Red


class AvatarCore:
    def __init__(self, bot: Red):
        self.bot = bot
        self.saveFolder = data_manager.cog_data_path(cog_instance=self)
        self.logger = logging.getLogger("red.luicogs.Avatar")
        if self.logger.level == 0:
            # Prevents the self.logger from being loaded again in case of module reload.
            self.logger.setLevel(logging.INFO)
            logPath = os.path.join(self.saveFolder, "info.log")
            handler = logging.FileHandler(filename=logPath, encoding="utf-8", mode="a")
            handler.setFormatter(
                logging.Formatter("%(asctime)s %(message)s", datefmt="[%d/%m/%Y %H:%M:%S]")
            )
            self.logger.addHandler(handler)

    async def saveAvatar(self, user: discord.User):
        """Save avatar images to the cog folder.

        Parameters
        ----------
        user: discord.User
            The user of which you wish to save the avatar for.
        """
        avatar = user.avatar_url_as(format="png")
        currentTime = datetime.now().strftime("%Y%m%d-%H%M%S")
        userPath = os.path.join(self.saveFolder, str(user.id))
        pathlib.Path(userPath).mkdir(parents=True, exist_ok=True)
        filePath = os.path.join(userPath, f"{user.id}_{currentTime}.png")
        await avatar.save(filePath)
        self.logger.debug("Saved image to %s", filePath)
