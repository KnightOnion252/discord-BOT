from botkey import *
import discord

client = discord.Client()

messages=["Hi","Hello","Greetings","ARRRRRRRRRRRRRRRRRRGHH!","Namaste","Beep Boop","Ayya re Ayya","Knock Knock","Not this guy again"]
message=message[randrange(7)]
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(message) #To be set randomly

client.run(token)
