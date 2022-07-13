# Usando o Tecladinho...
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

app = Client(
    'tesoubot_app'
)

@app.on_message(filters.command('teclado'))
async def teclado(client, message):
    teclado = ReplyKeyboardMarkup( #define as teclas
        [
            ['/ajuda', '/xpto'],
            ['a', 'b', 'c']
        ],
        resize_keyboard=True # ajusta o teclado a tela
    )
    await message.reply(
        'Aperta aí no teclado',
        reply_markup=teclado,
    )

@app.on_message(filters.command('a'))
async def resposta_teclado(client, message):
    await message.reply("I'm rilled up")
    
app.run() # executa