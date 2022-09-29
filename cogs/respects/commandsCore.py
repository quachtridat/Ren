from discord.errors import HTTPException, NotFound

from redbot.core.commands.commands import Command
from redbot.core.commands.context import Context

from .constants import (
    KEY_MSGS_BETWEEN,
    KEY_TIME_BETWEEN,
)
from .events import RespectsEvents


class RespectsCommandsCore(RespectsEvents):
    """Core logic for command handlers."""

    async def plusF(self, ctx: Context, invokingCommand: Command):
        """Pay your respects."""

        async with self.plusFLock:
            if not await self.checkLastRespect(ctx):
                # New respects to be paid
                await self.payRespects(ctx)
            elif not await self.checkIfUserPaidRespect(ctx):
                # Respects exists, user has not paid their respects yet.
                await self.payRespects(ctx)
            else:
                # Respects already paid by user!
                pass
            try:
                await ctx.message.delete()
            except NotFound:
                self.logger.debug("Could not find the old respect")
            except HTTPException:
                self.logger.error("Could not retrieve the old respect", exc_info=True)

    async def setfMessages(self, ctx: Context, messages: int, invokingCommand: Command):
        """Set the number of messages that must appear before a new respect is paid.

        Parameters:
        -----------
        messages: int
            The number of messages between messages.  Should be between 1 and 100
        """

        if messages < 1 or messages > 100:
            await ctx.send(
                ":negative_squared_cross_mark: Please enter a number " "between 1 and 100!"
            )
            return

        guildConfig = self.config.guild(ctx.guild)

        await guildConfig.get_attr(KEY_MSGS_BETWEEN).set(messages)
        timeBetween = await guildConfig.get_attr(KEY_TIME_BETWEEN)()

        await ctx.send(
            ":white_check_mark: **Respects - Messages**: A new respect will be "
            "created after **{}** messages and **{}** seconds have passed "
            "since the previous one.".format(messages, timeBetween)
        )

        self.logger.info(
            "%s#%s (%s) changed the messages between respects to %s messages",
            ctx.message.author.name,
            ctx.message.author.discriminator,
            ctx.message.author.id,
            messages,
        )

    async def setfShow(self, ctx: Context, invokingCommand: Command):
        """Show the current settings."""

        guildConfig = self.config.guild(ctx.guild)

        timeBetween = await guildConfig.get_attr(KEY_TIME_BETWEEN)()
        msgsBetween = await guildConfig.get_attr(KEY_MSGS_BETWEEN)()

        msg = ":information_source: **Respects - Current Settings:**\n"
        msg += "A new respect will be made if a previous respect does not exist, or:\n"
        msg += "- **{}** messages have been passed since the last respect, **and**\n"
        msg += "- **{}** seconds have passed since the last respect."
        await ctx.send(msg.format(msgsBetween, timeBetween))

    async def setfTime(self, ctx: Context, seconds: int, invokingCommand: Command):
        """Set the number of seconds that must pass before a new respect is paid.

        Parameters:
        -----------
        seconds: int
            The number of seconds that must pass.  Should be between 1 and 100
        """

        if seconds < 1 or seconds > 100:
            await ctx.send(
                ":negative_squared_cross_mark: Please enter a number " "between 1 and 100!"
            )
            return

        guildConfig = self.config.guild(ctx.guild)

        await guildConfig.get_attr(KEY_TIME_BETWEEN).set(seconds)
        messagesBetween = await guildConfig.get_attr(KEY_MSGS_BETWEEN)()

        await ctx.send(
            ":white_check_mark: **Respects - Time**: A new respect will be "
            "created after **{}** messages and **{}** seconds have passed "
            "since the previous one.".format(messagesBetween, seconds)
        )

        self.logger.info(
            "%s#%s (%s) changed the time between respects to %s seconds",
            ctx.message.author.name,
            ctx.message.author.discriminator,
            ctx.message.author.id,
            seconds,
        )
