python run.py \
        --model_type "ligand_mpnn" \
        --pdb_path "../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/rfdiffusion/theozyme_output_good/arrangement_10/arrangement_10_7.pdb" \
        --out_folder "../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/ligandmpnn/arrangement10_7" \
        --fixed_residues "A51 A62" \
        --batch_size 5 \
        --number_of_batches 10
