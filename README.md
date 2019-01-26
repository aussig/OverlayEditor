# OverlayEditor

This application edits [X-Plane](http://www.x-plane.com/) DSF "overlay" scenery packages for X-Plane 8.30 or later.
It runs on Windows 2000 or later, MacOS 10.5 or later and Linux.

The application allows you to place 3D objects, building facades, draped textures, roads and other kinds of scenery objects on top of X-Plane's terrain. The application does not edit X-Plane airport layouts (_i.e._ runways, taxiways and navaids) and does not edit X-Plane's terrain mesh, but it does read and display both of these in simplified form so you can see where you're placing your objects.

## Building

### Prerequisites

Using the system Python means that native Mac OS packages are included in the built app.  This can cause problems as these packages on the Mac doing the build may be compiled to take advantage of hardware features on that specific Mac.  The [PyInstaller docs](https://pyinstaller.readthedocs.io/en/v3.4/installation.html#installing-in-mac-os-x) recommend using a package manager such as [HomeBrew](https://brew.sh/) to avoid these types of problems, but that doesn't work.

So, the only option to get it working was to download and install [ActivePython v2.7.14](https://www.activestate.com/products/activepython/). Note that this overwrites all the python symlinks in `/usr/loca/bin` (and also creates them as root). Also note that as ActivePython is installed into `/Library/Frameworks/Python.framework/`, the `pip install` commands below will likely need to be run using `sudo`.

Prerequisites for wxPython (nothing works without this), 7z (essential for working with X-Plane 10's compressed DSFs), OpenGL (not essential, but important) and pyinstaller for building the package:

```bash
$ pip install wxPython
$ pip install PyLZMA
$ pip install PyOpenGL PyOpenGL_accelerate
$ pip install pyinstaller
```

### Using pyinstaller

Only tested on Mac so far. Uses pyinstaller to package, which in turn uses the `OverlayEditor-Mac.spec` specification file.

```bash
$ MacOS/setup
```


## License

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
