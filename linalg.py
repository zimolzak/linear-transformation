# python -mpip install -U pip
# python -mpip install -U matplotlib
# conda install python.app
# source activate py27

import matplotlib
import matplotlib.pyplot as plt
import sys
from numpy import pi, sin, cos, matrix, concatenate, linalg

m_string = '1 0.5; 2 1.2'
if len(sys.argv) > 1:
    m_string = sys.argv[1]

vi = sys.version_info
assert vi.major == 2

unit_circle = []
for offset in [0, pi/2, pi, 1.5*pi]:
    for a in [0, pi/6, pi/4, pi/3]:
        theta = offset + a
        unit_circle.append([sin(theta), cos(theta)])

u = matrix(unit_circle)
a = matrix(m_string)
p = u * a
evev = linalg.eig(a)
eigenvecs = evev[1]
print eigenvecs

fig, ax = plt.subplots()

for i in range(len(u)):
    xs = [u[i,0], p[i,0]]
    ys = [u[i,1], p[i,1]]
    
    plt.plot(xs, ys, 'go-')

#ax.plot(u.T[0], u.T[1], 'bo')
#ax.plot(p.T[0], p.T[1], 'ro')

ax.plot(eigenvecs.T[0], eigenvecs.T[1], 'r+')
ax.plot(0, 0, 'k+')
ax.set_aspect(1.0)
ax.set_title(str(a))
plt.show()
