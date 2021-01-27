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


sv_help_clan = '''
[手册]	查看公会战使用手册
[面板]	进入公会战面板
[创建日服公会]	日/韩/台/国，创建后可在后台修改
[加入公会 (@某人)]	加入到公会名单，如果有at则为加入他人
[加入全部成员]	
[报刀2000000 (@某人) (昨日) (：留言)]	对boss造成伤害但未击败时用，记录伤害，可以使用 200w/200万/2000k 等（一般公会精确到万即可）
如果有at则为代报，有冒号则为留言
如果有“昨日”则将记录添加到前一天1
[尾刀 (@某人) (昨日) (：留言)]	对boss造成伤害并击败时用，记录伤害
如果有at则为代报，有冒号则为留言
如果有“昨日”则将记录添加到前一天1
[SL (@某人) (？)]	挑战boss强制取消后用，记录本日SL2，用“？”查询今日是否已 SL，如果有at则为代报/代查
[撤销]	撤销上一次报刀（非管理员只能撤销自己的记录）
[状态]	显示boss状态
[预约1 (：留言)]	预约boss，当boss出现时通知，有冒号则为留言
[挂树 (：留言)]	挂树，当boss被击败时通知
[查1 / 查树]	查询预约boss的成员，查询挂树的成员
[取消预约1 / 取消1]	取消预约
[申请出刀]	锁定boss，提醒后面申请出刀的人有人正在挑战boss
[锁定:留言]	锁定boss，提醒后面申请出刀的人，冒号后为留言
[解锁]	解锁boss，其他人可以继续申请3
更多详情可点击请网页进入
'''.strip()


sv = Service('yobot_clan',help_=sv_help_entertainment, bundle='pcr会战')
