from telethon import TelegramClient, events
from better_automation.twitter import (
    Account as TwitterAccount,
    Client as TwitterClient,
    errors as twitter_errors,
)
from better_automation.utils import proxy_session
from aiohttp_socks import ProxyConnector
from dotenv import load_dotenv
from itertools import islice
from loguru import logger
from time import sleep
import threading
import aiohttp
import asyncio
import random
import os

load_dotenv()


def take(n, iterable):
    """Return the first n items of the iterable as a list."""
    return list(islice(iterable, n))


async def follow_back(auth_token, proxy):
    thread_name = threading.current_thread().name

    account = TwitterAccount(auth_token)

    async with proxy_session(proxy) as session:
        twitter = TwitterClient(account, session)

        try:
            followers = await twitter.request_followers(count=3)
            account_name = account.data.name

            logger.debug(
                f"ПОТОК | {thread_name} | Аккаунт: {account_name} \t\t Подписчиков: {account.data.followers_count}\n"
            )

            logger.warning(
                f"ПОТОК | {thread_name} | Пытаюсь подписаться на 10-15 подписчиков...\n"
            )

            for follower in followers[:random.randint(10, 15)]:
                try:
                    await twitter.follow(follower.id)
                    logger.success(
                        f"ПОТОК | {thread_name} | Успешно подписался на {follower.username}\n"
                    )
                except Exception:
                    logger.error(
                        f"ПОТОК | {thread_name} | Не удалось подписаться на {follower.username}\n"
                    )

                sleep(random.randint(5, 10))

        except twitter_errors.HTTPException as exc:
            logger.error(
                f"ПОТОК | {thread_name} | Не удалось выполнить запрос. Статус аккаунта: {account.status.value}\n"
            )
            raise exc


def follow_back_loop(tokens: list, proxies: list):
    logger.success(f"ФУНКЦИЯ 'ПОДПИСКИ НА ТВИТТЕРЫ' ЗАПУЩЕНА")
    while True:
        threads = []
        for token, proxy in zip(tokens, proxies):
            thread = threading.Thread(target=asyncio.run,
                                      args=(follow_back(token, proxy), ))
            threads.append(thread)
            sleep(5 +
                  random.random() * 5)  # Random delay between 5 and 10 seconds
            thread.start()

        for thread in threads:
            thread.join()

        tts = 25000

        print()
        logger.warning(f"СПЛЮ {(tts / 60) // 60} ЧАСОВ ПЕРЕД ПОДПИСКАМИ")
        sleep(tts)


async def send_twitter_list():
    thread_name = threading.current_thread().name
    logger.success(
        f"ПОТОК | {thread_name} | ПОТОК ОТПРАВКИ ТВИТТЕР СПИСКА ЗАПУЩЕН!")
    while True:
        logger.info(
            f"ПОТОК | {thread_name} | ОТПРАВЛЯЮ ССЫЛКУ НА ТВИТТЕР В ТЕЛЕГРАМ ЧАТЫ...\n"
        )

        msg_text = open(os.path.join("data", "msg.txt"), "r",
                        encoding="utf-8").read()

        client = TelegramClient("session_name", "20901287",
                                "a09716928f403e29f44bbbf68a1cc109")

        with open(os.path.join("data", "chats.txt"), "r",
                  encoding="utf-8") as file:
            chats_list = [chat.strip("\n") for chat in file.readlines()]

        async def main():
            for chat in chats_list:
                await client.send_message(chat, msg_text)

        async with client:
            client.loop.run_until_complete(main())

        tts = 3900
        logger.warning(
            f"ПОТОК | {thread_name} | СПЛЮ {(tts / 60) // 60} ЧАСОВ ПЕРЕД ОТПРАВКОЙ"
        )
        sleep(tts)


if __name__ == "__main__":
    try:
        tokens = [
            token.strip() for token in open(os.path.join("data", "tokens.txt"),
                                            "r").readlines()
        ]
        proxies = [
            proxy.strip() for proxy in open(
                os.path.join("data", "proxies.txt"), "r").readlines()
        ]
    except Exception:
        logger.error("ФАЙЛЫ tokens.txt И proxies.txt НЕ НАЙДЕНЫ!")

    if len(tokens) < 1:
        logger.error("НЕ УКАЗАНЫ ТОКЕНЫ!")
    elif len(proxies) < 1:
        logger.error("НЕ УКАЗАНЫ ПРОКСИ")

    send_twitter_lists = threading.Thread(target=asyncio.run,
                                          args=(send_twitter_list(), ))
    send_twitter_lists.start()

    follow_back_loop(tokens, proxies)
