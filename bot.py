import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")
    
@bot.command()
async def wave(ctx):
    await ctx.send(":wave:")
    
    
bot.run('https://discordapp.com/api/webhooks/494346956370608128/4xbRZRkZ6r8C4MxpEdJMEZOOfpYUCMGkc99uze_fEVL3ynOt_Ierm57tFv9TjAyqerEN')

# NDkzODcwMTc1MzU2MTkwNzI0.Dox77A.ZYZ5ZUJra6YVVy0cYOzM53r2QhM
