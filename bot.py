import discord
from discord.ext import commands
from config import config
from openai import OpenAI

client = OpenAI(api_key=config.OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

# Set up OpenAI API key

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    # Replace GUILD_ID and CHANNEL_ID with your server and channel IDs
    GUILD_ID = 1177921969199525899
    CHANNEL_ID = 1177921969702830133

    guild = bot.get_guild(GUILD_ID)
    channel = guild.get_channel(CHANNEL_ID)

    if channel:
        await channel.send("I'm online now!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return 

    prompt = message.content
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ])

    await message.channel.send(response.choices[0].message.content)

# Run the bot
bot.run(config.DISCORD_BOT_TOKEN)
