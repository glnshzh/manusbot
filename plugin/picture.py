import json

import requests


def getPicUrl(url):
    with open(r"F:\test\bott\PIC_S\0.json",encoding='utf-8') as f:
        data=json.loads(f.readline())
        # for key in data:
        #     print(key)
        # print(data['graph'][3])
        # for key in data['graph'][3]:
        #     print (key)
        print(data['graph'][3]['parameters']['paras'][0]['exampleValues'])
        imgs=data['graph'][3]['parameters']['paras'][0]['exampleValues']
        for i in range(len(imgs)):
            print(imgs[i]['value'])
            response = requests.get(imgs[i]['value'])

            save_path = "F:\\test\\bott\PIC_D\\"+str(i)+".jpg"
            with open(save_path,"wb") as k:
                k.write(response.content)
                k.close()
        print("下载成功")
        f.close()


if __name__=="__main__":
    url=r"F:\test\bott\PIC_S\0.json"
    getPicUrl(url)