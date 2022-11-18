# homeassistan-ezviz
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)

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


 
 



其他问题，可私信联系
-----------------------------

b站 https://space.bilibili.com/15856864



