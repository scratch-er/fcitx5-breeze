#!/bin/sh
if [ "$1" ] ; then
    install_prefix="$1"
else
    install_prefix="/usr/local"
fi
install_dir="$install_prefix"/share/fcitx5/themes

if [ ! -e $install_dir ] ; then
    mkdir $install_dir
fi

for i in $(ls build) ; do
    chmod 644 "build/${i}"/*
done

cp -rf --no-preserve=ownership --preserve=mode build/* $install_dir
