import discord
from discord import app_commands

guild = discord.Object(id=1362952956684668988)

class dependencias(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync(guild=guild)
        print('\n Comandos sincronizados\n')

client = dependencias()


# evento onready
@client.event
async def on_ready():
    print(f'\nLogged on as {client.user}')


# comandos direto no chat
@client.event
async def on_message(message): 
    if message.author == client.user:
        return
    if message.content == '.ping':
        await message.channel.send('pong')
        return


# comandos de barra daqui pra baixo
@client.tree.command(name="ping", description="Responde com pong!", guild=guild)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")
    return

@client.tree.command(name="abrido", description="Comando secreto dos enclavos", guild=guild)
async def abrido(interaction: discord.Interaction):
    await interaction.response.send_message("Idoso")
    return

@client.tree.command(name="teste", description="afbjkbjk", guild=guild)
async def teste(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention} teste')
    return
# Token do bot
client.run('token')
