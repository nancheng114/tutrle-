import turtle as t

t.circle(80)

#模拟抬笔的效果
t.pencolor('white')         #更改笔的颜色，白色
t.setx(-50)                 #更改坐标

t.pencolor('green')         #笔的颜色绿色
t.fd(150)                   #向前150

#方法二
#up()   抬起笔   turtle.up()
t.up()
t.sety(-100)

#donw()  放下笔    turtle.dowm()
t.down()
t.fd(150)
t.pencolor('red')
t.circle(90)

t.mainloop()