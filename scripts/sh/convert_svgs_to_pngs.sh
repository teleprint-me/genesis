#!/usr/bin/bash

# Get the input directory from the first argument or use the default
input_dir="${1:-assets/boxicons-2.1.4/svg/solid}"
output_dir="assets/boxicons-2.1.4/png/solid"

# Create the output directory if it doesn't exist
mkdir -p "${output_dir}"

# Find all SVG files in the input directory and its subdirectories
find "${input_dir}" -type f -iname '*.svg' | while read -r svg_file; do
  # Replace the input directory path with the output directory path
  png_file="${svg_file/$input_dir/$output_dir}"

  # Replace the .svg extension with .png
  png_file="${png_file%.svg}.png"

  # Create the output file's directory if it doesn't exist
  mkdir -p "$(dirname "${png_file}")"

  # Convert the SVG file to a PNG file
  convert "${svg_file}" "${png_file}"
done

echo "SVG to PNG conversion completed."
