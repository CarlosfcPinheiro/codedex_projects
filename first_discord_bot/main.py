# Import library/package discord to access discord API
import discord
import os
from dotenv import load_dotenv
# Load .env file and get BOT_TOKEN
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Import class Meme
from meme import Meme

# Creating child class inheriting the discord.Client class
class MyClient(discord.Client):
    # Built-in method from the discord package that is called when the Discord's bot login is successfull
    async def on_ready(self) -> None:
        print(f'Logged on as {self.user}')
    # Method that listen for a message and read the invited message
    async def on_message(self, message) -> None:
        if (message.author == self.user):
            return
        if (message.content.startswith('$hello')):
            # Wait the method execution
            await message.channel.send('Hello, world!')
        if (message.content.startswith('$meme')):
            # Call static method get_meme
            await message.channel.send(Meme.get_meme())

# Setting the basic configuration for the bot
intents = discord.Intents.default()
# Allow to interact with messages
intents.message_content = True
# instaciates MyClient class and passing the parameter intentes
client = MyClient(intents=intents)
# Run the application
client.run(BOT_TOKEN)