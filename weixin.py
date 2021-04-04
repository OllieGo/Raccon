import requests
from bs4 import BeautifulSoup


# 读取文件
def ReadFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        all_the_text = f.read()
    return all_the_text


# 保存文件函数
def SaveFile(filePath, fileContent):
    with open(filePath, 'w', encoding='utf-8') as f:
        f.write(fileContent)


# 修改网页中图片的src，使图片能正常显示
def ChangeImgSrc(htmlSource):
    bs = BeautifulSoup(htmlSource, "lxml")  # 由网页源代码生成BeautifulSoup对象
    imgList = bs.find_all("img")  # 找出网页中所有img标签
    for img in imgList:
        originalUrl = ""  # 定义一个变量保存图片真实url
        if "data-src" in img.attrs:  # 防止有的img标签中可能没有data-src而出错
            originalUrl = img.attrs["data-src"]
        elif "src" in img.attrs:  # 如果有src则提取出来
            originalUrl = img.attrs["src"]
        else:
            originalUrl = ""
        if originalUrl.startswith("//"):  # 如果url以//开始，则需要添加http
            originalUrl = "http:" + originalUrl
        img.attrs["src"] = originalUrl

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
    url = "https://mp.weixin.qq.com/s?__biz=MjM5MTIwNzg2OQ==&mid=208228982&idx=1&sn=44ca5cd06dfbd34b1d664673d2d025a2&scene=4#wechat_redirect"
    # url = "https://www.jianshu.com/p/36f5f74b6c04"
    htmlStr = DownloadHtml(url)
    htmlStr2 = ChangeImgSrc(htmlStr)
    savePath = "D:/Raccon/test2.html"
    SaveFile(savePath, htmlStr2)
