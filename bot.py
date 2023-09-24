import discord
from discord.ext import commands
from discord import Intents
import os


class Bot(commands.Bot, discord.Client):
    def __init__(self, command_prefix: str, intents: Intents) -> None:
        super().__init__(command_prefix, intents=intents)

    async def load_cogs(self):
        """
        Load all cogs in the cogs directory
        """
        cogs = os.listdir("cogs")
        if "__pycache__" in cogs:
            cogs.remove("__pycache__")  # ignore __pycache__

        print("loading cogs: ", " ".join(cogs))

        # add the cogs
        for cog in cogs:
            cog = cog.strip(".py")
            name = cog.title()  # name of the class

            # module
            module = getattr(__import__("cogs." + cog), cog)

            # add the cog
            await self.add_cog(getattr(module, name)(self))
        print("all cogs loaded")

    async def reload_cogs(self):
        cogs = list(self.cogs.keys())
        for cog in cogs:
            print("removing cog: ", cog)
            await self.remove_cog(cog)

        await self.load_cogs()

    async def on_ready(self):
        """
        Runs once the bot has logged in and is ready to be used
        """
        await self.load_cogs()
        print("bot is fully ready!")
