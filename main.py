main.py

@bot.event
async def on_member_update(ctx, before, after):
    if after.name == "SomeUser":
        await after.ban()

import disnake
from disnake.ext import commands
from disnake.ext.commands import Bot

intents = Intents.default()
intents.value |= disnake.Intents.messages.flag
intents.value |= disnake.Intents.message_content.flag
intents.value |= disnake.Intents.guilds.flag
intents.value |= disnake.Intents.members.flag

bot = Bot(
  command_prefix="&',
  sync_commands=True,
  intents=intents,
)

from dotenv import load_dotenv
import disnake
from disnake.ext import commands
from disnake.ext.commands import Bot
