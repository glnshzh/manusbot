import nonebot
from pydantic import BaseModel, Extra


class weatherConfig(BaseModel,extra=Extra.ignore):
    city:str
    internal_time:str



global_config=nonebot.get_driver().config
weather_config=weatherConfig(**global_config.dict())