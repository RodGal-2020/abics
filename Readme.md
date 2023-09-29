Auckland Bioengineering Institute Comfort Simulator (ABICS)
===========================================================

The Auckland Bioengineering Institute (ABI) Comfort Simulator (CS) is a user friendly, free, open-source, `python` based tool that enables the simulation of thermoregulation on realistic human geometries for various environmental, body constitution and metabolic activity levels.
A user manual describing the features of the tool, outlining the steps to setup an experiment, simulate, and visualize it is available in the docs folder.

Installation
-------------

The code is compatible with `python` 3.6 or higher, but due to the requirements by `opencmisszinc` it now works only with 3.9 or higher. The tool relies on dependencies which are expected to be available in the host `python` environment (both the client and the server).
Current opencmisszinc release requires `python` 3.9, so a `python` 3.9 or higher environment is required.

Install `python` v 3.9 or higher
-------------

You may use an existing `python` distribution, ensure the packages are installed through appropriate installers.

Install dependencies
-------------

Below are the commands for installing dependencies in an anaconda based environment.

```sh
conda install pyqt=5 scipy
conda install -c jmcmurray json
# Alternative as `json` is no longer available for Python 3.9+
conda install -c conda-forge diskcache pyqtgraph sqlitedict pyzmq
# In order to use the required `sip` module
pip3 install lxml
pip install pyqt6-sip
```

Install/Link with opencmiss-zinc
-------------

Install opencmiss zinc library from pypi is no longer available with `pip install opencmiss.zinc`, so we get it directly from source, for the version we are using of `Python`, in this case **3.10**.

```sh
# pip install opencmiss.zinc
# It is no longer available, so we get it from source for python 3.10:
wget https://github.com/cmlibs/zinc/releases/download/v4.0.2/cmlibs.zinc-4.0.2-cp310-cp310-linux_x86_64.whl
pip install cmlibs.zinc-4.0.2-cp310-cp310-linux_x86_64.whl
```

Launching the tool
------------------

The tool can be launched from the commandline using the script abics.bat (.sh) on Windows(Linux).

Launching the server
--------------------

The server can be launched using the script server.bat (.sh) on Windows(Linux). The default portno is 5570, to change the port number the script should be edited and the port number should be passed as on option "-p pornt_number".

Saving the environment
--------------------

```sh
conda env export > abics_env.yml
```
