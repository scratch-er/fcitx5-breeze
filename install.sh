#!/bin/sh
if [ "$1" ] ; then
    install_prefix="$1"
else
    install_prefix="/usr/local"
fi
install_dir="$install_prefix"/share/fcitx5/themes
install -Dm 644 ./config/theme_light.conf "$install_dir"/breeze/theme.conf
install -Dm 644 ./build/prev.png "$install_dir"/breeze/prev.png
install -Dm 644 ./build/next.png "$install_dir"/breeze/next.png
install -Dm 644 ./build/arrow.png "$install_dir"/breeze/arrow.png
install -Dm 644 ./build/radio.png "$install_dir"/breeze/radio.png
install -Dm 644 ./build/panel.png "$install_dir"/breeze/panel.png
install -Dm 644 ./build/highlight.png "$install_dir"/breeze/highlight.png
install -Dm 644 ./config/theme_dark.conf "$install_dir"/breeze-dark/theme.conf
install -Dm 644 ./build/panel_dark.png "$install_dir"/breeze-dark/panel.png
install -Dm 644 ./config/theme_light_translucent.conf "$install_dir"/breeze-translucent/theme.conf
install -Dm 644 ./build/panel_light_translucent.png "$install_dir"/breeze-translucent/panel.png
install -Dm 644 ./config/theme_dark_translucent.conf "$install_dir"/breeze-dark-translucent/theme.conf
install -Dm 644 ./build/panel_dark_translucent.png "$install_dir"/breeze-dark-translucent/panel.png
for dirname in breeze-dark breeze-translucent breeze-dark-translucent ; do
    for filename in prev.png next.png arrow.png radio.png highlight.png ; do
        ln -rs "$install_dir"/breeze/$filename "$install_dir"/$dirname/$filename
    done
done

