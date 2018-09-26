import discord
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
async def help(ctx):
    await ctx.send("------------------------------------------
Discord Commands:
1. /reload (Reload the server and discord bot!)
2. /help (Help with the bot!)
3. /inivte (Give's you the discord invite!)
4. /creator (Tell's you the creator's of this discord and me!)
------------------------------------------")
    
@bot.command()
async def wave(ctx):
    await ctx.send(":wave: {0.author.mention}")
    
bot.run('NDkzODcwMTc1MzU2MTkwNzI0.Dox77A.ZYZ5ZUJra6YVVy0cYOzM53r2QhM')
