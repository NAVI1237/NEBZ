import os
from server import start_server
from discord.ext import commands

bot = commands.Bot(command_prefix='nz!', case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user}: Im Ready'

@bot.event
extensions = [
    'commands.register'
]

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)
        
    start_server()
    bot.run(os.environ.get('TOKEN'))