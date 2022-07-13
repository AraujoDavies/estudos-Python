# mandando primeira msg
from asyncio import run
from pyrogram import Client

app = Client(
    'tesoubot_app'
)

# função assíncrona
async def main(): 
    await app.start() # inicia conexao com a api do telegram
    await app.send_message('Davies9', 'oi bb denovo') # nome do usuario, msg
    await app.stop() # para conexao com a api do telegram

run(main()) # executa!