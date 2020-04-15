import numpy as np
import scipy.interpolate
import matplotlib.pylab as mp

# interpolation nodes
matrix = np.array(
    [0.062500, 0.187500, 0.312500, 0.437500, 0.562500, 0.687500, 0.812500, 0.937500])
# values
Fx = np.array([0.687959, 0.073443, -0.517558, -1.077264, -1.600455, -2.080815, -2.507266, -2.860307])

polynomial = (scipy.interpolate.lagrange(matrix, Fx))

solutions = [] #Has coefficients polynomial

for item in polynomial:
    solutions.append(item)

print("Our result is: ")

for i in range(len(solutions)):
    print("a{} = {}".format((i + 1), "%0.4f" % solutions[i]))

x = matrix
p1 = mp.plot(matrix, Fx, 'bo')

valueOfX = []
valueOfY = []

for x in np.arange(-1.0, 1.0, 0.001):
    y = polynomial(x)
    valueOfX.append(x)
    valueOfY.append(y)

p2 = mp.plot(valueOfX, valueOfY)

mp.legend((p1[0], p2[0]), ('Points', 'Line'))

mp.axis([-1, 1, -10, 10]) #Draw graph
mp.axvline()
mp.axhline()
mp.grid(True)
mp.savefig('graph.png', dpi=80)
mp.show()