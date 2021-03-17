import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(Self,bot):
        self.bot = bot
        self.slash = bot.slash

    async def hello(Self,ctx):
        await ctx.send("hello")


def setup(bot):
    bot.add_cog(Admin(bot))
