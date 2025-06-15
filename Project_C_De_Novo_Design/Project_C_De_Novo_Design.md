# De-Novo Design of a Mandelate Decarboxylase

## Project Goals

- **Objective:** Build a novel enzyme from the ground up, starting with the chemistry of the reaction.
- **Target Reaction:** LMF + Mandelate --> LMF + CO2 + Phenylaldehyde
- **Tools:** : `ORCA` + `RFDiffusion All Atom` + `coTIMED` + `LigandMPNN` 

## Some Background

This project is a but more involved, so we'll start with some background.

For an enzyme to be catalytic, it needs to stabilize (or at least accommodate) the reactions transition state(s). A **theozyme** is a small cluster of side-chains surrounding the key transition state in a pose that stabilizes it. In the case of a multi-step reaction, multiple transition states can be incorporated into the theozyme by superimposing multiple transition state geometries. 

In this project, we will design a theozyme that is unique to the LMF + Mandelate reaction. As `Linus` has already done some QM work on this reaction, we know the rate-limiting transition state. `Marta` has been working on a pipeline to generate theozymes from QM geometries, so we can use these as our starting points.  

Alternatively, we could use the exact arrangement of amino acids that cvFAP has, and try to incorporate this into a *de-novo* design.

## Proposed Methodology

1. **GENERATE THEOZYME:** Use QM calculations to create theozymes, either using `Marta's` combinatorial QM pipeline or from cvFAP itself

2. **DIFFUSE IN A BACKBONE:** Use `RFDiffusion All Atom` to diffuse the theozyme into a backbone scaffold

3. **PLACE THEOZYME IN PROTEIN:** Manually place the theozyme into a protein scaffold

3. **DESIGN SEQUENCE:** Use `coTIMED`, or `ligandMPNN`` to design a sequence for the diffused proteins

4. **SELECT BEST SEQUENCES:** AI methods generate a probability distribution of amino acid identities at each position. We can sample from these distributions to generate final sequences. Depending on how we do this sampling, this can produce a huge library of potential sequences. Out of this large library, we need to narrow down the best candidates. As this task will be relevant to each project, I will discuss it in its own section. 