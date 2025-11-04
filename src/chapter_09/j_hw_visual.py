import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Функція Сфери
def sphere_function(x, y):
    return x**2 + y**2

# Побудова сітки точок для графіка
x_values = [i / 10 for i in range(-50, 51)]  # x ∈ [-5, 5]
y_values = [i / 10 for i in range(-50, 51)]  # y ∈ [-5, 5]

# Обчислення значень функції для кожної точки
z_values = [[sphere_function(x, y) for x in x_values] for y in y_values]

# Побудова графіка
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Графік поверхні
X, Y = zip(*[(x, y) for y in y_values for x in x_values])
Z = [sphere_function(x, y) for x, y in zip(X, Y)]
ax.plot_trisurf(X, Y, Z, cmap='viridis', edgecolor='none')

# Підпис осей
ax.set_title("Функція Сфери", fontsize=16)
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("f(x1, x2)")

plt.show()
