# Hoshino插件指令
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
| 插件            | 作用                        |
| --------------- | --------------------------- |
| Rua | 发送一张搓群友头像的gif图片 |

![关于我的项目只有setu插件更新这回事](https://img-blog.csdnimg.cn/img_convert/93e4a4317f5ffdfb7bfd4e3a732f5181.png)

关于只有我的涩图插件在更新这档事
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