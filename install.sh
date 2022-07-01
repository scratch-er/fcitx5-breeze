#!/bin/sh
if [ "$1" ] ; then
    install_prefix="$1"
else
    install_prefix="/usr/local"
fi
install_dir="$install_prefix"/share/fcitx5/themes

chmod -R 644 build
cp -rf --no-preserve=ownership --preserve=mode build/* $install_dir
