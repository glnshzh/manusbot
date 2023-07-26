import json
from nonebot import on_keyword, Bot
from nonebot.adapters.onebot.v11 import Event, Message, MessageEvent
from nonebot.params import CommandArg
import requests
from nonebot.plugin.on import on_command

WEEKENUM={'1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'日'}
def getData(url:str,parms:list):
    url+="?"
    if len(parms)==0:
        return False
    if len(parms)==1:
        url+=parms[0]
        print("url="+url)
        return requests.get(url)
    else:
        url += parms[0]
        for i in range(1, len(parms)):
            url +="&"+parms[i]
        print("url=" + url)
        return requests.get(url)


word=on_command("现在天气")
@word.handle()
async def _(bot:Bot,event: Event,ags:Message=CommandArg()):
    parms = ["key=bc082dbe33794190c7e113164a358604"]
    parms.append("keywords="+str(ags))
    data=getWeather(getCityCode(parms))
    if data==[] or data==None:
        await bot.send(event=event,message=f"维尔汀：'My though still cling to the moldering past,But the hopes of youth fall thick in the blast!'")
        await bot.send(event=event,message="您输入的城市在暴雨中消逝，请重新输入正确的城市")
    else:
        print(data)
        await bot.send(event=event,message=f"维尔汀：'My though still cling to the moldering past,But the hopes of youth fall thick in the blast!'")
        for i in range(0,len(data)):
            d=data[i]
            day="日期"+d['date']+",星期"+WEEKENUM[d['week']]+",白天情况：天气"+d['dayweather']+",温度为"+d['daytemp']+"风力"+d['daypower']+",平均温度"+d['daytemp_float']
            night="夜晚情况：天气"+d['nightweather']+",温度为"+d['nighttemp']+"风力"+d['nightpower']+",平均温度"+d['nighttemp_float']
            await bot.send(event=event, message=day+"/n"+night)
    await word.finish()
def getCityCode(parms):
    url="https://restapi.amap.com/v3/config/district"
    data=getData(url,parms)
    data=json.loads(data.text)
    data=data['districts']
    if len(data)>0:
        cityCode=data[0]["adcode"]
        print(cityCode)
        return cityCode
    else:
        return None
def getWeather(cityCode):
    if cityCode==None:
        return None
    parms=[]
    parms.append("city="+cityCode)
    parms.append("key=bc082dbe33794190c7e113164a358604")
    parms.append("extensions=all")
    url="https://restapi.amap.com/v3/weather/weatherInfo"
    data=getData(url,parms).text
    data=json.loads(data)['forecasts'][0]['casts']
    return data

if __name__=='__main__':
    parms=["key=bc082dbe33794190c7e113164a358604","keywords=海门"]
    getWeather(getCityCode(parms))
