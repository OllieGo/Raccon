from SearchArticles import SearchArticles

sa = SearchArticles()

cookie = "noticeLoginFlag=1; remember_acct=939571103@qq.com; appmsglist_action_3899606125=card; pgv_pvi=3658089472; RK=dAhgLO1zFn; ptcz=320bcb8913d9209a298c4d9755601f2ca537961f0e483181755d2561930f0551; pgv_pvid=1893749385; pac_uid=0_f6bdab6174356; ua_id=iGm30scGY5BGw01dAAAAAOIgUEv1oMHVMTX51uXBU8U=; wxuin=17542032848578; mm_lang=zh_CN; bizuin=3899606125; noticeLoginFlag=1; remember_acct=939571103@qq.com; rand_info=CAESID/VFuExB9FpR4vLJPb0I0hVYKc9wbB0yCyXZ5RfrOfw; slave_bizuin=3899606125; data_bizuin=3899606125; data_ticket=H3VfTdKW2kFiosn0VSsk4ovvG9eRXroxkD0/4DB/nIShnVfUMx+H7HWUwZW74FSe; slave_sid=ZWNUZ3NDUF9xMGF6ZDFkVmZTNnVncGFGcDBncWZTWld0dG1HaHNfUjFKa29lVzlrNDF6U3Q4a0RGZHJpQXo5R1lGX1E1Y1dsYjRTd1MyMWZLaU9yMEZlaFhqYnNRWkRRVmU0VDdQYk53XzFsUmVaZ2czaVNWY0FWeEJWZU9KcVJ4YUc3SnM4cFJGZHJ3WUZ3; slave_user=gh_fd75692e1901; xid=9876540b284ba5a0c7efc4efc2d131de; openid2ticket_obURv6BZFggp6EkxAA9EgvbjtKrc=fC16vfAqLKee3Aung6TSXBl3AqRwiY3BlClMUuA55ao="
token = "449184339"
fakeid = "MzU0Mjc2OTkzNQ=="  # 公众号fakeid
subscriptionName = "灼识新维度"  # 公众号名称

sa.Search(cookie, token, fakeid, subscriptionName)
