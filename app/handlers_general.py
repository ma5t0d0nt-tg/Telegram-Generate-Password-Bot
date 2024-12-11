from aiogram import F, Router
from aiogram.types import Message, ReactionTypeEmoji
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

import re
import random

from config.parser_config_admin import (get_status_bot, get_max_len, get_max_size)
from db.sqlite import db_start, add_user, db_close

router = Router()


@router.message(Command("start"))
async def handler(message: Message):
    await db_start()
    await add_user(user_id=message.from_user.id, name=message.from_user.full_name,
                   url="https://t.me/" + message.from_user.username if message.from_user.username != "" else "")
    await db_close()
    status = get_status_bot()
    if status == "1":
        await message.reply(text=f"Здравствуйте, {message.from_user.first_name}.\n"
                                 f"Я бот, предназаченный для создания безопасных паролей в Telegram Messenger для "
                                 f"регистрации на сайтах. Сгенерированные пароли никуда не сохраняются.")


@router.message(Command("author"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        emoji_got_it = ReactionTypeEmoji(emoji='👨‍💻')
        await message.react(reaction=[emoji_got_it])
        await message.reply(text=f"Ссылка на автора данного бота\nhttps://t.me/m/-kwpIKrTMzIy")


@router.message(Command("pic"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        await message.reply(
            text=f"Ссылка на аватар бота:\nhttps://in.pinterest.com/pin/805862927053104693/")


@router.message(Command("description"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        await message.reply(text="Этот бот работает как генератор сложных паролей.\n"
                                 "Для получения примеров, используйте команду /example_gen_pass")


@router.message(Command("example_gen_pass"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        example_tmp = (f"💠Примеры **правильных** шаблонов:\n"
                       f"👉`pass l8 AZ az 09 !@ n10` - сгенерирует пароль длиной 8 символов из "
                       f"заглавных, прописных, цифр и спец. символов. "
                       f"Таких паролей будет сгенерировано - 10 штук.\n"
                       f"👉`pass l5 AZ az -09 -!@ n15` - сгенерирует пароль длиной 5 символов из "
                       f"заглавных и прописных."
                       f"Таких паролей будет сгенерировано - 15 штук.\n\n"
                       f"💠Примеры **неправильных** шаблонов:\n"
                       f"👉`pass l8 -AZ -az -09 -!@ n10` - при задании такого шаблона, бот выдаст ошибку, потому что все "
                       f"параметры исключены из генерации пароля.\n"
                       f"👉`pass lr -uZ -a7 -9 - n10=` - такой шаблон не правильный:\n"
                       f"вместо длины, стоит буква;\n"
                       f"если нужно указать, чтобы присутствовали или отсутствовали заглавные символы, нужно указывать 'AZ' или '-AZ';\n"
                       f"с прописными символами аналогично заглавным;\n"
                       f"если нужно указать, что нужны или не нужны цифры в генерации, то шаблон должен содержать '09' или '-09', для параметра должны присутствовать обе цифры;\n"
                       f"вместо параметра не может стоять прочерк;\n"
                       f"Неправильные шаблоны не выдадут результат.\n\n"
                       f"‼️‼️***ПРИМЕЧАНИЕ***‼️‼️\n"
                       f"Созданный пароль можно скопировать нажатием на любой пароль. Он добавится в буфер обмена.\n"
                       f"Символ '-' перед параметром в шаблоне, означает, что он не будет включен в генерацию пароля.\n")
        await message.reply(text=example_tmp, parse_mode=ParseMode.MARKDOWN)


@router.message(F.text.startswith("pass"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        text = re.sub(r'\s+', ' ', message.text.replace("pass", "").strip())
        arr_parameters = text.split(" ")

        if len(arr_parameters) == 6:

            ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
            digits = "0123456789"
            punctuation = "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~"

            size_pass = arr_parameters[0]
            uppercase = arr_parameters[1]
            lowercase = arr_parameters[2]
            digit = arr_parameters[3]
            special_characters = arr_parameters[4]
            count = arr_parameters[5]

            str_description_template = "Шаблон был составлен из: "
            arr_description_template = []

            if size_pass.startswith("l"):
                size_pass = size_pass.replace("l", "")
                if size_pass.isdigit():
                    size_pass = int(size_pass)
                    max_len = get_max_len()
                    if size_pass < 1:
                        size_pass = 1
                    if size_pass > max_len:
                        size_pass = max_len

            if uppercase == "AZ":
                uppercase = True
                arr_description_template.append("заглавных букв")
            elif uppercase == "-AZ":
                uppercase = False
            else:
                uppercase = False

            if lowercase == "az":
                lowercase = True
                arr_description_template.append("прописных букв")
            elif lowercase == "-az":
                lowercase = False
            else:
                lowercase = False

            if digit == "09":
                digit = True
                arr_description_template.append("цифр")
            elif digit == "-09":
                digit = False
            else:
                digit = False

            if special_characters == "!@":
                special_characters = True
                arr_description_template.append("специальных символов")
            elif special_characters == "-!@":
                special_characters = False
            else:
                special_characters = False

            if count.startswith("n"):
                count = count.replace("n", "")
                if count.isdigit():
                    count = int(count)
                    max_size = get_max_size()
                    if count > max_size:
                        count = max_size
                    if count < 1:
                        count = 1

            if ((uppercase + lowercase + digit + special_characters > 0) and
                    isinstance(size_pass, int) and isinstance(count, int)):

                str_tmp = ((ascii_uppercase if uppercase else "") + (ascii_lowercase if lowercase else "") +
                           (digits if digit else "") + (punctuation if special_characters else ""))

                arr_gen_pass = []

                for c in range(count):
                    ps = ""
                    for s in range(size_pass):
                        ps += random.choice(str_tmp)
                    arr_gen_pass.append(str(c + 1) + ": `" + ps + "`")

                await message.reply(text=f"Набор паролей по шаблону\n`{text}` 👇", parse_mode=ParseMode.MARKDOWN)
                await message.reply(text=str_description_template + ", ".join(arr_description_template) + "\n\n" +
                                         f"Длина паролей: {size_pass}.\nКоличество паролей: {count}")
                await message.reply(text="\n\n".join(arr_gen_pass), parse_mode=ParseMode.MARKDOWN)
                emoji_got_it = ReactionTypeEmoji(emoji='👍')
                await message.react(reaction=[emoji_got_it])

            else:
                await message.reply("В шаблоне допущена ошибка.\n"
                                    "Смотрите примеры создания паролей командой /example_gen_pass")
                emoji_got_it = ReactionTypeEmoji(emoji='👎')
                await message.react(reaction=[emoji_got_it])

        else:
            await message.reply("В шаблоне допущена ошибка.\n"
                                "Смотрите примеры создания паролей командой /example_gen_pass")
            emoji_got_it = ReactionTypeEmoji(emoji='👎')
            await message.react(reaction=[emoji_got_it])
