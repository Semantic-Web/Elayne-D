import numpy as np
import matplotlib.pyplot as plt
import datetime as DT

data= np.loadtxt('/home/pi/ass3/data/good.csv', usecols=(0,1),delimiter=',',dtype={'names': ('date', 'step_count'),'formats': ('S10', 'i4')} )

cal= np.loadtxt('/home/pi/ass3/data/good.csv', usecols=(0,2),delimiter=',',dtype={'names': ('date', 'calories'),'formats': ('S10', 'i4')} )

x = [DT.datetime.strptime(key,"%Y-%m-%d") for (key, value) in data ]
y = [value for (key, value) in data]
z = [value for (key,value) in cal]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid()

fig.autofmt_xdate()

plt.plot(x,y, label="steps")
plt.plot(x,z, label="calories")
plt.xlabel('Date')
plt.ylabel('Steps')
plt.title('Daily Steps')
plt.legend(loc='upper right')

plt.savefig('/home/pi/ass3/ped.png')
plt.show()
