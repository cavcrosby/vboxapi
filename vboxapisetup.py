"""
Copyright (C) 2009-2021 Oracle Corporation, Conner Crosby

This file is part of VirtualBox Open Source Edition (OSE), as
available from http://www.virtualbox.org. This file is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License (GPL) as published by the Free Software
Foundation, in version 2 as it comes in the "COPYING" file of the
VirtualBox OSE distribution. VirtualBox OSE is distributed in the
hope that it will be useful, but WITHOUT ANY WARRANTY of any kind.

The contents of this file may alternatively be used under the terms
of the Common Development and Distribution License Version 1.0
(CDDL) only, as it comes in the "COPYING.CDDL" file of the
VirtualBox OSE distribution, in which case the provisions of the
CDDL are applicable instead of those of the GPL.

You may elect to license modified versions of this file under the
terms and conditions of either the GPL or the CDDL or both.
"""
# Standard Library Imports
import os
import shutil
import sys
import subprocess
import platform
from distutils.sysconfig import get_python_lib

# Third Party Imports

# Local Application Imports


def cleanupComCache():
    """ """
    comCache1 = os.path.join(get_python_lib(), "win32com", "gen_py")
    comCache2 = os.path.join(os.environ.get("TEMP", "c:\\tmp"), "gen_py")
    print("Cleaning COM cache at", comCache1, "and", comCache2)
    shutil.rmtree(comCache1, True)
    shutil.rmtree(comCache2, True)


def patchWith(f, vboxInstallPath):
    """ """
    newFile = f"{f}-temp"
    vboxInstallPath = vboxInstallPath.replace("\\", "\\\\")
    try:
        os.remove(newFile)
    except:
        pass
    oldFh = open(f, "r")
    newFh = open(newFile, "w")
    for line in oldFh:
        line = line.replace("%VBOX_INSTALL_PATH%", vboxInstallPath)
        line = line.replace(
            "%VBOX_SDK_PATH%", os.environ.get("VBOX_SDK_PATH", default="")
        )
        newFh.write(line)
    newFh.close()
    oldFh.close()
    try:
        os.remove(f)
    except:
        pass
    os.rename(newFile, f)


def main(argv):
    """ """
    if platform.system() == "Windows":
        cleanupComCache()

    vboxInstallPath = os.environ.get("VBOX_INSTALL_PATH", None)
    poetryBinPath = os.environ.get("POETRY_BIN_PATH", None)
    if vboxInstallPath is None:
        raise Exception("No VBOX_INSTALL_PATH defined, exiting")
    if poetryBinPath is None:
        raise Exception("No POETRY_BIN_PATH defined, exiting")
    patchWith(
        os.path.join(os.getcwd(), "vboxapi", "__init__.py"),
        vboxInstallPath,
    )
    subprocess.run(
        [poetryBinPath, "install"],
    )


if __name__ == "__main__":
    main(sys.argv)
