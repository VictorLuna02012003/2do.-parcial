import os
import discord
from discord.ext import commands
import pytube
import openai

TOKEN='MTA4MjI5NDI4NTgyMDQ5ODAzMQ.G0Wwg_.Ti3_wTQgfFwBaj0p_5YEYnsLymAY3rZ6R-N5wg'

intents= discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("Bot conectado a discord")

@client.event
async def on_message(message):
  if message.content.startswith("!hello"): 
    await message.channel.send("Hola crack")
    
  if message.content.startswith("!sumar"):
    numeros = message.content.split()[1:]
    resultado = sum([float(numeros) for num in numeros])
    await message.channel.send(f"El resultado de la suma es: {resultado}")

  if message.content.startswith("!download"):
    url = message.content.split('')[1]
    yt = pytube.YouTube(url)
    stream = yt.streams.get.highest_resolution()
    filename = stream.download()
    await message.channel.send(f'Video descargado como {filename}')
    os.system(f'start {filename}')

  if message.content.startswith('!AI'):
    prompt = message.content #Es el contenido del mensage
    response = openai.Completion.create(engine = "")
    
client.run(TOKEN)