# examples:
# python linalg.py "1 -0.2; 0.5 2"
# python linalg.py "1 -1; 0 2"
# python linalg.py
# python linalg.py 'rot 5'
# python linalg.py 'rotate 5'
# python linalg.py 'rot 30'
# python linalg.py 'rot 170'

## here is junk I [maybe?] had to do to set up.
## Most important is the last one.

# python -mpip install -U pip
# python -mpip install -U matplotlib
# conda install python.app
# source activate py27

import matplotlib
import matplotlib.pyplot as plt
import sys
from numpy import pi, sin, cos, matrix, concatenate, linalg
from random import uniform

## set up some globals

def rotation_matrix(degrees):
    t = degrees / 360 * 2 * pi
    return(matrix([[cos(t), -sin(t)], [sin(t), cos(t)]]))

m_string = '1 0.5; 2 1.2'
if len(sys.argv) > 1:
    if sys.argv[1].startswith('rot'):
        degrees = float(sys.argv[1].split()[1])
        m_string = rotation_matrix(degrees)
    else:
        m_string = sys.argv[1]
else: # no argv
    m_string = (str(uniform(-2,2)) + ' ' +
                str(uniform(-2,2)) + '; ' + 
                str(uniform(-2,2)) + ' ' +
                str(uniform(-2,2)))

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

p = u * a.T
evev = linalg.eig(a)
eigenvecs = evev[1].T # default is return vecs in columns, so I transpose it.

print "Eigenvalues:", evev[0]
print "Eigenvectors in rows:\n", eigenvecs

## plot unit circle and its transformation

fig, ax = plt.subplots()

for i in range(len(u)):
    xs = [u[i,0], p[i,0]]
    ys = [u[i,1], p[i,1]]
    plt.plot(xs, ys, 'go-')

## plot eigenvectors

for i in range(len(eigenvecs)):
    xs = [0, eigenvecs[i,0]]
    ys = [0, eigenvecs[i,1]]
    plt.plot(xs, ys, 'r+-')

p2 = eigenvecs * a.T
for i in range(len(p2)):
    ax.plot(p2[i,0], p2[i,1], 'r^')

## wrap up

ax.set_aspect(1.0)
ax.set_title(str(a))
plt.show()
