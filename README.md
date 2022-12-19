# //myezviz
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=c1pher-cn&repository=homeassistan-ezviz&category=integration)

配置说明
-----------------------------

    camera:
      - platform: myezviz
        name: name1
        id: yourdeviceid1
        key: appkey
        sec: appsecret
        ismaoyan: maoyan
      - platform: myezviz
        name: name2
        id: yourdeviceid2
        key: appkey
        sec: appsecret
        ismaoyan: notmaoyan
        
        
        
版本说明
-----------------------------
master分支下支持最新custom_components文件格式，直接下载到对应目录即可不需要任何修改

old分支下为老的custom_components文件格式


原理说明
-----------------------------
该插件主要基于作者自身需求设计产生，作者日常使用ha对摄像头没有很高的实时性需求，但希望有一定安全性，所以未直接使用本地局域网协议直接访问摄像头，通过周期性调用萤石抓图api定期获取摄像头实时画面并下载到ha本地，通过ha的临时文件展示该图片作为摄像头画面。
因为猫眼不支持抓包，故采用最近一条告警信息作为图像来源，这里的‘告警’包括动作、人脸识别、门铃

    
参数说明   
-----------------------------   
 deviceid（设备序列号） 见 https://open.ys7.com/console/device.html
 
 appkey和appsecret 见 https://open.ys7.com/console/application.html （创建应用后可见）
 
 ismaoyan 设备是否为猫眼，普通摄像头填notmaoyan。猫眼填maoyan

（插件里布尔类型值总是传不进去，所以配置文件才如此不优雅。。。哪位知道怎么配请赐教，跪谢）


 
 
问题支持
-----------------------------

使用问题，请提issues，或者到b站专栏处留言 https://www.bilibili.com/read/cv19602064 （个人看b站的频率高一点）

提问请描述清楚自己的情况，让相同问题的人能看到，不要私信！！！！，不要私信！！！！，不要私信！！！！


请我喝咖啡？
-----------------------------
玩b站的朋友关注投币支持一下就行了，咖啡就不需要了





