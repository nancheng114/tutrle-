import turtle as t

#导入 turtle库    as+t  给turtle命名为t

'''
三个单引号也为注释
#使用库 需要先安装 然后再导入
#pip install 库名
ctrl+D 鼠标放在代码后面，可以直接复制一行代码
批量注释  ctrl+？   

'''
#1创建画布  括号内为画布大小

t.setup(800,800)

#2设置笔

t.pencolor('orange')         #默认黑色
t.width(3)                   #设置画笔宽细
t.speed(5)                   #控制笔的速度  1~10由快到慢

#3移动笔

#前进
#t.forward(100)               #forward(100)或者 fd(100)括号内表示距离
t.fd(100)                     #前进(100)，同forward(100)一样
#后退

t.pencolor('red')             #设置颜色
t.width(5)                    #设置画笔宽度

t.bk(200)                     #后退(200)，用处同back(200)一样
#t.back(200)                  #后退(200)

#4移动到指定位置

t.goto((100,200))             #括号中间加坐标
t.pencolor('cyan')
t.goto((-300,300))

#5修改坐标

t.setx(200)                   # y 轴不变，修改 X 轴
t.pencolor('yellow')
t.sety(-10)                   # x 轴不变，修改 y 轴

#6回到坐标原点

t.home()

#7让程序一直运行

t.mainloop()

