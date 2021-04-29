import requests
import time
import pandas as pd


# 通过微信公众平台素材管理 查询公众号历史文章
# 根据自己的cookie和token进行更改
class SearchArticles():

    def Search(self, cookie, token, fakeid, gzhname):
        # 目标url
        url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

        # 使用Cookie，跳过登录操作
        headers = {
            # "Cookie": "noticeLoginFlag=1; remember_acct=939571103@qq.com; appmsglist_action_3899606125=card; pgv_pvi=3658089472; RK=dAhgLO1zFn; ptcz=320bcb8913d9209a298c4d9755601f2ca537961f0e483181755d2561930f0551; pgv_pvid=1893749385; pac_uid=0_f6bdab6174356; ua_id=iGm30scGY5BGw01dAAAAAOIgUEv1oMHVMTX51uXBU8U=; wxuin=17542032848578; mm_lang=zh_CN; uuid=dc9de218a70caba323c66f6c73f64049; bizuin=3899606125; ticket=d4057fa40008ba0a4a6b06fdb1305ee8581b9d44; ticket_id=gh_fd75692e1901; cert=5IR7o9Jfyae8Vv4aZNEyP_ZMoA_M4bKe; rand_info=CAESIOIEo8jxeYjZgn5o2tJmJaZrCfX6tEo9ekwX3ns1X6Sa; slave_bizuin=3899606125; data_bizuin=3899606125; data_ticket=B3y1+wleyMv5XZ3btC/bTo7dl742x/EW4yBaI+Z0TlFjBNQdiVs7Fqh84kp063Ar; slave_sid=RVFNUE9fZFhNM25DSDZ3a1RveGxuRW9DUEtQMnhjYkFBS2hfTlpmVzd3VUJEMUhmMngxQjBJYjBOSGlDbktQaW9IRHdQeGFZVkRDODZmeU85SWRVdXFNR0dVRXl1ejdBVm51c2lmU3pIa1dMTzM1MFVzNDBVOHhtQ2R6T2I2MkF6eEJ1M0trVGdGVllVaUVY; slave_user=gh_fd75692e1901; xid=b93d1ea0d99d857e243c4e3c8e68d164; openid2ticket_obURv6BZFggp6EkxAA9EgvbjtKrc=pMBbA/39HQzR9igG41qgJbWSCMTZR+WvHqCxuXZEeQA=",
            "Cookie": cookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        }

        # fakeid是公众号id
        data = {
            # "token": "921232635",
            "token": token,
            "lang": "zh_CN",
            "f": "json",
            "ajax": "1",
            "action": "list_ex",
            "begin": "0",
            "count": "5",
            "query": "",
            # "fakeid": "MzU0Mjc2OTkzNQ==",
            "fakeid": fakeid,
            "type": "9",
        }

        content_list = []
        for i in range(50):
            data["begin"] = i * 5
            time.sleep(3)
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
        saveCsvPath = "./csv/" + f'{gzhname}' + ".csv"
        test.to_csv(saveCsvPath, mode='a', encoding='utf-8')
        print("保存成功")
