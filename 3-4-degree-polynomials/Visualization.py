# Article: "Cubic polynomials with real or complex coefficients: The full picture"
# Author: N. S. Bardell
# Published: 2016
# Journal: Australian senior mathematics journal

import matplotlib.pyplot as plt
import numpy as np

#Visualization of the roots of cubic with real coefficients
def visualizer(rotat_angle, view_angle, v_range, a, b, c, d):

  # Most variable names (like flg or ax) are standard for libraries
  # numpy and matplotlib for better code readability

  # Creation of 3D space
  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')

  # Creating of vectors x and y in a range (-v_range, v_range) both to create plot Oxy at meshgrid
  # Third argument is responsible for the accuracy of displaying surfaces
  X = np.arange(-v_range, v_range, 0.15)
  Y = np.arange(-v_range, v_range, 0.15)
  X, Y = np.meshgrid(X, Y)

  # Creating two arrays for values (Z1 and Z2) and painting (C1 and C2) functions
  Z1 = np.empty_like(X)
  Z2 = np.empty_like(X)
  C1 = np.empty_like(X, dtype=object)
  C2 = np.empty_like(X, dtype=object)

  for i in range(len(X)):
    for j in range(len(X[0])):

      # Current coordinate
      x = X[i][j]
      y = Y[i][j]

      # Formulas for surfaces, derived from parenthesis expansion of
      # a(x+iy)**3 + b(x+iy)**2 + c(x+iy) + d = Q + i*W, then z1 = Q, z2 = W
      # You can add more coefficients like the fourth degree or more
      z1 = (a*x+b)*(x*x-y*y)+x*(c-2*a*y*y)+d
      z2 = y*(a*(3*x*x-y*y)+2*b*x+c)

      # Writing to arrays of values
      Z1[i,j] = z1
      Z2[i,j] = z2

      # Writing to painting arrays
      # Author prefers to write some constant(0.5, for example) value instead of z1
      C1[i,j] = plt.get_cmap("Greens")(0.5)
      C2[i,j] = plt.get_cmap("Blues")(z2)

  # Create a transparent bridge region
  X_bridge = np.vstack([X[-1,:],X[-1,:]])
  Y_bridge = np.vstack([Y[-1,:],Y[-1,:]])
  Z_bridge = np.vstack([Z1[-1,:],Z2[-1,:]])

  # Creating of labels of axises
  ax.set_xlabel("X axis")
  ax.set_ylabel("Y axis")
  ax.set_zlabel("Z axis")

  # Limitation the range of Z coordinate in (-8 * v_range**2, 8 * v_range**2)
  # The selected limits are conditional and chosen empirically
  ax.set_zlim(-8*v_range*v_range, 8*v_range*v_range)

  # Creating and filling of color bridge for Z_coordinates
  color_bridge = np.empty_like(Z_bridge, dtype=object)
  color_bridge.fill((1,1,1,0))

  # Join the two surfaces flipping one of them (using also the bridge)
  X_full = np.vstack([X, X_bridge, np.flipud(X)])
  Y_full = np.vstack([Y, Y_bridge, np.flipud(Y)])
  Z_full = np.vstack([Z1, Z_bridge, np.flipud(Z2)])
  color_full = np.vstack([C1, color_bridge, np.flipud(C2)])

  # Creation of plot of surfaces
  # You can change parameters rstride, cstride, linewidth and antialiased to
  # change quality, best values are all 1 and antialiased=False.
  surf_full = ax.plot_surface(X_full, Y_full, Z_full, rstride=1, cstride=1, shade = True,
                              facecolors=color_full, linewidth=1,
                              antialiased=False)

  # Changing of viewing and rotation angles
  ax.view_init(view_angle, rotat_angle)

  # Changing of image size
  fig.set_size_inches(8, 8)

  # Grid removing, delete this if u want to see it
  ax.grid(False)

  # Drawing of final plot
  plt.draw()



# Coefficients of polynom ( maximum degree of polynomial is three)
# Program can be modified for complex coefficients
a,b,c,d = map(float,input().split())

# Visibility range (4 is enough for small polynomials, otherwise we use a reduced sum of absolutes)
# The selected value is conditional and chosen empirically
v_range = max(4,(abs(a)+abs(b)+abs(c)+abs(d))//2)


for angle in range(0,4):
  # 1 arg is the rotation around space Oxyz, 2 arg is the viewing angle relative to Oxy plane
  # In the current example, these arguments are chosen empiricially, they can be changed as you like

  visualizer(60*angle, 45+15*angle, v_range, a, b, c, d)

  # To display multiple pictures
  plt.pause(0.01)