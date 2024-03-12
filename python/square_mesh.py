#%%
import gmsh
import numpy as np
import matplotlib.pyplot as plt

# %%
xlim=np.array([0,1])
ylim=np.array([0,1])
h=0.1

#%%
gmsh.initialize()
gmsh.model.add("square_mesh")

#%%
gmsh.model.geo.addPoint(xlim[0],  ylim[0], 0, h, 1)  
gmsh.model.geo.addPoint(xlim[1],  ylim[0], 0, h, 2)  
gmsh.model.geo.addPoint(xlim[1],  ylim[1], 0, h, 3)
gmsh.model.geo.addPoint(xlim[0],  ylim[1], 0, h, 4)

#%%

gmsh.model.geo.addLine(1, 2, 1)  
gmsh.model.geo.addLine(2, 3, 2)  
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)

#%%

gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

s = gmsh.model.addPhysicalGroup(2, [1]) # En este caso no se especifica tag
gmsh.model.setPhysicalName(2, s, "surface")  # Se puede definir un nombre

gmsh.model.geo.synchronize()

#%%
gmsh.option.setNumber('Mesh.SurfaceFaces', 1)  # Ver las "caras" de los elementos finitos 2D
gmsh.option.setNumber('Mesh.Points', 1)        # Ver los nodos de la malla

#%%
# Y finalmente guardar la malla
filename = 'square_mesh.msh'
gmsh.write(filename)

#%%
nod, xnod, pxnod = gmsh.model.mesh.getNodes()
xnod = xnod.reshape((nod.size, -1))
#imprime la lista de nodos
print(xnod[:,:2])

gmsh.finalize()
# %%
