#导入库
import turtle as t

#笔的方向默认水平向右
t.left(50)           #向左旋转50度，括号内为角度，left向左，right向右
t.fd(100)            #fd=forward  前进距离

#向右旋转
t.right(90)          #向右旋转45度，括号内为角度，left向左，right向右
t.pencolor('red')
t.fd(200)

#设置成指定角度
t.seth(90)           # seth设置笔的角度
t.fd(200)

#让程序一直运行
t.mainloop()