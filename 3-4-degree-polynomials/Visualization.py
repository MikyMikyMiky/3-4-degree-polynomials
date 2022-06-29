# Article: "Cubic polynomials with real or complex coefficients: The full picture"
# Author: N. S. Bardell
# Published: 2016
# Journal: Australian senior mathematics journal

import matplotlib.pyplot as plt
import numpy as np


# Visualization of the roots of cubic with real coefficients
# Program can be modified for complex coefficients
def visualizer(rotat_angle, view_angle, v_range, a, b, c, d):
    # Most variable names (like flg or ax) are standard for libraries
    # numpy and matplotlib for better code readability

    # Creation of 3D space
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Creating of vectors x and y in a range (-v_range, v_range) both to create plot Oxy at meshgrid
    # Third argument is responsible for the accuracy of displaying surfaces

    v_step = 0.1  # Number that responsible for the accuracy of displaying surfaces, integer or float, must be positive

    X = np.arange(-v_range, v_range, v_step)
    Y = np.arange(-v_range, v_range, v_step)
    X, Y = np.meshgrid(X, Y)

    # Creating two arrays for values (Z1 and Z2) and painting (C1 and C2) functions
    Z1 = np.empty_like(X)
    Z2 = np.empty_like(X)
    C1 = np.empty_like(X, dtype=object)
    C2 = np.empty_like(X, dtype=object)

    for i in range(len(X)):
        for j in range(len(X[i])):

            # Current coordinate
            x = X[i][j]
            y = Y[i][j]

            # Formulas for surfaces, derived from parenthesis expansion of
            # a(x+iy)**3 + b(x+iy)**2 + c(x+iy) + d = Q + i*W, then z1 = Q, z2 = W
            # You can add more coefficients like the fourth degree or more
            z1 = (a * x + b) * (x * x - y * y) + x * (c - 2 * a * y * y) + d
            z2 = y * (a * (3 * x * x - y * y) + 2 * b * x + c)

            # Writing to arrays of values
            Z1[i, j] = z1
            Z2[i, j] = z2

            # Writing to painting arrays
            # Author prefers to write some constant(0.5, for example) value instead of z1
            C1[i, j] = plt.get_cmap("Greens")(z1)
            C2[i, j] = plt.get_cmap("Blues")(z2)

    # Create a transparent bridge region
    X_bridge = np.vstack([X[-1, :], X[-1, :]])
    Y_bridge = np.vstack([Y[-1, :], Y[-1, :]])
    Z_bridge = np.vstack([Z1[-1, :], Z2[-1, :]])

    # Creating of labels of axises
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")

    # Limitation the range of Z coordinate
    z_limit = 8 * v_range**2  # Z coordinate limits range constant, selected const is conditional and chosen empirically
    ax.set_zlim(-z_limit, z_limit)

    # Creating and filling of color bridge for Z_coordinates
    color_bridge = np.empty_like(Z_bridge, dtype=object)

    RGBA_tuple = (1, 1, 1, 0) # Stub tuple for color bridge, all numbers must be at [0,1]
    color_bridge.fill(RGBA_tuple)

    # Join the two surfaces flipping one of them (using also the bridge)
    X_full = np.vstack([X, X_bridge, np.flipud(X)])
    Y_full = np.vstack([Y, Y_bridge, np.flipud(Y)])
    Z_full = np.vstack([Z1, Z_bridge, np.flipud(Z2)])
    color_full = np.vstack([C1, color_bridge, np.flipud(C2)])

    # You can change parameters surface_quality and antialiased to
    # change quality, best values are surface_quality=1, width_of_line=0 and antialiased=False.

    surface_quality = 1  # amount of image downsapling, integer, must be positive
    width_of_line = 0  # width of line, integer or float

    # Creation of plot of surfaces
    ax.plot_surface(X_full, Y_full, Z_full, rstride=surface_quality, cstride=surface_quality,
                                facecolors=color_full, linewidth=width_of_line, antialiased=False)

    # Changing of viewing and rotation angles
    ax.view_init(view_angle, rotat_angle)

    # Changing of image size
    image_size = 8  # Size of image, integer or float, must be positive, default is 6.4
    fig.set_size_inches(image_size, image_size)

    # Grid removing, delete this if u want to see it
    ax.grid(False)

    # Drawing of final plot
    plt.draw()


# Coefficients of polynom ( maximum degree of polynomial is three)
a, b, c, d = map(float, input("Enter the coefficients separated by a space: ").split())

viewing_angle = int(input("Enter azimuth angle: "))  # viewing angle relative to Oxy plane, integer or float
rotation_angle = int(input("Enter elevation angle: "))  # the rotation around space Oxyz, integer or float

p_const = .01  # constant that is used to pause between displaying different images, integer or float, must be positive

# Visibility range
minimum_of_v_range = 4  # minimum of visibility range, integer or float, enough for small polynomials,
red_sum_of_abs = (abs(a) + abs(b) + abs(c) + abs(d)) // 2              # else we use a reduced sum of absolutes
v_range = max(minimum_of_v_range, red_sum_of_abs)

visualizer(rotation_angle, viewing_angle, v_range, a, b, c, d)

plt.pause(p_const)  # there will be no picture without it
