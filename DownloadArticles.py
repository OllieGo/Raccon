import os
import requests
from bs4 import BeautifulSoup
import pandas as pd


# 通过url下载公众号文章

# 读取文件
def ReadFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        all_the_text = f.read()
    return all_the_text


# 保存文件函数
def SaveFile(filePath, fileContent):
    with open(filePath, 'w', encoding='utf-8') as f:
        f.write(fileContent)


# 将图片从远程下载到本地
def DownloadImg(url, savePath):
    r = requests.get(url)
    with open(savePath, 'wb') as f:
        f.write(r.content)


# 修改网页中图片的src，使图片能正常显示
def ChangeImgSrc(htmlSource):
    bs = BeautifulSoup(htmlSource, "lxml")  # 由网页源代码生成BeautifulSoup对象
    imgList = bs.find_all("img")  # 找出网页中所有img标签
    imgIndex = 0  # 图片编号，不同图片要保存为不同名称
    for img in imgList:
        imgIndex += 1
        originalUrl = ""  # 定义一个变量保存图片真实url
        if "data-src" in img.attrs:  # 防止有的img标签中可能没有data-src而出错
            originalUrl = img.attrs["data-src"]
        elif "src" in img.attrs:  # 如果有src则提取出来
            originalUrl = img.attrs["src"]
        else:
            originalUrl = ""
        if originalUrl.startswith("//"):  # 如果url以//开始，则需要添加http
            originalUrl = "http:" + originalUrl

        if len(originalUrl) > 0:  # 有图片网址则下载该图片
            print(originalUrl)
            if "data-type" in img.attrs:
                imgType = img.attrs["data-type"]  # 文件扩展名
            else:
                imgType = "png"  # 没有扩展名则默认png
            imgName = str(imgIndex) + "." + imgType
            imgSavePath = "D:/Raccon/images/" + imgName  # 图片保存目录
            DownloadImg(originalUrl, imgSavePath)  # 下载图片
            img.attrs["src"] = "images/" + imgName  # 网页中图片的相对路径
        else:
            img.attrs["src"] = ""

    return str(bs)  # 将BeautifulSoup对象转为字符串，用于保存


# 下载url网页并保存
def DownloadHtml(url):
    # 构造请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }

    # 模拟浏览器发送请求
    response = requests.get(url, headers=headers)
    if response.status_code == 200:  # 返回码为200表示正常返回
        htmltext = response.text  # 网页正文
        print(htmltext)
        return htmltext
    else:
        return None


if __name__ == '__main__':

    # 判断文件夹是否存在，不存在则创建
    dirs1 = 'D:\\Raccon\\images'
    if not os.path.exists(dirs1):
        os.makedirs(dirs1)

    filename = './/csv//articles.csv'
    num = 0;

    with open(filename, 'r', encoding='utf-8') as f:
        num = len(f.readlines()) - 1
        print(num)

    # 读取articles.csv
    df = pd.read_csv(filename)

    # 下载每篇文章
    for i in range(num):
        print("开始下载第" + str(i) + "篇文章")
        print(df["title"][i])
        # print(df["link"][i])

        title = df["title"][i]
        url = df["link"][i]
        htmlStr = DownloadHtml(url)
        htmlStr2 = ChangeImgSrc(htmlStr)
        savePath = "D:/Raccon/" + title + ".html"
        SaveFile(savePath, htmlStr2)

