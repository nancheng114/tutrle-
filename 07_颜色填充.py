import turtle as t

# t.circle(50)            #画一个半径50的圆
# t.up()
# t.sety(-100)
#
# t.pencolor('red')
# t.dot(50)

#填充颜色
#1.设置填充颜色

t.fillcolor('pink')         #fillcolor设置填充色粉色
t.speed(1)

#2.开始填充

t.begin_fill()
t.circle(100)
t.fd(120)
t.left(90)
t.fd(160)
t.home()
t.right(90)
t.circle(80)

#3.结束填充
t.end_fill()


#连续画图
t.up()
t.sety(-88)
t.down()
t.fillcolor('cyan')
t.begin_fill()
t.fd(150)
t.right(90)
t.fd(150)
t.right(135)
t.fd(220)
t.end_fill()

t.mainloop()