import discord

client = discord.Client()

@client.event
async def on_ready():
    print('ボットがログインしました')

client.run('ボットのトークン')
