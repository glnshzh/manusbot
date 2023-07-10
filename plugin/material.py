from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment

m=on_keyword(["材料"])

#这里需要修改地址
@m.handle()
async def _(event:Event,bot:Bot):
    for i in range(1,5):
        with open("C:/Users/47818/Desktop/acg/ma/"+str(i)+".jpg","rb") as f:
            img=f.read()
            message=MessageSegment.image(img)
            await bot.send(event=event,message=message)
    await m.finish()