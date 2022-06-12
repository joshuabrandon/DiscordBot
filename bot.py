# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

import steam_game_output as sgo

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='MockAndy', help='Makes fun of Andy with Andy facts')
async def andy_jokes(ctx):
    andy = [
        "Andy is an Iron LoL player (barely)."
        ,"Andy could easily be defeated by a loaf of bread."
        ,"Andy has a golf handicap of 69."
        ,"The year is 2099. Andy has not yet beat Elden Ring."
    ]

    response = random.choice(andy)
    await ctx.send(response)
    
@bot.command(name='MockEkin', help='Makes fun of Ekin with Ekin facts')
async def ekin_jokes(ctx):
    ekin = "No."

    response = ekin
    await ctx.send(response)

@bot.command(name='MockNina', help='Makes fun of Nina with Nina facts')
async def nina_jokes(ctx):
    nina = "No."

    response = nina
    await ctx.send(response)
    
@bot.command(name='WhatYouPlaying', help='Responds with the Steam game currently being played by a user')
async def steam_game(ctx, player_name):
    
    response = sgo.get_steam_game(player_name)
    await ctx.send(response)
    
#@bot.command(name='jamal', help='Responds with whatever game Jamal is playing on Steam right now')
#async def nine_nine(ctx):
#    
#
#    response = 
#    await ctx.send(response)

bot.run(TOKEN)