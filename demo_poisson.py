import numpy as np

import ufl
from dolfinx import fem, io, mesh, plot
from ufl import ds, dx, grad, inner

from mpi4py import MPI
from petsc4py.PETSc import ScalarType

msh = mesh.create_rectangle(comm=MPI.COMM_WORLD,
                            points=((0.0, 0.0), (2.0, 1.0)), n=(32, 16),
                            cell_type=mesh.CellType.triangle,)
V = fem.FunctionSpace(msh, ("Lagrange", 1))
facets = mesh.locate_entities_boundary(msh, dim=1,
                                       marker=lambda x: np.logical_or(np.isclose(x[0], 0.0),
                                                                      np.isclose(x[0], 2.0)))

dofs = fem.locate_dofs_topological(V=V, entity_dim=1, entities=facets)

bc = fem.dirichletbc(value=ScalarType(0), dofs=dofs, V=V)

u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)
x = ufl.SpatialCoordinate(msh)
f = 10 * ufl.exp(-((x[0] - 0.5) ** 2 + (x[1] - 0.5) ** 2) / 0.02)
g = ufl.sin(5 * x[0])
a = inner(grad(u), grad(v)) * dx
L = inner(f, v) * dx + inner(g, v) * ds

problem = fem.petsc.LinearProblem(a, L, bcs=[bc], petsc_options={"ksp_type": "preonly", "pc_type": "lu"})
uh = problem.solve()

unorm = uh.x.norm()
print("Solution vector norm:", unorm)
print('This norm should be equal to 4')

outdir = "out_poisson"

with io.XDMFFile(msh.comm, f"{outdir}/poisson.xdmf", "w") as file:
    file.write_mesh(msh)
    file.write_function(uh)

with io.VTXWriter(msh.comm, f"{outdir}/poisson.bp", [uh]) as vtx:
    vtx.write(0.0)


# %%
# %% 
# This is to check where you run the program
import getpass
import socket

import pyvista
pyvista.OFF_SCREEN = True
from dolfinx import plot
pyvista.start_xvfb()
u_topology, u_cell_types, u_geometry = plot.create_vtk_mesh(V)
u_grid = pyvista.UnstructuredGrid(u_topology, u_cell_types, u_geometry)
u_grid.point_data["u"] = uh.x.array.real
u_grid.set_active_scalars("u")
u_plotter = pyvista.Plotter()
u_plotter.add_mesh(u_grid, show_edges=True)
u_plotter.view_xy()

u_plotter.window_size = (800, 600)
u_plotter.add_text(
    f"Test run by \n {getpass.getuser()} \n on \n {socket.gethostname()}", 
    font_size=10, 
    color="Black", 
    position="upper_edge"
    )

u_plotter.background_color = "white"

if not pyvista.OFF_SCREEN:
    u_plotter.show()
else:
    filename = f"{outdir}/test_poisson.png"
    print("Saving screenshot of mesh to %s" % filename)
    figure = u_plotter.screenshot(filename)

