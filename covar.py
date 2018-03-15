import matplotlib
import matplotlib.pyplot as plt
import sys
from numpy import mean, matrix, linalg, dot, add, arctan, rad2deg

vi = sys.version_info
assert vi.major == 2

x1 = [0.0, 1.0, 2.0, 1.5, 0.2, 0.2, 3.0, 1.0, 3.1, 1.0,
      2.0, 2.5, 2.5, 2.0, 2.5, 1.5, 2.5, 2.2, 0.5, 1.5,
      1.2, 1.7, 2.7, 3.5, 2.5, 2.6, 3, 4]

x2 = [0.1, 1.1, 0.6, 0.5, 0.3, 0.8, 1.8, 1.5, 2.1, 1.3,
      1.2, 1.5, 1.2, 1.1, 2.3, 2.2, 2.5, 2.1, 1.0, 2.7,
      2.0, 2.2, 1.4, 4, 5, 6.5, 8, 9]

def recenter(vec):
    return [el - mean(vec) for el in vec]

def cov(v1, v2):
    n = len(v1)
    assert n == len(v2)
    return dot(recenter(v1), recenter(v2)) / n

def cov_matrix (v1,v2):
    return matrix([[cov(v1,v1), cov(v1,v2)],
                   [cov(v2,v1), cov(v2,v2)]])

#### Calculations

C = cov_matrix(x1, x2)
print "Covariance matrix:\n", C, "\n"

evev = linalg.eig(C)
eigenvecs = evev[1].T # default is return vecs in columns, so I transpose it.
print "Eigenvalues:", evev[0]
print "Eigenvectors in rows:\n", eigenvecs, "\n"

print "Principal component angles:"
for ev in eigenvecs.tolist():
    print round(rad2deg(arctan(ev[1] / ev[0])), 1)

## plot points

fig, ax = plt.subplots()
for i in range(len(x1)):
    plt.plot(x1[i], x2[i], 'go')

## plot eigenvectors

for i in range(len(eigenvecs)):
    xs = [mean(x1), add(eigenvecs[i,0], mean(x1))]
    ys = [mean(x2), add(eigenvecs[i,1], mean(x2))]
    plt.plot(xs, ys, 'r+-')

## wrap up

ax.set_aspect(1.0)
plt.savefig('pca.png')
