from pylab import *
x = linspace(0,5,10)
y = x ** 3
g = y * x
'''
figure()
plot(x,y, 'b')
xlabel('x')
ylabel('y')
title('grafik')
show()
'''
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.5, 0.5, 0.2, 0.2])

#main
axes1.plot(x,y,'b')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('grafik')

#import
axes2.plot(g,x,'y')
axes2.set_xlabel('g')
axes2.set_ylabel('x')
axes2.set_title('grafik')
show()