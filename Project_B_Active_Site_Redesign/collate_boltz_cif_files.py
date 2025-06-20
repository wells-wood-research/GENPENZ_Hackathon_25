#!/usr/bin/env python3

import os
import shutil
import pathlib
import argparse

# Note: TARGET_FILE_SUFFIX and BOLTZ_DIR_PREFIX are fixed as per the request
# and are defined in the `if __name__ == "__main__":` block.

def collate_files(base_search_dir_arg: str,
                  output_dir_specifier_arg: str,
                  target_suffix_arg: str,
                  boltz_prefix_arg: str):
    """
    Finds specific .cif files based on a suffix, within subdirectories matching a prefix,
    under a base search directory, and copies them to a new output directory.

    Args:
        base_search_dir_arg (str): Path to the base directory to search within.
                                   Supports '~' for home directory.
        output_dir_specifier_arg (str): Name or path for the output directory.
                                   Supports '~' for home directory. If a relative path,
                                   it's created relative to the resolved base_search_dir_arg.
                                   If an absolute path, it's used directly.
        target_suffix_arg (str): Suffix of the files to find (e.g., "_model_0.cif").
        boltz_prefix_arg (str): Prefix for subdirectories to search within (e.g., "boltz").
    """
    base_path = pathlib.Path(base_search_dir_arg).expanduser().resolve()

    # Determine the final output path
    # Expand user for output_dir_specifier_arg first, in case it uses '~'
    output_specifier_path = pathlib.Path(output_dir_specifier_arg).expanduser()

    if output_specifier_path.is_absolute():
        output_path = output_specifier_path.resolve()
    else:
        # If relative, it's joined with the resolved base_path
        output_path = (base_path / output_specifier_path).resolve()

    if not base_path.is_dir():
        print(f"Error: Base search directory not found: {base_path}")
        return

    # Create the output directory if it doesn't exist
    try:
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"Output directory created/ensured: {output_path}")
    except OSError as e:
        print(f"Error: Could not create output directory {output_path}: {e}")
        return

    found_files_count = 0
    copied_files_count = 0

    print(f"\nSearching in: {base_path}")
    print(f"Looking for directories starting with: '{boltz_prefix_arg}'")
    print(f"Looking for files ending with: '{target_suffix_arg}'")
    print("-" * 30)

    # 1. Find directories starting with boltz_prefix_arg
    for item in base_path.iterdir():
        if item.is_dir() and item.name.startswith(boltz_prefix_arg):
            current_boltz_dir = item
            print(f"\nSearching in boltz directory: {current_boltz_dir.name}")

            # 2. Recursively search for target files within this boltz directory
            # The pattern '*_model_0.cif' will find files like 'anything_model_0.cif'
            for cif_file in current_boltz_dir.rglob(f"*{target_suffix_arg}"):
                if cif_file.is_file(): # Ensure it's a file, not a dir matching the pattern
                    found_files_count += 1
                    destination_file = output_path / cif_file.name
                    print(f"  Found: {cif_file}")

                    try:
                        # Copy the file, preserving metadata if possible
                        shutil.copy2(cif_file, destination_file)
                        print(f"    Copied to: {destination_file}")
                        copied_files_count += 1
                    except shutil.SameFileError:
                        print(f"    Skipped (source and destination are the same): {cif_file}")
                    except OSError as e:
                        print(f"    Error copying {cif_file} to {destination_file}: {e}")

    print("-" * 30)
    print(f"\nSummary:")
    print(f"  Total potential files found: {found_files_count}")
    print(f"  Total files successfully copied: {copied_files_count}")
    print(f"  Files are located in: {output_path}")

if __name__ == "__main__":
    # --- Fixed Configuration (not exposed as CLI arguments as per request) ---
    FIXED_TARGET_FILE_SUFFIX = "_model_0.cif"
    FIXED_BOLTZ_DIR_PREFIX = "boltz"

    parser = argparse.ArgumentParser(
        description=(
            "Collates specific .cif files into a new output directory. "
            f"It searches for files ending with '{FIXED_TARGET_FILE_SUFFIX}' "
            f"within subdirectories starting with '{FIXED_BOLTZ_DIR_PREFIX}' "
            "under the specified base search directory."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter # Shows default values in help
    )
    parser.add_argument(
        "base_search_dir",
        type=str,
        help="The base directory to search within (e.g., /home/user/data/, or ./my_data). "
             "Supports '~' for home directory. Subdirectories matching the boltz prefix "
             f"'{FIXED_BOLTZ_DIR_PREFIX}' are expected here."
    )
    parser.add_argument(
        "-o", "--output-dir",
        dest="output_dir_specifier", # Argument will be stored in args.output_dir_specifier
        type=str,
        default="collated_cif_models",
        help="Path for the output directory. Supports '~' for home directory. "
             "If a relative path (e.g., 'my_output'), it's created relative to 'base_search_dir'. "
             "If an absolute path (e.g., '/tmp/my_output' or '~/my_output_folder'), it's used directly. "
             "(default: '%(default)s')"
    )

    args = parser.parse_args()

    collate_files(
        args.base_search_dir,
        args.output_dir_specifier,
        FIXED_TARGET_FILE_SUFFIX,
        FIXED_BOLTZ_DIR_PREFIX
    )