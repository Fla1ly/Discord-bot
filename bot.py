import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  

from config import config
import openai

openai.api_key = config.OPENAI_API_KEY

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return  

    prompt = message.content
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )

    await message.channel.send(response['choices'][0]['text'])

bot.run(config.DISCORD_BOT_TOKEN)
