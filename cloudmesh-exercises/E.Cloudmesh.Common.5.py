from cloudmesh.common.StopWatch import StopWatch
from time import sleep


StopWatch.start('time')
sleep(1)
a = 1+1
print(a)
sleep(1)
b = 2+2
print(b)
sleep(1)
print("A+B =", a+b)
sleep(1)
StopWatch.stop('time')
print("running time:", StopWatch.get('time'))