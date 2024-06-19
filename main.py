from vpython import *
import math
# G=6.67e-11
# Ms=1.989e30
# Me=5.972e24
# AU=1.49e11
# Rs=6.957e8
# Re=6.371e6


G=6.67e-11
Ms=1.989e30
Me=5.972e24
AU=1.49e11
Rs=6.957e8
Re=6.371e6

r1=Rs*3
m1=Ms
r2=Rs*3
m2=Ms
r3=Rs*3
m3=Ms



# #****************** Próba czegoś stabilnego xdddddd ***********************
# s1= sphere(pos = vector(-80*Rs,0,0), radius= r1, color = color.blue, make_trail = True)
# s2= sphere(pos = vector(80*Rs,0,0), radius= r2, color = color.yellow, make_trail = True)
# s3= sphere(pos = vector(0,0,0), radius= r3, color = color.green, make_trail = True)
#
# s1.p=vector(0,Ms*3e4,0)
# s2.p=vector(0,-Ms*3e4,0)
# s3.p=vector(0,0,Ms*50)
#
# m3=Ms/1000
# #rate(1500)





s1= sphere(pos = vector(-40*Rs,0,0), radius= r1, color = color.blue, make_trail = True)
s2= sphere(pos = vector(40*Rs,0,0), radius= r2, color = color.yellow, make_trail = True)
s3= sphere(pos = vector(0,-(sqrt(3)*40*Rs),0), radius= r3, color = color.green, make_trail = True)



s1.p=vector(Ms*3e4,0,0)
s2.p=vector(0,Ms*3e3,-Ms*3e3)
s3.p=vector(0,Ms*3e3,0)

t=0
dt=1000
while True:
    rate(300)
#odległośc, siła grawitacji
    r1_2=s2.pos-s1.pos
    F1_2=G*m1*m2*norm(r1_2)/(mag(r1_2)**2)
    r2_3=s3.pos-s2.pos
    F2_3=G*m2*m3*norm(r2_3)/(mag(r2_3)**2)
    r1_3= s3.pos - s1.pos
    F1_3= G * m1 * m3 * norm(r1_3) / (mag(r1_3) ** 2)
#suma sił na ciele
    s1.F= F1_2 + F1_3
    s2.F= F2_3 + -F1_2
    s3.F= -F1_3 + -F2_3
#popęd xd
    s1.p += s1.F * dt
    s2.p += s2.F * dt
    s3.p += s3.F * dt
#przemieszczenie
    s1.pos+= (s1.p*dt)/m1
    s2.pos+= (s2.p*dt)/m2
    s3.pos+= (s3.p*dt)/m3
