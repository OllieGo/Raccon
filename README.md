# Raccon(浣熊)
下载公众号历史文章

## 教程

登录微信公众号后台

在新建图文素材界面添加超链接

选择其他公众号链接内容，通过Chrome DevTools获取目标公众号ID(fakeid)和自己的cookie和token

替换main.py中四个参数（fakeid、token、cookie、subscriptionName）并执行

    token
    cookie
    fakeid 公众号id
    SubscriptionName 公众号名称

生成的csv/subscriptionName.csv文件包含文章标题和地址


在DownloadArticles.py修改待下载csv文件路径

    filename = 'D:\\WxArticles\\灼识新维度.csv' 

执行DownloadArticles.py下载文章，生成路径可自行修改

