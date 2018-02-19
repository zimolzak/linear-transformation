# python -mpip install -U pip
# python -mpip install -U matplotlib
# conda install python.app
# source activate py27

import matplotlib
import matplotlib.pyplot as plt
import sys
from numpy import pi, sin, cos, matrix, concatenate, linalg

## set up some globals

m_string = '1 0.5; 2 1.2'
if len(sys.argv) > 1:
    m_string = sys.argv[1]

vi = sys.version_info
assert vi.major == 2

unit_circle = []
theta = 0
while theta <= 2 * pi:
    unit_circle.append([sin(theta), cos(theta)])
    theta += 2 * pi / 32

u = matrix(unit_circle)
a = matrix(m_string)

## do calculations

p = u * a
evev = linalg.eig(a)
eigenvecs = evev[1].T # default is return vecs in columns, so I transpose it.

## plot unit circle and its transformation

fig, ax = plt.subplots()

for i in range(len(u)):
    xs = [u[i,0], p[i,0]]
    ys = [u[i,1], p[i,1]]
    plt.plot(xs, ys, 'go-')

## plot eigenvectors

print eigenvecs

for i in range(len(eigenvecs)):
    xs = [0, eigenvecs[i,0]]
    ys = [0, eigenvecs[i,1]]
    plt.plot(xs, ys, 'r+-')

## wrap up

ax.set_aspect(1.0)
ax.set_title(str(a))
plt.show()
