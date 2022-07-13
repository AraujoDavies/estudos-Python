# Além do app.on_message existem outros decoradores...
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

app = Client(
    'tesoubot_app'
)
# 
"""
on_edited_message   = auto explicativo
on_deleted_message  = auto explicativo
on_callback_query   = quando for preciso dar continuidade no comando
"""

@app.on_callback_query()
async def callback(client, callback_query):
    pages = {
        'data': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_2'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='data'),
            'texto': 'Você está na página 1'
        },
        'page_3': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='data'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='page_2'),
            'texto': 'Você está na página 3'
        },
        'page_2': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_3'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='data'),
            'texto': 'Você está na página 2'
        }
    }
    page = pages[callback_query.data]
    await callback_query.edit_message_text(
        page['texto'],
        reply_markup=InlineKeyboardMarkup([[page['anterior'], page['proximo']]])
    )


@app.on_message(filters.command('inline'))
async def teclado(client, message):
    botoes = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Callback', callback_data='data'),
                InlineKeyboardButton(
                    'Link',
                    url='https://docs.pyrogram.org/api/methods/#messages'
                )
            ]
        ]
    )
    await message.reply(
        'Aperta aí no teclado',
        reply_markup=botoes
    )
    
app.run() # executa
