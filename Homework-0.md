# Preliminary homework: installation

In this class we will use fenicsx, a python library for finite element computations. We will use the version 0.6.0 of fenicsx. 

The goal of this homework is to install fenicsx on your computer and perform a test to check that everything is working fine.

You must have a working installation of fenicsx before the first class. If you have any problem, please contact us in slack.

1. Follows the installation instructions in the file [INSTALL.md](INSTALL.md). You can also find the instructions in the file [INSTALL.pdf](INSTALL.pdf).

2. Install Paraview that you can find at https://www.paraview.org/download/. Paraview is a free open-source software for visualization of 3D data. We will use it to visualize the results of our simulations.

3. Test your installation by running the file `demo_poisson.py` in this folder. You can run the file by typing in a terminal:
    
    ```
    python3 demo_poisson.py
    ```

    If everything is working fine, you will find a png output file `out_poisson/test_poisson.png` and two file that you can visualize with paraview `out_poisson/test_poisson.vtk` in the folder `out_poisson`.

During the first class, we will check that you have a working installation of fenicsx. If you have any problem, please contact us in slack. 