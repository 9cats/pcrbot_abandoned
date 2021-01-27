from hoshino import Service

sv_help_query = '''
[日程(今日/明日/x月x日)(可自动)] 查看活动日程
[日程表] 查看一周日程
[设置温度/设置环境温度 <温度>] 设置温度或环境温度
[挖矿计算 +当前名次] 计算剩余可获得的奖励钻石
'''.strip()

sv = Service('yobot_query', help_=sv_help_query, bundle='pcr查询')

sv_help_entertainment = '''
[人偶] (权:主人)人偶功能
'''.strip()

sv = Service('yobot_entertainment',help_=sv_help_entertainment, bundle='pcr娱乐')