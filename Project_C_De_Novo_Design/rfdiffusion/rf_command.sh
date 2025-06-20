/usr/bin/apptainer run --nv "rf_se3_diffusion.sif" -u run_inference.py \
        inference.deterministic=True \
        diffuser.T=50 \
        inference.output_prefix="../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/rfdiffusion/theozyme_output" \
        inference.input_pdb="../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/theozymes/250618_pdb_with_backbone/arrangement_8a.pdb" \
        contigmap.contigs=['\150-150'\] \
        contigmap.length='150-150'\
        inference.ligand=UNK \
        inference.num_designs=1 \
        inference.design_startnum=0

/usr/bin/apptainer run --nv rf_se3_diffusion.sif -u run_inference.py \
        inference.deterministic=True \
        diffuser.T=50 \
        inference.output_prefix=../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/rfdiffusion/theozyme_output \
        inference.input_pdb=../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/theozymes/250619/gly/arrangement_8.pdb \
        contigmap.contigs=['75,A2,75'] \
        contigmap.length="140-155" \
        inference.ligand=UNK \
        inference.num_designs=1 \
        inference.design_startnum=0


/usr/bin/apptainer run --nv "rf_se3_diffusion.sif" -u run_inference.py \
        inference.deterministic=True \
        diffuser.T=50 \
        inference.output_prefix="../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/rfdiffusion/theozyme_output" \
        inference.input_pdb="../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/theozymes/250618_pdb_with_backbone/arrangement_8.pdb" \
        contigmap.contigs="10-50, A,2, 10-50, A,3, 10-50" \
        contigmap.length='150-150'\
        inference.ligand=UNK \
        inference.num_designs=1 \
        inference.design_startnum=0

HYDRA_FULL_ERROR=1 /usr/bin/apptainer run --nv rf_se3_diffusion.sif -u run_inference.py \
    inference.deterministic=true \
    diffuser.T=50 \
    inference.output_prefix="../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/rfdiffusion/theozyme_output" \
    inference.input_pdb=../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/theozymes/250619/gly/arrangement_8.pdb \
    contigmap.contigs="[\"10-120\", \"A2-2\", \"10-120\", \"A3-3\", \"10-120\"]" \
    contigmap.inpaint_str='["0","2","4"]' \
    contigmap.inpaint_seq='["0","2","4"]'

HYDRA_FULL_ERROR=1 /usr/bin/apptainer run --nv rf_se3_diffusion.sif -u run_inference.py \
        inference.deterministic=True \
        diffuser.T=50 \
        inference.output_prefix=../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/rfdiffusion/theozyme_output \
        inference.input_pdb=../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/theozymes/250619/gly/arrangement_8.pdb \
        contigmap.contigs="[\"10-120\", \"A2-2\", \"10-120\", \"A3-3\", \"10-120\"]" \
        contigmap.inpaint_str=[\'0,2,4\'] \
        contigmap.inpaint_seq=[\'0,2,4\'] \
        inference.ligand=UNK \
        inference.num_designs=1 \
        inference.design_startnum=1

HYDRA_FULL_ERROR=1 /usr/bin/apptainer run --nv rf_se3_diffusion.sif -u run_inference.py \
        inference.deterministic=True \
        diffuser.T=100 \
        inference.output_prefix=../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/rfdiffusion/theozyme_output/arrangement_3_ \
        inference.input_pdb=../GENPENZ_Hackathon_25/Project_C_De_Novo_Design/theozymes/250619/gly/arrangement_3.pdb \
        contigmap.contigs=[\'50-50,A2-2,50-50,A3-3,50-50\'] \
        inference.ligand=UNK \
        inference.num_designs=1 \
        inference.design_startnum=0