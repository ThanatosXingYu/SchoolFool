# SchoolFool
为恶搞学校教师设计的插入U盘弹窗病毒，无感染性。

# 效果
电脑开机后会自动运行本程序，当检测到U盘(可移动设备)后会自动弹窗，循环打开网页`fhzx.top/laji`,并且播放国歌`fhzx.top/laji/a.mp3`。

# 安装

要安装最新的开发版本，请键入以下命令：

     pip install psutil

缺少什么库pip install即可。

# 运行方法

将文件放在Windows系统开机自启动目录下即可，一般为

> C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

也可使用pyinstaller打包成exe文件后再移动目录

# 说明

本程序只为恶搞使用，无任何传染性、破坏性，使用所造成的一切后果请自行承担。
