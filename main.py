import discord

'''
class MyClient(discord.Client):
    async def on_ready(self):
        print('\nLogged on as', self.user)

    async def on_message(self, message):
        # Confere se a mensagem é de si mesmo
        if message.author == self.user:
            return
        #ping pong básico
        if message.content == 'ping':
            await message.channel.send('pong')
            return
'''

intents = discord.Intents.default()
intents.message_content = True # para ler o chat
# futuramente aprender a usar comando de barra
client = MyClient(intents=intents)

# Token do bot
client.run('token')
