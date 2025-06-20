INPUT_DIR="../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/theozymes/250619/gly/good"
OUTPUT_DIR="../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/rfdiffusion/theozyme_output_good"

for pdb in "$INPUT_DIR"/*.pdb; do
    name=$(basename "$pdb" .pdb)
    echo "Running RFdiffusion on $name"

    /usr/bin/apptainer run --nv "rf_se3_diffusion.sif" -u run_inference.py \
        inference.deterministic=True \
        diffuser.T=100 \
        inference.output_prefix="$OUTPUT_DIR/$name" \
        inference.input_pdb="$pdb" \
        contigmap.contigs=[\'50-50,A2-2,1-50,A3-3,50-50\'] \
        inference.ligand=UNK \
        inference.num_designs=10 \
        inference.design_startnum=0
done