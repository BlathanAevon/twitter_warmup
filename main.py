import os
import asyncio
from telethon import TelegramClient, events

api_id = '28009996'
api_hash = '24b5b5f2594e8a5f7e0066203c1550dd'

msg_text = open('msg_text.txt', 'r', encoding='utf-8').read()

client = TelegramClient('session_name', api_id, api_hash)

with open('chats.txt', 'r', encoding='utf-8') as file:
    chats_list = [chat.strip("\n") for chat in file.readlines()]

async def send_message(chat_name):
    await client.send_message(chat_name, msg_text)

    
async def main():
    for chat in chats_list:
        await send_message(chat)
        

with client:
    client.loop.run_until_complete(main())
