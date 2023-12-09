import discord
from bot_logic import *
from discord.ext import commands

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Zalogowaliśmy się jako {client.user}")
    await client.get_channel(1177921969702830133).send("Bot jest online!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Cześć!")
    elif message.content.startswith("$bye"):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("$smile"):
        await message.channel.send(gen_emodji())
    elif message.content.startswith("$coin"):
        await message.channel.send(flip_coin())
    elif message.content.startswith("$pass"):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith("$add"):
        await message.channel.send("test")
    else:
        await message.channel.send(message.content)

client.run("MTE3NzkyMjc2NzE2NTg1NzgxMg.GYcQ0a.GquCQ_LzT1AcuKBAQnj5dn90MLV6TITGB63re8")

gen_pass(10)
