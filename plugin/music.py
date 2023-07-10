from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Event, Bot, Message, MessageSegment






record=on_keyword(["record"])
@record.handle()
async def _(event:Event,bot:Bot):
    with open("F:/test/bott/music/群青-YOASOBI.flac","rb") as f:
        music=f.read()
        music=MessageSegment.record(music)
        await bot.send(event=event,message=music)
    await record.finish()