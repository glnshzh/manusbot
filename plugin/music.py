from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Event, Bot, Message, MessageSegment






record=on_keyword(["record"])
@record.handle()
async def _(event:Event,bot:Bot):
    with open("F:\\vits\\getVist5.4\\getVist5.4\\object\\temp\\1689878552\\0.wav","rb") as f:
        music=f.read()
        music=MessageSegment.record(music)
        await bot.send(event=event,message=music)
    await record.finish()