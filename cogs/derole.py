import discord
from discord.ext import commands

class DeRole(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.slash = bot.slash

    @commands.Cog.listener()
    async def on_ready(self):
    guild: discord.Guild = bot.get_guild(808283612105408533)
    role: disocrd.Role = discord.utils.get(guild.roles, name="Guest")
    mems = []
    async for mem in guild.members:
        await mem.remove_roles(roles=role,reason="記念祭に参加するため")
        mems += [mem.name]
        print('取得完了: {0}'.format(len(mems)), end='\r')
    print('取得完了')

    @commands.command()
    async def fes(self,ctx):
        guild: discord.Guild = ctx.author.guild
        role: disocrd.Role = discord.utils.get(guild.roles, name="Guest")
        await ctx.author.remove_roles(roles=role,reason="記念祭に参加するため")


def setup(bot):
    bot.add_cog(DeRole(bot))
