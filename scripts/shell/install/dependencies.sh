#!/usr/bin/env bash

# Update the distribution detection method using /etc/os-release
source /etc/os-release
declare -r DISTRO=$ID

# Set package manager, package names, and install flag based on the distribution
if [[ $DISTRO == "debian" || $DISTRO == "ubuntu" ]]; 
	then
		declare -r PACKAGE_MANAGER="apt"
		declare -r INSTALL_FLAG="install"
elif [[ $DISTRO == "arch" || $DISTRO == "endeavouros" || $DISTRO == "manjaro" ]]; 
	then
		declare -r PACKAGE_MANAGER="pacman"
		declare -r INSTALL_FLAG="-S"
else
	echo "Error: Unsupported distribution. Exiting now."
	exit 1
fi

# Prompt the user for their display server choice
echo "Select the display server you are using:"
echo "1. Wayland"
echo "2. X11"
echo "3. Skip glfw and glew installation"
read -rp "Enter the number (1, 2, or 3): " choice

# Install the dependencies based on the user's choice
case "$choice" in
	1)
		echo "Installing dependencies for Wayland."
		if [[ $DISTRO == "debian" || $DISTRO == "ubuntu" ]]; then
			GLFW_PACKAGE_NAME="libglfw3"
			GLEW_PACKAGE_NAME="libglew-dev"
		else
			GLFW_PACKAGE_NAME="glfw-wayland"
			GLEW_PACKAGE_NAME="glew"
		fi
		;;
	2)
		echo "Installing dependencies for X11."
		if [[ $DISTRO == "debian" || $DISTRO == "ubuntu" ]]; then
			GLFW_PACKAGE_NAME="libglfw3"
			GLEW_PACKAGE_NAME="libglew-dev"
		else
			GLFW_PACKAGE_NAME="glfw-x11"
			GLEW_PACKAGE_NAME="glew"
		fi
		;;
	3)
		echo "Skipping glfw-<compositor>..."
		echo "WARN: glfw and glew are required dependencies!"
		;;
	*)
		echo "Error: Unknown option given. Exiting now."
		exit 1
		;;
esac

if [[ "$choice" == "1" || "$choice" == "2" ]]; then
	sudo "$PACKAGE_MANAGER" "$INSTALL_FLAG" "$GLFW_PACKAGE_NAME" "$GLEW_PACKAGE_NAME" -y
fi

# Set the CURL_PACKAGE_NAME based on the distribution
if [[ $DISTRO == "debian" || $DISTRO == "ubuntu" ]]; then
	CURL_PACKAGE_NAME="libcurl4-gnutls-dev"
else
	CURL_PACKAGE_NAME="libcurl-gnutls"
fi

# Add the '-y' flag to the CURL package installation
sudo "$PACKAGE_MANAGER" "$INSTALL_FLAG" "$CURL_PACKAGE_NAME" -y
