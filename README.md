# vboxapi

Oracle provides the original Python wrapper that interfaces with VirtualBox's Main API (COM/XPCOM/Web Service). This wrapper (or glue layer) is provided by the VirtualBox SDK. The SDK can be downloaded from here, 'https://www.virtualbox.org/wiki/Downloads'.

## Installation

Currently, the target platform is Linux but other *nix systems may work as well. There are two ways about installing the vboxapi package.

First and the easiest, is to install the source and wheels archive(s).

If the package archive(s) are not a available, then run the following below to install the vboxapi package:

```shell
    git clone https://github.com/cavcrosby/vboxapi
    cd vboxapi
    export POETRY_BIN_PATH=<path to poetry binary>
    export VBOX_INSTALL_PATH=<dir path where virtualbox is installed>
    poetry run python vboxapisetup.py
```

## Installation Notes

- Technically all vboxapisetup.py does now is run a variant of 'poetry install', but some remnants for Mac OSX/Windows support still exist (e.g. VBOX_INSTALL_PATH/VBOX_SDK_PATH is still patched in the vboxapi package \_\_init\_\_.py, but really VBOX_INSTALL_PATH isn't needed for xpcom, VBOX_SDK_PATH still needed for webservice). Support for Windows/Mac OSX may be terminated depending on the scope of the project going forward.

- If using pyenv to manage virtual envs, ensure that the virtual env that this package is installed to has the same \<major\>.\<minor\> Python version as the system Python. The vboxapi package currently loads dynamic libraries that are installed with VirtualBox, the version of dynamic libraries installed is determined by your system's Python.

## License

This code derives from the VirtualBox SDK at the following link, 'https://download.virtualbox.org/virtualbox/6.1.22/VirtualBoxSDK-6.1.22-144080.zip'. That said, the following is performed to ensure proper credit is given where credit is due.
- New changes made will be associated with the type of license specified in 'LICENSE'.
- Any original files will be associated with the license(s) specified within the file.
- Original files that are modified will contain an updated license statement.
