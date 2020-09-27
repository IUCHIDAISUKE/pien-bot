import discord
import random
import os

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

yokopien = "ぴえん:pleading_face:"
tatepien = "ぴ\nえ\nん\n:pleading_face:"
squarepien = "ぴ:pleading_face:\nえん"
lpien = "ぴえん\n:pleading_face:"


pien_type = [yokopien, tatepien, squarepien, lpien]


@client.event
async def on_message(message):
    if "ぴえん" in message.content:
        if client.user != message.author:
            await message.channel.send(pien_type[random.randint(0, 3)])


client.run(token)
