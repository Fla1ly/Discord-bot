import discord
from discord.ext import commands
from config import config
from openai import OpenAI

client = OpenAI(api_key=config.OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

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
        {"role": "system", "content": "You are only answering questions about global warming."},
        {"role": "user", "content": prompt},
    ])

    await message.channel.send(response.choices[0].message.content)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Zapisano obraz w ./{attachment.filename}")
        else:
            await ctx.send("Zapomniałeś załadować obraz :(")

bot.run(config.DISCORD_BOT_TOKEN)
