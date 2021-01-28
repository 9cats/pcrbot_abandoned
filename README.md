# VPS搭建部署 HoshinoBot 与 yobot
闲着用VPS搭建一个qq机器人
(安全性未知/概率性暴毙/购买的VPS便宜性能较差且未翻越GFW)
## 主要参考
### 参考文章
 [Linux 下部署一个公主连结 qq 群聊机器人](https://cn.pcrbot.com/deploy-a-priconne-bot-on-linux/)
### 常用站点
[pcrbot](https://cn.pcrbot.com/)

[yobot](https://yobot.win/)

[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)

[go-cqhttp](https://docs.go-cqhttp.org/guide/#go-cqhttp)

[HoshinoBot插件索引](https://github.com/pcrbot/HoshinoBot-plugins-index)

## yobot功能
[yobot官方介绍](https://yobot.win/features/)（注：我删除了部分插件，部分插件不生效）
## HoshinoBot插件
| 插件 | 名称 | 作用 |
| ---- | --- | ---- |
| Rua | 搓你 | 发送一张搓群友头像的gif图片 |
| feedback | 反馈 | 向HoshinoBot发送反馈信息 |
| aircon | 群空调 | 通过比较科学的算法来得到群活跃度 |
| antiqks | 骑空士的阴谋 | 揭发群友的阴谋 |
| dice | 掷骰子 | 产生随机结果 |
| gacha | 模拟抽卡 | 别看了，井田人竟是我自己 |
| pcr-avatar-guess | 猜头像 | 优衣你不识得？ |
| pcr-cherugo | 切噜 | 切啰巴切拉切蹦切蹦 |
| pcr-desc-guess | 猜角色 | 根据描述猜出角色 |
| pcr-login-bouns | 群签到 | 妈亲自来给你签到 |
| pcr-query | pcr查询 | 查找pcr的相关信息信息 |
| random-repeater | 复读机 | 概率跟着群友+1 |
| setu_mix | 涩图 | DDDD |
| sleeping-set | 精致睡眠 | 群禁言 |
| chat | 聊天 | 自定义回复群友内容 |
| rss | 推送 | 推送up主或官方 |
| PcrRun | 赛跑（下注） | pcr角色的赛跑小游戏 |
| PcrDuel | 比拼（下注） | 创建贵族进行俄罗斯转盘决斗，提升贵族等级，争夺pcr女友的小游戏 |

![关于我的项目只有setu插件更新这回事](https://img-blog.csdnimg.cn/img_convert/93e4a4317f5ffdfb7bfd4e3a732f5181.png)

关于只有我的涩图插件在更新这档事

## 各插件指令相关详情

### Rua
### feddback
### aircon
### antiqks
### dice
### gache
### pcr-avatar-guess
### pcr-cherugo
### pcr-comic
### pcr-desc-guess
### pcr-login-bouns
### pcr-news-bili
### pcr-news-tw
### pcr-query
### pcr-query
### random-repeater
### setu_mix
### sleeping-set
### chat

## 移植注意

### 项目目录：
* Pcrbot
  * Hoshino
    * hoshino
    * res （资源）
      * gacha （抽卡音效）
      * HARU （野中晴语言包）
      * hayasaka （早坂爱语言包）
      * MEGUMIN （惠惠语言包）
      * pcrwarn （黑猫语言包）
      * record （小仓唯语言包）
      * img （图库）
    * <font color="#06f090">log（Hoshino数据）</font>
    * LICENSE
    * requirements.txt
    * run.py
  * yobot
    * src
      * client
        * <font color="#06f090">yobot_data（yobot数据）</font>
        * other
    * script
    * docs
    * LICENSE
    * __init.py
  * gocqhttp
    * go-cqhttp
    * <font color="#06f090">data（QQ数据）</font>
    * <font color="#06f090">logs（日志文件）</font>
    * <font color="#f65060">config.hjson</font>（配置文件）  
    * <font color="#f65060">device.json</font>（配置文件） 
  

### 别又忘了随机生成的密钥
| 加密中的各值 |  最常见的一种加密算法    |
|:--------:| -------------:|
|TOKEN| XXXXXXXXXXXXXXXX|
|KEY| IAMADIDI|
|RESULT| U2FsdGVkX1+fWk0SDQFei0u6SIv9h2HNPQDrpDS43VSd9raE1WCDWoxSfqaPjSmG|