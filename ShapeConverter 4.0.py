# ==============================================================================#
# =============================SHAPE CONVERTER==================================#
# ==============================================================================#
from turtle import*
from time import*

reset()

ht()

speed(12)
delay(0)
color("#ff0000", "#0000ff")
lt(90)


def conv(x, y, t):
    for i in range(y):
        fd(x)
        lt(t)


x = int(input("Select the length of the side of the pattern. (in pixels) "))
y = int(input("Choose how many times one line will be repeated. "))
t = int(input("Select a U-turn before the second line. (in degrees) "))
a = int(input("Choose after how long your figure will be removed? (in seconds) "))
z = int(input("Choose the width of your shape. "))
print("Ready! To view your shape, go to the Python Turtle Graphics tab.")

width(z)
begin_fill()
conv(x, y, t)
end_fill()
sleep(a)
clear()
pu()

exitonclick()
# ==============================================================================#
# ========================SHAPE CONVERTER VERSION: BETA 4.0======================#
# ==============================================================================#
