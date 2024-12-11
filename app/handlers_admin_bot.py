from aiogram import F, Router
from aiogram.types import Message, ReactionTypeEmoji
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

import configparser
import os

from config.parser_config_admin import (get_status_bot, set_active_bot,
                                        set_inactive_bot, get_owner_user_id,
                                        set_len, set_size)
from sqlite import db_start, get_all_users, db_close

router = Router()


def check_user(user_id_message: int) -> bool:
    """
    Функция для проверки доступа к управлению ботом и его настройками
    :param user_id_message: int user_id пользователя, который пишет боту
    :return: true - дается доступ к функциям бота, false - запрет
    """
    user_id_owner = get_owner_user_id()
    return user_id_message == user_id_owner


@router.message(Command("cmd"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        str_f_cmd = (f"Список команд для администрирования бота:\n\n"
                     f"/act - активация бота;\n"
                     f"/dis - деактивация бота;\n"
                     f"/getstatus - получить текущий статус бота;\n"
                     f"/getconfig - получить текущий файл конфигурации;\n"
                     f"/getfiledbsize - получить размер файла базы данных;\n"
                     f"/getusers - получить список пользователей, воспользовавшихся ботом;\n"
                     f"len X - установить новую максимальную длину пароля (Х - число);\n"
                     f"size X - установить максимальное число генерируемых паролей за раз (Х - число);")
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])
        await message.reply(text=str_f_cmd, parse_mode=ParseMode.MARKDOWN)


@router.message(Command("act"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_active_bot()
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])
        await message.reply(text="Бот включен")


@router.message(Command("dis"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_inactive_bot()
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])
        await message.reply(text="Бот отключен")


@router.message(Command("getstatus"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        current_status = int(get_status_bot())
        if current_status == 0:
            await message.reply(text="Бот отключен")
            emoji_got_it = ReactionTypeEmoji(emoji='😴')
            await message.react(reaction=[emoji_got_it])
        elif current_status == 1:
            await message.reply(text="Бот работает")
            emoji_got_it = ReactionTypeEmoji(emoji='👨‍💻')
            await message.react(reaction=[emoji_got_it])


@router.message(Command("getconfig"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        conf = configparser.ConfigParser()
        conf.read('config/config.ini')
        str_f = (f"[ACTIVE_BOT]:\n"
                 f"is_active_bot: {conf['ACTIVE_BOT']['is_active_bot']}\n\n"
                 f"[PARAMETERS_MAX]:\n"
                 f"len: {conf['PARAMETERS_MAX']['len']}\n"
                 f"size: {conf['PARAMETERS_MAX']['size']}")
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])
        await message.reply(text=str_f)


@router.message(Command("getfiledbsize"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        file_size_byte = os.path.getsize("users.db")
        file_size_kbyte = file_size_byte / 1024
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])
        await message.reply(f"Размер файла базы данных: {file_size_kbyte} КБ")


@router.message(Command("getusers"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        await db_start()
        users = await get_all_users()
        await db_close()
        for user in users:
            str_user = (f"Telegram id: {user[0]}\n"
                        f"Name: {user[1]}\n"
                        f"URL: {user[2]}")
            await message.reply(text=str_user)
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])


@router.message(F.text.startswith("len"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        lent = message.text.replace("len", "").strip()
        set_len(lent)
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])
        await message.reply(text=f"Максимальная длина одного пароля изменена на {lent}")


@router.message(F.text.startswith("size"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        size = message.text.replace("size", "").strip()
        set_size(size)
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])
        await message.reply(text=f"Максимальное количество генерируемых сообщений за раз изменено на {size}")
