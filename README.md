1.下载python 版本 3.10.10（建议至少3.8以上）

2.安装ffmpeg 设置好bin的PATH(可以参考[go-cqhttp](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%AE%89%E8%A3%85-ffmpeg)中说明)

3.安装git 并下载本项目：

 git clone https://github.com/glnshzh/manusbot.git

4.建议安装pycharm进行管理

5.安装nonbot脚手架和适配器：

```bash
pip install nb-cli
pip install nonebot-adapter-onebot
```

6.安装JDK，常规配置路径版本建议版本在15以上,具体讨论参考：

https://github.com/Mrs4s/go-cqhttp/discussions/2245

注：若出现日志冲突，可以尝试：

```
git clean -d -fx

git pull
```



