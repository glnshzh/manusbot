import requests

#此函数可以处理url地址,返回json数据
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
