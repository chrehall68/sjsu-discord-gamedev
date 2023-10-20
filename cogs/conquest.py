from discord.ext import commands
import discord
from bot.gamecomponents import Tile, Village, Army

class Plot:
    def __init__(self, size: int = 10) -> None:
        self.width = size
        self.height = size
        self.vals = [
            [Tile(x, y) for x in range(self.width)] for y in range(self.height)
        ]

    def toEmbed(self) -> discord.Embed:
        embed = discord.Embed(title="Plot")
        embed.description = "\n".join(map(lambda row: "".join(map(lambda tile: tile.display(), row)), self.vals))
        return embed


class Conquest(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.plots = {}

    @commands.command(name="conquest")
    async def play(self, ctx: commands.Context):
        await ctx.channel.send(
            f"Sorry {ctx.author}, Conquest is still under construction."
        )

    @commands.command(name="init")
    async def initPlot(self, ctx: commands.Context):
        if ctx.guild.id in self.plots:
            await ctx.send("It is already initialized.")
        else:
            self.plots[ctx.guild.id] = Plot()
            await ctx.send("It is now initialized")

    @commands.command(name="view")
    async def view(self, ctx: commands.Context):
        if ctx.guild.id in self.plots:
            await ctx.send(embed=self.plots[ctx.guild.id].toEmbed())
        else:
            await ctx.send("Sorry, no plot is initialized yet")

    @commands.command(name="claim")
    async def claim(self, ctx: commands.Context, row: int, col: int):
        if ctx.guild.id in self.plots:
            tile = self.plots[ctx.guild.id].vals[row][col]
            tile.claim(ctx.author.id)
            tile.village = Village(tile, "Center")
            await self.view(ctx)
        else:
            await ctx.send("Nope not initialized")

    @commands.command(name="view-tile")
    async def viewTile(self, ctx: commands.Context, row: int, col: int):
        if ctx.guild.id in self.plots:
            tile = self.plots[ctx.guild.id].vals[row][col]
            e = discord.Embed(title=f"Tile ({tile.x}, {tile.y})")
            e.description = tile.description(self.bot)
            await ctx.send(embed=e)
        else:
            await ctx.send("Plot not initialized")

    ''''@commands.command(name="test-id")
    async def testId(self, ctx: commands.Context):
        user = self.bot.get_user(ctx.author.id)
        await ctx.send(user.display_name)'''

async def setup(bot: commands.Bot):
    await bot.add_cog(Conquest(bot))
