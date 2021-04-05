import requests
import time
import csv
import pandas as pd

# 通过微信公众平台素材管理 查询公众号历史文章
# 根据自己的cookie和token进行更改

# 目标url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# 使用Cookie，跳过登陆操作
headers = {
    "Cookie": "noticeLoginFlag=1; remember_acct=939571103@qq.com; appmsglist_action_3899606125=card; pgv_pvi=3658089472; RK=dAhgLO1zFn; ptcz=320bcb8913d9209a298c4d9755601f2ca537961f0e483181755d2561930f0551; pgv_pvid=1893749385; pac_uid=0_f6bdab6174356; ua_id=iGm30scGY5BGw01dAAAAAOIgUEv1oMHVMTX51uXBU8U=; wxuin=17542032848578; bizuin=3899606125; rand_info=CAESILCOJBx+BJOfl6U8VuNGYfpprtBQ8hUsV50UFVkafqTp; slave_bizuin=3899606125; data_bizuin=3899606125; data_ticket=dYGGNL8PUYZpy0lc/1h2DyGd9MGmNS2qZ094H/75ms2Aew9cKVfwivQCf7hn1tuQ; slave_sid=dlhfc05seHFVSWxPY3ZMOHhEellfSjd6MlhCYU90b1puRTRpTTRRaHpnVzBhREg5ZVNzRDNVWU5OMHlnb1VuanQzajZucmoxS1owUEVJeFRTNW93eGdjbEFpOE5RX2RkNXRNQ0NINko5WHFJTHpHckRZR3lMbkoya2lPMnhlRW9ZSERLUmlzRkxRYlBmaDBh; slave_user=gh_fd75692e1901; xid=ef322c58dc724ab02282b419a72770f4; openid2ticket_obURv6BZFggp6EkxAA9EgvbjtKrc=6uI1XlUj7wxSBZs1rG3i1HyKTe2wgp/k+iLSli8zpFM=; mm_lang=zh_CN",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
}

# fakeid是公众号id
data = {
    "token": "1950979280",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": "MjM5NzE2NTY0Ng==",
    "type": "9",
}

content_list = []
for i in range(20):
    data["begin"] = i * 5
    time.sleep(5)
    # 使用get方法进行提交
    content_json = requests.get(url, headers=headers, params=data).json()
    # 返回了一个json，里面是每一页的数据
    for item in content_json["app_msg_list"]:
        # 提取每页文章的标题及对应的url
        items = []
        items.append(item["title"])
        # items.append(item["digest"])  # 文章摘要
        items.append(item["link"])
        content_list.append(items)
    print(i)

name = ['title', 'link']
# name = ['title', 'digest', 'link']
test = pd.DataFrame(columns=name, data=content_list)
test.to_csv(".//csv//articles.csv", mode='a', encoding='utf-8')
print("保存成功")
