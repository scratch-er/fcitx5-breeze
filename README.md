# Fcitx5-breeze
Fcitx5 theme to match KDE's Breeze style.

For Arch Linux users, this theme is available on the AUR as `fcitx5-breeze`.

## Build

Run `bulid.sh` to build this theme. You need to have inkscape installed.

This themes uses svg as the source format. However, in fcitx5 themes, png images are used.

## Installation

To install this theme, you need to build it first or get a pre-built package from the [releases page](https://github.com/scratch-er/fcitx5-breeze/releases).

Run `install.sh`. By default, this will install the theme into `/usr/local`.

```shell
sudo ./install.sh
```

To specify another installation prefix, for example, if you want install this theme into `/usr`.

```shell
sudo ./install.sh /usr
```

If you want to install this theme only for yourself without root privilege, you need to set installation prefix to `~/.local`.

```shell
./install.sh ~/.local
```

To uninstall this theme, run `./uninstall.sh <installation-prefix>`, for example:

```shell
./uninstall.sh ~/.local
```



## Acknowledgements

This theme is based on the default Fcitx5 theme and Breeze Plasma theme.

