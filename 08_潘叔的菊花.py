#向前100像素  画笔旋转90度，再向前100像素  形成第二条边  循环4次成一个正方形
import turtle as t

t.speed(6)              #控制笔的速度
t.pencolor('red')       #笔的颜色
t.fillcolor('yellow')   #填充颜色
t.begin_fill()          #开始填充

for x in range(36):         #需要36个正方形
    for i in range(4):      #一条线画完 转换角度 4次之后变成一个正方形
        t.fd(100)
        t.left(90)
    t.right(10)             #每个正方形画完后像右旋转10度

t.end_fill()                #结束填充

t.mainloop()