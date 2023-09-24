import dotenv
import discord
from bot import Bot

if __name__ == "__main__":
    # make sure that we can access message content
    intents = discord.Intents.default()
    intents.message_content = True

    # create bot
    bot = Bot(command_prefix="-", intents=intents)

    # run bot
    bot.run(dotenv.get_key(".env", "BOT_TOKEN"))
