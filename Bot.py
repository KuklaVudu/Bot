import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")


MSG = "Водичку попей {}!"


bot = Bot("6098377894:AAHuvbAjVLDWIpLhA1vJ8aW2Dj5Tm3Vx700")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!")

    for i in range(1):
        await asyncio.sleep(60*60*24)
        await bot.send_message(user_id, MSG.format(user_name))

if __name__ == "__main__":
    executor.start_polling(dp)