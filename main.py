from bot import Amaner
import setting

bot = Amaner()

BOT_TOKEN = setting.BOT

extensions = [
    "cogs.admin",
    "cogs.derole",
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(BOT_TOKEN)
