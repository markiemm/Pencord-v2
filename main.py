import os, sys, json, platform, discord, random
from discord.ext import commands, tasks
from config import BOT_TOKEN, COMMAND_PREFIX, RICH_PRESENCE_STATUS

if not os.path.isfile("config.py"):
    sys.exit("'config.py' file could not be detected!")
else:
    print("config.py is detected.")


bot = commands.Bot(command_prefix=COMMAND_PREFIX)
bot.remove_command("help")

for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        bot.load_extension(f'modules.{filename[:-3]}')
        print("Successfully added modules")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-"*22)
    print("Changeing Rich Presence...")
    await bot.change_presence(activity=discord.Game(RICH_PRESENCE_STATUS))


bot.run(BOT_TOKEN)

