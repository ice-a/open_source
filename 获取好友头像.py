# coding: utf-8
# Author：lidashan
# Date ：2019/10/18 19:33
# Tool ：PyCharm
# Used ：用于生成一张好友图片
import os
os.system("pip install pillow")
os.system("pip install wxpy")
import math
import time
from PIL import Image
import itchat

# 先登录
itchat.auto_login(hotReload=True)
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]
num = 0

for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open('D:' + "\\1" + "\\" + str(i["UserName"]) + ".jpg", 'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1
    time.sleep(2)  # 添加等待延迟，避免被封
    print(i["UserName"])


def joint_avatar(path):
    all_image = os.listdir(path)
    each_size = int(math.sqrt(float(800 * 800) / len(all_image)))
    lines = int(800 / each_size)
    print(lines)
    image = Image.new("RGBA", (800, 800))
    x = 0
    y = 0
    for i in range(0, len(all_image)):
        temp = r"D:\1" + "\\" + all_image[i]
        img = Image.open(temp)
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
    image.save("all_pin.png")


path = r"D:\1"
joint_avatar(path)
