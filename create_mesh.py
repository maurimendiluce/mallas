from func_mesh import *

#argumentos para crear la malla
h=0.05
xmin=0
xmax=1
ymin=0
ymax=1

#creamos la malla y guardamos los datos
filename = create_mesh(h,xmin,xmax,ymin,ymax)

nodes = xnod_from_msh(filename, dim=2)
elem = LaG_from_msh(filename)

#plot de la malla
plot_msh(filename, '2D')
plt.show()

#exportamos los datos para poder usarlos
np.savetxt("nodes.csv", nodes, delimiter=",")
np.savetxt("elements.csv", elem[:,1:], delimiter=",")