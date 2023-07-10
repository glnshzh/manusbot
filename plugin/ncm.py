from typing import Tuple, Any, Union
import nonebot
from .data_source import nncm, ncm_config, setting, Q, cmd

__plugin_meta__ = nonebot.plugin.PluginMetadata(
    name='网易云无损音乐下载',
    description='✨ 基于go-cqhttp与nonebot2的 网易云 无损音乐下载 ✨',
    usage=(
        '将网易云歌曲/歌单分享到群聊即可自动解析\n'
        '回复分享消息 + 文字`下载` 即可开始下载歌曲并上传到群文件(需要稍等一会)\n'
        '指令：\n'
        f'开启下载：{cmd}ncm t\n'
        f'关闭下载：{cmd}ncm f\n'
        f'点歌：{cmd}点歌 歌名'
    ),
    extra={'version': '1.5.0'}
)

from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent

TRUE = ["True", "T", "true", "t"]
FALSE = ["False", "F", "false", "f"]
ADMIN = ["owner", "admin", "member"]

# ===============Rule=============
async def song_is_open(event: Union[GroupMessageEvent, PrivateMessageEvent]) -> bool:
    if isinstance(event, GroupMessageEvent):
        info = setting.search(Q["group_id"] == event.group_id)
        if info:
            return info[0]["song"]
        else:
            setting.insert({"group_id": event.group_id, "song": False, "list": False})
            return False
    elif isinstance(event, PrivateMessageEvent):
        info = setting.search(Q["user_id"] == event.user_id)
        if info:
            return info[0]["song"]
        else:
            setting.insert({"user_id": event.user_id, "song": True, "list": True})
            return True


async def playlist_is_open(event: Union[GroupMessageEvent, PrivateMessageEvent]) -> bool:
    if isinstance(event, GroupMessageEvent):
        info = setting.search(Q["group_id"] == event.group_id)
        if info:
            return info[0]["list"]
        else:
            setting.insert({"group_id": event.group_id, "song": False, "list": False})
            return False
    elif isinstance(event, PrivateMessageEvent):
        info = setting.search(Q["user_id"] == event.user_id)
        if info:
            return info[0]["list"]
        else:
            setting.insert({"user_id": event.user_id, "song": True, "list": True})
            return True
async def check_search() -> bool:
    info = setting.search(Q["global"] == "search")
    if info:
        return info[0]["value"]
    else:
        setting.insert({"global": "search", "value": True})
        return True





