from discord.ext import commands


class Conquest(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="conquest")
    async def play(self, ctx: commands.Context):
        await ctx.channel.send(
            f"Sorry {ctx.author}, Conquest is still under construction."
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Conquest(bot))
