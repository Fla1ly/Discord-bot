from discord.ext import commands
import openai

class ChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # Ignore messages from bots

        # Use OpenAI to generate a response
        prompt = message.content
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )

        # Send the generated response to the same channel
        await message.channel.send(response.choices[0].text)

def setup(bot):
    bot.add_cog(ChatCog(bot))
