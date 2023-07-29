import nonebot
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Event
from nonebot import on_message, on_command, on_keyword
from nonebot import rule
import os
import openai
from nonebot.params import CommandArg, EventPlainText
from nonebot.permission import Message
from nonebot.rule import to_me
from pydantic import Extra, BaseModel


class gptConfig(BaseModel,extra=Extra.ignore):
    openai_api_key:str

global_config=nonebot.get_driver().config
gpt_config=gptConfig(**global_config.dict())


def getChat(message:str,role="user"):
    openai.api_key = gpt_config.openai_api_key
    openai.api_base = "https://openaiapicn.top/v1"
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                   messages=[{"role": role, "content": message}]
                                                   )
    text=chat_completion
    print(text["choices"][0]["message"]['content'])
    return text["choices"][0]["message"]['content']

def _checker(event: GroupMessageEvent) ->bool:
    return event.message_type=="group" and rule.to_me()


word=on_keyword(keywords={"gpt"},rule=rule.to_me())

@word.handle()
async def gptBack(event: Event,ags=EventPlainText()):
    print(str(ags))
    ask=str(ags)
    ask=ask.split(" ")
    print(ask[1])
    gpt_ask=ask[1]
    try:
        await word.send("请稍等几分钟,等待gpt生成")
        await word.send(getChat(gpt_ask))
    except Exception as e:
        print(e)
        await word.send("发送失败，请重新尝试")