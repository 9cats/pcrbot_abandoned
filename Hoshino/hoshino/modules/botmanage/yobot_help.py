from hoshino import Service
import socket

def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip

sv_help_query = '''
[日程(今日/明日/x月x日)(可自动)] 查看活动日程
[日程表] 查看一周日程
[挖矿计算 +当前名次] 计算剩余可获得的奖励钻石
'''.strip()

sv = Service('yobot_query', help_=sv_help_query, bundle='pcr查询')

sv_help_entertainment = '''
[人偶] (权:主人)人偶功能
'''.strip()

sv = Service('yobot_entertainment',help_=sv_help_entertainment, bundle='pcr娱乐')


sv_help_clan = '''
[手册] 查看公会战使用手册
[面板] 进入公会战面板
[创建日服公会]	日/韩/台/国，创建后可在后台修改
[加入公会 (@某人)]	加入到公会名单
[加入全部成员]	
[报刀2000000 (@某人) (昨日) (：留言)] 对boss造成伤害，记录
[尾刀 (@某人) (昨日) (：留言)] 对boss造成伤害并击败时用，记录伤害
[SL (@某人) (？)] SL查询和记录
[撤销]	撤销上一次报刀
[状态]	显示boss状态
[预约1 (：留言)] boss出现时通知
[挂树 (：留言)]	boss被击败时通知
[查1/查树] 查询预约boss和挂树的成员
[取消预约1/取消1] 取消预约
[申请出刀] 提醒后面申请出刀的人有人正在挑战boss
[锁定:留言]	锁定boss，提醒后面申请出刀的人并留言
[解锁] 解锁boss，其他人可以继续申请3
更多详情可点击请网页进入
'''.strip() + "\nhttp://" + get_host_ip() + ":9222/helpOfYobot/"


sv = Service('yobot_clan',help_=sv_help_clan, bundle='pcr会战')
