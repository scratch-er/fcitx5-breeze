#!/bin/sh
if [ "$1" ] ; then
    install_prefix="$1"
else
    install_prefix="/usr/local"
fi
install_dir="$install_prefix"/share/fcitx5/themes
for dirname in breeze breeze-dark breeze-translucent breeze-dark-translucent ; do
    rm -r "$install_dir"/$dirname
done

