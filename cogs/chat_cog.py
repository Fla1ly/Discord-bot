from discord.ext import commands
from openai import OpenAI

client = OpenAI()

class ChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  

        prompt = message.content
        response = client.completions.create(model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150)

        await message.channel.send(response.choices[0].text)

def setup(bot):
    bot.add_cog(ChatCog(bot))
