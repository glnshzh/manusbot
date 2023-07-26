import time
from nonebot import on_keyword, Bot
from nonebot.adapters.onebot.v11 import Event, MessageEvent, bot, MessageSegment
from nonebot.internal.params import ArgPlainText
from nonebot.typing import T_State
from pyncm.apis.cloudsearch import GetSearchResult
from pyncm.apis.login import LoginViaCellphone
from pyncm.apis.track import GetTrackAudio
from pyncm.apis.login import LoginViaAnonymousAccount
from .musicConfig import music_config
print(music_config.music_account)
print(music_config.music_password)
LoginViaCellphone(music_config.music_account,music_config.music_password)
music=on_keyword(["music"])
option_text='''请选择想要的功能:
              1.网页快捷听歌(推荐)
              2.转换成音频发送
'''


@music.got("song_name",prompt="输入想要的歌曲米喵~")
async def got_song_name(state:T_State,song_name: str = ArgPlainText()):
    print(song_name)
    songs = GetSearchResult(song_name)['result']['songs']
    print(songs)
    for i in range(10):
        song = songs[i]
        state[str(i)]=song
        song_info = str(i) + ". " + "歌曲名：" + song['name']
        if len(song['alia']) > 0:
            song_info += ",介绍:" + song['alia'][0]
        await music.send(song_info)
        time.sleep(1)

@music.got("song_id",prompt="请输入想要的歌曲编号喵~")
async def get_music_id(state:T_State,song_id: str = ArgPlainText()):
    state["song_id"]=song_id


@music.got("option",prompt=option_text)
async def _(state:T_State,option:str=ArgPlainText()):
    print(option)
    print(state.get(state.get('song_id')))
    song = state.get(state.get('song_id'))
    # for key in song:
    #     print(key)
    pic=song['al']['picUrl']
    pic=MessageSegment.image(pic)
    await music.send(pic)
    if option=="3":
        download=GetTrackAudio(song['id'],bitrate=6400 * 2000)
        url=download['data'][0]['url']
        print(url)
        if url=='' or url==None:
            await music.send("歌曲收听,网易云没有上架该音乐")
        else:
            await music.send(url)
    if option=="2":
        print("")
    await music.finish()







