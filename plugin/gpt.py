from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot import on_message
from nonebot import rule
import os
import openai
def _checker(event: GroupMessageEvent) ->bool:
    return event.message_type=="group"
# word=on_message(rule=rule.to_me())
#
# def getChat():
#     openai.api_key = "ssk-f2KkLJ1DF9dR2PUWoMknNU7KHOL2VW9EY6vQ6SYdHBa93pKk"
#     openai.api_base = "https://api.f2gpt.com/v1"
#     chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "测试"}])
#     return chat_completion
#
#
# @word.handle()
# async def gptBack(event:GroupMessageEvent):
#     print(event.message_type)
#     msg=event.message
#     await word.send(msg)
#     print(event.user_id)
#     await word.finish(str(event.user_id))