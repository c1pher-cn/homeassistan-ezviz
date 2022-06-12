# homeassistan-ezviz
配置说明
-----------------------------

    camera:
      - platform: ezviz
        name: "name"
        id: "yourdeviceid"
        key: "appkey"
        sec: "appsecret"
        
版本说明
-----------------------------
master分支下支持最新custom_components文件格式，直接下载到对应目录即可不需要任何修改
old分支下为老的custom_components文件格式


原理说明
-----------------------------
该插件主要基于作者自身需求设计产生，作者日常使用ha对摄像头没有很高的实时性需求，但希望有一定安全性，所以未使用本地局域网协议直接访问摄像头，仅需要同步近期截图即可，所以插件仅使用萤石官方api，定期获取摄像头实时画面并下载到ha本地，通过ha的临时文件展示该图片作为摄像头画面

    
参数说明   
-----------------------------   
 deviceid（设备序列号） 见 https://open.ys7.com/console/device.html
 
 appkey和appsecret 见 https://open.ys7.com/console/application.html （创建应用后可见）
 
 


其他问题，可私信联系
-----------------------------

b站 https://space.bilibili.com/15856864

微博 https://weibo.com/u/1147593092


