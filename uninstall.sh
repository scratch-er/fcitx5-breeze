#!/bin/sh
if [ "$1" ] ; then
    install_prefix="$1"
else
    install_prefix="/usr/local"
fi
install_dir="$install_prefix"/share/fcitx5/themes

rm -r "$install_dir"/breeze*

