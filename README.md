# OverlayEditor

This application edits [X-Plane](http://www.x-plane.com/) DSF "overlay" scenery packages for X-Plane 8.30 or later.
It runs on Windows 2000 or later, MacOS 10.5 or later and Linux.

The application allows you to place 3D objects, building facades, draped textures, roads and other kinds of scenery objects on top of X-Plane's terrain. The application does not edit X-Plane airport layouts (_i.e._ runways, taxiways and navaids) and does not edit X-Plane's terrain mesh, but it does read and display both of these in simplified form so you can see where you're placing your objects.

## Building

### Prerequisites

Using the system Python means that native Mac OS packages are included in the built app.  This can cause problems as these packages on the Mac doing the build may be compiled to take advantage of hardware features on that specific Mac.  The [PyInstaller docs](https://pyinstaller.readthedocs.io/en/v3.4/installation.html#installing-in-mac-os-x) recommend using a package manager such as [HomeBrew](https://brew.sh/) to avoid these types of problems, but that doesn't work.

So, the only option to get it working was to build on a machine with an older architecture.  This is obviously far from ideal.

Prerequisites for wxPython and numpy (nothing works without these), 7z (essential for working with X-Plane 10's compressed DSFs), requests (for HTTP support), OpenGL (essential), AppKit (not sure what this is for, but there's an import error if it's not included) and pyinstaller for building the package.

Note: numpy version fixed at 1.15.4 due to https://github.com/pyinstaller/pyinstaller/issues/3982 until pyinstaller is patched

Note: On the Mac, AppKit may complain about various missing packages (such as `glib`, `gobject-introspection` etc.) so just brew install these.  The only one causing trouble was `libffi`, but setting the `PKG_CONFIG_PATH` as per https://stackoverflow.com/questions/22875270/error-installing-bcrypt-with-pip-on-os-x-cant-find-ffi-h-libffi-is-installed/25854749#25854749 fixed this.

```bash
$ pip install numpy==1.15.4
$ pip install wxPython
$ pip install PyLZMA
$ pip install requests
$ pip install PyOpenGL PyOpenGL_accelerate
$ pip install AppKit
$ pip install pyinstaller
```

### Using pyinstaller

Only tested on Mac so far. Uses pyinstaller to package, which in turn uses the `OverlayEditor-Mac.spec` specification file.

Edit `OverlayEditor-Mac.spec` and `version.py` and insert desired version number in both (the `version.py` version is only used when naming the zip when using pyinstaller).

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
