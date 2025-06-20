import argparse
import os

def generate_mutated_wt_fasta(wt_fasta_path, hotspot_path, timed_fasta_path, output_fasta_path):
    """
    Generates a FASTA file by applying mutations from a timed_fasta to a WT_sequence,
    but only at specified hotspot positions.

    Args:
        wt_fasta_path (str): Path to the FASTA file containing the wild-type sequence
                             (expected to have one sequence after the first header).
        hotspot_path (str): Path to a text file containing comma-separated, 1-based
                            hotspot positions.
        timed_fasta_path (str): Path to the input FASTA file with mutated sequences
                                (e.g., from CoTIMED).
        output_fasta_path (str): Path where the generated FASTA file will be saved.
    """
    try:
        with open(wt_fasta_path, 'r') as f_wt:
            wt_lines = f_wt.readlines()
            if len(wt_lines) < 2:
                raise ValueError(f"WT FASTA file '{wt_fasta_path}' must have at least a header and a sequence.")
            WT_seq = wt_lines[1].strip()
    except FileNotFoundError:
        print(f"Error: Wild-type FASTA file not found at '{wt_fasta_path}'")
        return
    except Exception as e:
        print(f"Error reading WT FASTA file '{wt_fasta_path}': {e}")
        return

    try:
        with open(hotspot_path, 'r') as f_hotspot:
            hotspot_str = f_hotspot.read().strip()
            if not hotspot_str:
                print(f"Warning: Hotspot file '{hotspot_path}' is empty. No mutations will be applied from hotspots.")
                hotspots_0based = []
            else:
                # Convert 1-based hotspot strings to 0-based integers
                hotspots_0based = [int(spot.strip()) - 1 for spot in hotspot_str.split(',') if spot.strip()]
    except FileNotFoundError:
        print(f"Error: Hotspot file not found at '{hotspot_path}'")
        return
    except ValueError:
        print(f"Error: Hotspot file '{hotspot_path}' contains non-integer values or is improperly formatted.")
        return
    except Exception as e:
        print(f"Error reading hotspot file '{hotspot_path}': {e}")
        return

    try:
        with open(timed_fasta_path, 'r') as timed_fasta_file, \
             open(output_fasta_path, 'w') as mut_WT_file:

            for idx, line in enumerate(timed_fasta_file):
                if idx % 2 == 0:  # Header line
                    mut_WT_file.write(line)
                else:  # Sequence line
                    timed_seq_list = list(line.strip())
                    final_seq_list = list(WT_seq) # Start with a fresh WT sequence

                    if not timed_seq_list:
                        print(f"Warning: Empty sequence found in '{timed_fasta_path}' at line {idx+1}. Skipping.")
                        mut_WT_file.write("\n") # Write an empty sequence line to maintain FASTA structure
                        continue

                    for spot_0based in hotspots_0based:
                        if 0 <= spot_0based < len(WT_seq) and 0 <= spot_0based < len(timed_seq_list):
                            final_seq_list[spot_0based] = timed_seq_list[spot_0based]
                        else:
                            print(f"Warning: Hotspot position {spot_0based + 1} is out of bounds "
                                  f"for WT_seq (len {len(WT_seq)}) or timed_seq (len {len(timed_seq_list)}). Skipping this hotspot.")
                    
                    mut_WT_file.write(f"{''.join(final_seq_list)}\n")
        
        print(f"Successfully generated mutated FASTA: '{output_fasta_path}'")

    except FileNotFoundError:
        print(f"Error: Timed FASTA file not found at '{timed_fasta_path}'")
    except IOError as e:
        print(f"Error during file operations: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generates a mutated FASTA file by applying mutations from a 'timed' FASTA "
                    "to a wild-type sequence, specifically at given hotspot locations."
    )
    
    parser.add_argument(
        "--wt_fasta", 
        required=True, 
        help="Path to the FASTA file containing the wild-type sequence (e.g., dataset.fasta)."
    )
    parser.add_argument(
        "--hotspots", 
        required=True, 
        help="Path to the text file containing comma-separated, 1-based hotspot positions (e.g., hotspot.txt)."
    )
    parser.add_argument(
        "--timed_fasta", 
        required=True, 
        help="Path to the input FASTA file with mutated sequences (e.g., CoTIMED_temp_0.5_n_10_DESIGN.fasta)."
    )
    parser.add_argument(
        "--output_fasta", 
        required=True, 
        help="Path for the generated output FASTA file (e.g., b5ininn_W25A_W45A_ADD_mut.fasta)."
    )
    # Optional arguments if you still want to use input_dir, output_dir, design to construct paths
    # parser.add_argument("--input_dir", default=".", help="Directory for input files.")
    # parser.add_argument("--output_dir", default=".", help="Directory for output files.")
    # parser.add_argument("--design", help="Design identifier, used for constructing some default filenames if full paths are not given.")


    args = parser.parse_args()

    # --- Example of how you might use input_dir, output_dir, design if you prefer that ---
    # This part is commented out because the primary arguments above ask for full paths, which is generally better.
    # If you wanted to reconstruct paths as in the original script:
    #
    # design_name = args.design if args.design else "default_design" # Fallback if --design not given
    #
    # wt_fasta_path = os.path.join(args.input_dir, "dataset.fasta")
    # hotspot_path = os.path.join(args.input_dir, "hotspot.txt")
    # # Constructing timed_fasta_path might be more complex if its name pattern varies
    # # For the specific pattern in your original script:
    # timed_fasta_filename = f"CoTIMED_temp_0.5_n_10_{design_name}.fasta"
    # timed_fasta_path = os.path.join(args.input_dir, timed_fasta_filename)
    #
    # output_fasta_filename = f"{design_name}.fasta" # Or a more descriptive name
    # output_fasta_path = os.path.join(args.output_dir, output_fasta_filename)
    #
    # # Then call the function:
    # generate_mutated_wt_fasta(wt_fasta_path, hotspot_path, timed_fasta_path, output_fasta_path)
    # --- End of example ---

    # Call the main function with the parsed arguments (assuming full paths are provided)
    generate_mutated_wt_fasta(
        args.wt_fasta,
        args.hotspots,
        args.timed_fasta,
        args.output_fasta
    )