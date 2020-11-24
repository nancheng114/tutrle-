
#原理  前进的过程中不断改变笔的方向

# 不断  在程序中 体现出来的就是循环
#python严格区分缩进

#循环语句  for x in range()

# for x in range(10):     #10的话表示 0到10  包含10 但是不包含10
#     print(x)
#
#
# for x in range(1,11):   #输出1~10
#     print(x)

#导入库
import turtle as t

t.pencolor('cyan')
t.speed(5)
for i in range(9):    #向前走（10）向左旋转10度循环9次
    t.fd(10)
    t.left(10)

for i in range(9):    #向前走（10）向右旋转10度循环9次
    t.fd(10)
    t.right(10)

t.mainloop()