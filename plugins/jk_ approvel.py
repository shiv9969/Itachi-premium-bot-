# import os
# import re
# import ast
# import asyncio
# from pyrogram import Client, filters
# from pyrogram.types import Message, User, ChatJoinRequest
# from info import CHAT_ID, WEL_TEXT, WEL_MSG

# @Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
# async def autoapprove(client, message: ChatJoinRequest):
#     chat=message.chat 
#     user=message.from_user 
#     print(f"{user.first_name} Joined (Approved)") 
#     await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
#     if WEL_MSG == "on":
#         await client.send_message(chat_id=chat.id, text=WEL_TEXT.format(mention=user.mention, title=chat.title))
