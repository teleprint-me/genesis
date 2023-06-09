# Genesis

Genesis is a versatile user interface for creating, training, and interacting with AI models. The primary focus is on providing an easy-to-use environment for developers and users to work with various AI models and interact with them through an intuitive interface powered by ImGui.

This project is in its infancy and has a long development journey ahead. I appreciate your support, suggestions, and contributions as I continue to develop Genesis.

Note: This project and its contents were created with the assistance of OpenAI's GPT-3.5 and GPT-4.

## Features

-   Develop models from scratch
-   Train models from scratch
-   Manage datasets
-   Run inference on locally trained models (CPU or GPU)
-   Access external AI libraries and frameworks
-   Simplified interactions with AI models through an intuitive ImGui-based user interface
-   Support for integrating Python through ctypes

## Getting Started

### Prerequisites

To use Genesis, you'll need the following prerequisites:

-   Arch Linux (other platforms may work but are not officially supported at this time)
-   C, C++, and Python development tools
-   ImGui library

To install the necessary dependencies, follow these steps:

1.  Install the C, C++, and Python development tools:

    -   On Arch Linux, you can use the package manager to install the necessary tools. Run the following command:

        ```sh
        # Base dependencies
        sudo pacman -S gcc gdb make cmake python-pip
        # Use `glfw-x11` for X11.
        # Use `glfw-wayland` for Wayland.
        sudo pacman -S glfw-wayland glew
        # Curl dependency
        sudo pacman -S libcurl-gnutls
        ```

        For other platforms, refer to the respective library/package documentation for installation instructions.

2.  Optional: Set up the Python development environment:

    -   Run the following commands to install the required Python packages using Poetry, a Python dependency management tool:

        ```sh
        pip install --user pipx
        pipx install poetry
        poetry install
        poetry shell
        ```

    This will set up a virtual environment and install the necessary Python packages for Genesis.

3.  Install the ImGui library:

    -   If you are using submodules, ensure that the ImGui submodule is properly initialized and updated in your project. If it is not, run the following command to initialize and update the submodules:

        ```sh
        git submodule update --init
        ```

    -   Once the submodules are initialized and updated, you can proceed to build and install the ImGui library according to the instructions provided in the submodule's documentation.

        It is recommended to refer to the specific ImGui submodule's documentation for detailed instructions on building and installing the library.

Make sure all the prerequisites are properly installed before proceeding with the installation and usage of Genesis.

### Building

To build Genesis, follow these steps:

1. Build the CPR library:

    To build the CPR library, perform the following:

    ```sh
    cd submodules/cpr
    mkdir -p build
    cd build
    cmake ..
    make
    ```

    This will compile the CPR library required by Genesis.

2. Build Genesis:

    To build Genesis, execute the following command in the project root directory:

    ```sh
    make
    ```

    This command compiles the source code and generates the Genesis binary.

Ensure that you have the necessary prerequisites installed and handle any errors or missing dependencies that may arise during the build process.

### Scripts

Helper scripts are provided in the `scripts/shell/install` directory to assist with installing the required dependencies, setting up the Python development environment, and building the CPR library.

1. Run `dependencies.sh` to install the necessary C, C++, and Python development tools and libraries.
2. Run `python_dev.sh` to set up the Python development environment using Poetry.
3. Run `cpr.sh` to build the CPR library.

After running these scripts, proceed to build Genesis by executing the following command in the project root directory:

```sh
make
```

This command compiles the source code and generates the Genesis binary.

Ensure that you have the necessary prerequisites installed and handle any errors or missing dependencies that may arise during the build process.

### Setting up the Environment File

Genesis requires an environment file, `.env`, in the project root directory to store sensitive information, such as the `OPENAI_API_KEY`.

To create the `.env` file, follow these steps:

1. In the project root directory, create a new file named `.env`.
2. Open the `.env` file with your preferred text editor.
3. Add the required environment variables in the following format:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

    Replace `your_openai_api_key` with your actual API key.

Save the `.env` file and close your text editor. The `run.sh` script will automatically source the `.env` file and set up the necessary environment variables when executed.

Note: This is a temporary solution.

### Running Genesis

To run Genesis, execute the `run.sh` script in the project root directory:

```sh
./run.sh
```

This script will build Genesis, source the `.env` file, and set up the necessary environment variables before running the Genesis binary.

Ensure that you have the necessary prerequisites installed, the `.env` file is properly set up, and handle any errors or missing dependencies that may arise during the build process.

### Installation

_TODO: Add installation instructions_

## Development

Genesis is built using ImGui, a powerful C++ GUI framework. As you work on the project, please ensure that you:

-   Keep the GUI and core functionality separate for easier unit testing
-   Write unit tests for non-GUI components
-   Test the GUI-specific parts manually or with a dedicated GUI testing framework if necessary

_TODO: Add more development guidelines and instructions_

## Contributing

I welcome contributions from the community! To get started, please read our [Contribution Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md). These documents provide essential information on issue reporting, pull requests, code style, and other guidelines for contributing to the project.

## License

This project is licensed under the GNU General Public License v3.0 (GPLv3) - see the [LICENSE](LICENSE) file for details.

    Genesis - An AI model interaction and development tool
    Copyright (C) 2023 teleprint-me

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.

## Acknowledgements

_TODO: Add acknowledgements for any resources or tools used in the project_
