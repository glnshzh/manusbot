import nonebot
from pydantic import BaseModel,Extra

class musicConfig(BaseModel,extra=Extra.ignore):
    superusers: list = []

    ncm_admin_level: int = 1
    '''设置命令权限(1:仅限superusers和群主,2:在1的基础上管理员,3:所有用户)'''

    ncm_phone: str = ""
    '''手机号'''

    ncm_ctcode: str = "86"
    '''手机号区域码,默认86'''

    ncm_password: str = ""
    '''密码'''

    ncm_playlist_zip: bool = False
    '''上传歌单时是否压缩'''

    def __str__(self):
        """返回一个对象的描述信息"""
        return "%s,%s" % (self.ncm_admin_level, self.ncm_phone)


global_config=nonebot.get_driver().config
ncm_config=musicConfig(**global_config.dict())
print(ncm_config)