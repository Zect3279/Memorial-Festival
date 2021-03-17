import discord
from discord.ext import commands
from discord_slash import SlashCommand

from os import environ
import json


class Amaner(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(environ.get('PREFIX', '/')),
            help_command=None,
        )
        self.slash = SlashCommand(self, sync_commands=True)

    # async def on_ready(self):
        # status = discord.Game("メンテナンス中")
        # await self.change_presence(activity=status)
