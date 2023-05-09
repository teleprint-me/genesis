#!/usr/bin/env bash

echo "Select the display server you are using:"
echo "1. Wayland"
echo "2. X11 (default)"
read -rp "Enter the number (1 or 2): " choice

case "$choice" in
  1)
    echo "Installing dependencies for Wayland."
    sudo pacman -S glfw-wayland glew
    ;;
  2|*)
    echo "Installing dependencies for X11."
    sudo pacman -S glfw-x11 glew
    ;;
esac

sudo pacman -S 	libcurl-gnutls