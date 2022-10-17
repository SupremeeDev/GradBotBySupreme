#############################################
##                                         ##
##       Bot Developer: $upreme#1337       ##
##                                         ##  
#############################################

import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix="!") ## PREFIX 

api_key = "" ## Ovdje stavite Api Key koji mozete naci na: api.openweathermap.com/api

@bot.event
async def on_ready():
    print("Bot Status: Online")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Bot Dev: $upreme#1337")) ## Bot Status

@bot.command()
async def grad(ctx, grad = None):
    if grad == None:
        await ctx.reply("Nisi upisao Grad!")
        return

    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={grad}")
    data = response.json()

    if data["cod"] != "404":
        data1 = data["main"]
        data2 = data["wind"]
        data3 = data["sys"]
        data4 = data["clouds"]

        temperatura = data1["temp"]
        temp = str(round(temperatura - 273.15))
        pritisakuzraku = data1["pressure"]
        vlaznost = data1["humidity"]
        brzina = data2["speed"]
        drzava = data3["country"]
        imegrada = data["name"]
        oblaci = data4["all"]
        kokain = data["timezone"]
        koks = (kokain//3600)
        z = data["weather"]
        weather_description = z[0]["description"]

        embed = discord.Embed(description=f'**Trenutno:**\nGrad: **{imegrada}**\nDrzava: **{drzava}**\nTemperatura: **{temp}**°C\nBrzina vazduha: **{brzina}km/h**\nVlaznost vazduha: **{vlaznost}**%',color=discord.Color(0x0074ff), timestamp=ctx.message.created_at,)
        embed.set_author(name=f'Grad: {imegrada} / {drzava}', icon_url=f'{ctx.author.avatar_url}')
        embed.set_footer(text=f'{ctx.author.name}')
        await ctx.reply(embed=embed)
    else:
        await ctx.reply("Grad nije pronadjen")


bot.run("") ## Bot Token
