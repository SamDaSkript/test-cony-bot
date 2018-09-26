import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

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
    await ctx.send(":wave: @user.name")
    
@bot.command()
async def invite(ctx):
    await ctx.send("Bot Invite: https://discordapp.com/oauth2/authorize?client_id=493870175356190724&scope=bot")
    
    
bot.run('NDkzODcwMTc1MzU2MTkwNzI0.Dox77A.ZYZ5ZUJra6YVVy0cYOzM53r2QhM')

# NDkzODcwMTc1MzU2MTkwNzI0.Dox77A.ZYZ5ZUJra6YVVy0cYOzM53r2QhM
