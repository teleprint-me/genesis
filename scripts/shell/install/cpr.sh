#!/usr/bin/env bash

cd submodules/cpr || (echo "Error: Missing 'submodules/cpr'" && exit)
mkdir -p build
cd build || (echo "Error: Building 'submodules/cpr' failed" && exit)
cmake ..
make
