import info
from helpers.database.access_db import db
from pyrogram import Client
from pyrogram.types import Message


async def AddUserToDatabase(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if info.LOG_CHANNEL is not None:
            await bot.send_message(
                int(info.LOG_CHANNEL),
                f"[{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) Started Using Our Bot🤩 \n\n#New_User @{(await bot.get_me()).username}"
            )
