import nonebot
from pydantic import BaseModel,Extra

class musicConfig(BaseModel,extra=Extra.ignore):
    music_account:str
    music_password:str



global_config=nonebot.get_driver().config
music_config=musicConfig(**global_config.dict())