import turtle as t


t.speed(0)              #设置笔速度

#轮廓
t.fillcolor('yellow')   #设置填充颜色
t.up()                  #抬笔
#t.goto((150,150))      #移动至指定位置
t.setx(150)             #移动位置
t.sety(150)             #移动位置
t.left(90)              #向左旋转90度
t.down()                #下笔
t.begin_fill()          #准备填充
t.circle(150,180)       #画一个圆弧  半径150  角度180
t.fd(300)               #向前走300  可用forward
#t.forward(300)         #forward=fd
t.circle(150,180)       #画一个圆弧  半径150  角度180
t.fd(300)               #向前走300
t.end_fill()            #完成填充

#眼镜框
t.fillcolor('white')    #设置颜色
t.width(5)              #设置笔的宽度
t.up()                  #抬笔
t.goto((80,150))        #移动到指定位置
t.down()                #落笔
t.begin_fill()          #开始填充
t.circle(40)            #半径为40的圆
t.up()                  #抬笔
t.goto((0,150))         #移动至指定位置
t.down()                #落笔
t.circle(40)            #半径为40的圆
t.end_fill()            #完成填充

#眼镜边
t.up()                  #抬笔
t.goto((152,150))       #到指定位置
t.down()                #落笔
t.width(15)             #设置笔宽度
t.left(90)              #向左旋转90度
t.fd(74)                #向前前进74
t.up()                  #抬笔
t.goto((-78,151))       #移动至指定位置
t.down()                #落笔
t.width(15)             #设置笔的宽度
t.fd(74)                #向前前进74

#眼球
t.up()                  #
t.goto((-45,150))       #
t.down()                #
t.dot(40)               #画一个半径为40的实心圆
t.up()                  #
t.goto((45,150))        #
t.down()                #
t.dot(40)               #画一个半径为40的实心圆

#瞳孔
t.up()                  #
t.goto((-35,150))       #
t.down()                #
t.pencolor('white')     #更改画笔颜色   画笔默认颜色为黑色
t.dot(15)               #画一个半径为15的实心圆
t.up()                  #
t.goto((55,150))        #
t.down()                #
t.pencolor('white')     #设置笔的颜色
t.dot(15)               #画一个半径为15的实心圆

#嘴巴
t.up()
t.goto((-90,50))
t.down()
t.pencolor('red')
t.width(4)
t.left(120)
t.circle(100,130)       #半径为100角度为130的圆

#裤子
t.pencolor('black')
t.width(1)
t.fillcolor('blue')
t.up()
t.goto((-100,-100))
t.down()
t.begin_fill()
t.right(70)
t.fd(198)
t.right(90)
t.fd(60)
t.left(90)
t.fd(50)
t.right(90)
t.circle(-150,180)
t.right(90)
t.fd(50)
t.left(90)
t.fd(50)
t.end_fill()

#裤子   右边带子
t.fillcolor('blue')
t.up()
t.goto((150,-35))
t.down()
t.begin_fill()
t.width(1)
t.left(180)
t.pencolor('black')
t.fd(15)
t.right(43)
t.fd(80)
t.right(90)
t.fd(15)
t.right(90)
t.fd(98)
t.end_fill()

#裤子    左边带子
t.fillcolor('blue')
t.up()
t.goto((-150,-35))
t.down()
t.begin_fill()
t.width(1)
t.right(140)
t.pencolor('black')
t.fd(15)
t.left(43)
t.fd(80)
t.left(90)
t.fd(15)
t.left(90)
t.fd(98)
t.end_fill()

#口袋
t.up()
t.goto((-50,-140))
t.right(130)
t.width(5)
t.down()
t.fd(100)
t.right(90)
t.fd(25)
t.up()
t.goto((-50,-140))
t.down()
t.fd(25)
t.circle(50,180)

t.mainloop()            #让程序一直运行