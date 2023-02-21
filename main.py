from pyrogram import Client
from pyrogram.errors import FloodWait, BadRequest, Flood, InternalServerError
from time import sleep
from sys import stderr, exit
from loguru import logger
from os import system
import time

print('Telegram channel - https://t.me/n4z4v0d\n')


def clear(): return system('cls')



SESSION_NAME = "TweetFollowBot"
API_ID = 28795013
API_HASH = "a84701b19a169c790460acafb15655e2"

logger.remove()
logger.add(stderr,
           format='<white>{time:HH:mm:ss}</white> | '
                  '<level>{level: <8}</level> | '
                  '<cyan>{line}</cyan> - '
                  '<white>{message}</white>')

app = Client(SESSION_NAME, API_ID, API_HASH)

with open('otc.txt', 'r', encoding='utf-8') as file:
    otc_list = [row.strip() for row in file]

msg_text = open('msg_text.txt', 'r', encoding='utf-8').read()


def send_message_otc(current_otc):
    for _ in range(3):
        try:
            with app:
                app.send_message(current_otc, msg_text)

        except FloodWait as error:
            logger.info(f'{current_otc} | FloodWait: {error.x}')
            sleep(error.x)

        except Flood:
            pass

        except BadRequest as error:
            logger.error(f'{current_otc} | {error}')

        except InternalServerError as error:
            logger.error(f'{current_otc} | {error}')

        except Exception as error:
            logger.error(f'{current_otc} | {error}')

        else:
            logger.success(f'{current_otc} | The message was successfully sent')
            return

    with open('errors_send_message.txt', 'a', encoding='utf-8') as file:
        file.write(f'{current_otc}\n')


def join_chat_otc(current_otc):
    for _ in range(3):
        try:
            with app:
                app.join_chat(current_otc)

        except FloodWait as error:
            logger.info(f'{current_otc} | FloodWait: {error.x}')
            sleep(error.x)

        except Flood:
            pass

        except BadRequest as error:
            logger.error(f'{current_otc} | {error}')

        except InternalServerError as error:
            logger.error(f'{current_otc} | {error}')

        except Exception as error:
            logger.error(f'{current_otc} | {error}')

        else:
            logger.success(f'{current_otc} | Successfully logged into the chat')
            return

    with open('errors_join_chat.txt', 'a', encoding='utf-8') as file:
        file.write(f'{current_otc}\n')


if __name__ == '__main__':

    clear()
    while True:
        for current_otc in otc_list:

            send_message_otc(current_otc)

            logger.success('Работа успешно завершена!')

    print('\nPress Any Key To Exit..')
    exit()
