# How to install FEniCS

## On Linux and Macosx using Anaconda

Instructions on how to install FEniCS-dolfinx are available at https://fenicsproject.org/download/.

We suggest and support the installation method using anaconda. Anaconda is a useful package manager for python.

The following install instruction work only on Linux on Macosx. If you have Windows, see below.

1. Install Anaconda:
   - Go to https://www.anaconda.com/download#downloads.
   - If you are on macOS and have an M1/M2 processor, be sure to download the M1 version of Anaconda.

2. Download the present repository in your computer either by using git (`git clone https://github.com/msolides-2023/MU5MES01-2023.git`) or by downloading a zip version: `https://github.com/msolides-2023/MU5MES01-2023/archive/refs/heads/main.zip`.

2. Open a new terminal and go to the directory containing the file `fenicsx-0.6.0.yaml`. You will find this file in the present git repository, downloaded at the previous step.

3. You should now be in the `base` environment and your command prompt should show `(base)`. Make sure to use the updated version of the package and avoid conflicts.
    ```
    conda update -n base -c defaults conda
    ```

4. Create a new conda environment from the file `fenicsx-0.6.0.yaml`. This will install the major required packages for the course. You can read the file `fenicsx-0.6.0.yaml` to see which packages are installed. The installation can take a few minutes.
The ``--force`` option is used to overwrite an existing environment with the same name.
    ```
    conda env create --file fenicsx-0.6.0.yml --force
    ```

5. Install the xserver. This is required to run the graphical interface of pyvista.
    - On Linux, assuming that you are using a Debian-based distribution (e.g. Ubuntu), run the following command:
        ```
        sudo apt-get update
        sudo apt-get install libgl1-mesa-glx xvfb
        ```
    - On macOS:
        - Install XQuartz by downloading and running the installer from the XQuartz website at https://www.xquartz.org/.
        - Install the xorg-xserver package by running the following command in a terminal window with the fenicsx-0.6.0 activated :
        ```
        conda install -c conda-forge xorg-xserver
        ```

6. Congratulations, you have successfully installed FEniCS in the Conda environment `fenicsx-0.6.0`. To use it, you must activate the environment by running the following command in a terminal window:

    ```
    conda activate fenicsx-0.6.0
    ``` 

This will activate the environment and allow you to use the packages that were installed in it, including FEniCS. Note that activating an environment only affects the current terminal session. If you open a new terminal window, you will need to activate the environment again.

After the first installation, you only need to run step 5 above (`conda activate fenicsx-0.6.0`) to use FEniCS in a terminal.

For further help on Conda, you can refer to the [Conda cheatsheet](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf).

## On Windows

FEniCS is not distributed for Windows boxes. For Windows 10, the preferred option is the [Windows subsystem for linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install).
Install the Ubuntu distribution as WSL, then refer to the section above inside the Ubuntu WSL.

As an alterative you can use Docker or a cloud-based solution.

## Cloud-based  Google colab installations
You can run python programs jupyter notebooks and FEniCS on online servers. The basic service is free and can be a solution if all other installation systems fail.

* You need a google account
* You can use this example to start https://fem-on-colab.github.io/packages.html 
* You can save the notebooks and your working environment on your google drive

We suggest to use this only as emergency solution
* *advantages:* You do not need to install anything on your machine and you do note use the resources of your machine

* *disadvantages:* It can be slow. You can use only jupyter notebooks, you share your data with google or microsoft, you do not a full control of the system, you need to be online with a good network connection.

## How to test the installation

Run following commands in your terminal:

```
python3 demo_poisson.py
```
or copy and paste this code in the notebook and exectute the cell

# Editor

We suggest to use VSCode as editor. It is free and open source. It is available for Linux, Macosx and Windows. It is a very good editor for python and it has a very good integration with git. You can find it here: https://code.visualstudio.com/


# Troubleshooting

If conda installation of the fenicsx-0.6.0 environment takes too long, interrupt the process and try with `mamba`:
1. Install mamba: 
```
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```
2. Open a new terminal and use `mamba` to install instead of `conda``: 
```
mamba env create --file fenicsx-0.6.0.yml
```
Hence always use `mamba` instead of `conda` to install packages in the environment.