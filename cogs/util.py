from discord.ext import commands
from datetime import datetime


class Util(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.channel.send("ping: ", datetime.now() - ctx.message.created_at)

    @commands.command(name="reload_cogs")
    async def reload_cogs(self, ctx: commands.Context):
        await ctx.channel.send("Reloading cogs...")
        await self.bot.reload_cogs()
        await ctx.channel.send("All cogs reloaded!")
