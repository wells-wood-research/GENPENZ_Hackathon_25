***

<div align="center">
  <img src=".assets/images/wood_lab_logo.png" alt="Wells Wood Research Group Logo" width="200" />
  <h1>Flavo-Mandelate Binder Design Hackathon</h1>
</div>

Hello Everyone, welcome to the GitHub repository for the  **GENPENZ Hackathon 2025**! 

Here you will find all sorts of information on the hackathon, including project descriptions, resources, and instructions for getting started.

---

## 🧑‍💻 Getting Started

Ready to dive in? Here’s your checklist:

1.  **Confirm Your Attendance:** Please let the organizers know you are coming so we can arrange desk space and resources.
2.  **Choose Your Project:** Read the descriptions and let the organizers know your preference.
3.  **Bring your laptop:** We have powerful clusters for you to run calculations, you'll need to bring a laptop to log into these. If you have one, please bring a mouse as well. 
4.  **Get a GitHub Account:** We will be sharing files via [GitHub](https://github.com/), you'll need and account if your don't already have one!
5.  **Download VSCode and WSL:** We do all of our work in `Linux`. On a windows machine, the easiest way to set this up is to use a combination of [VSCode](https://code.visualstudio.com/download) and [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install)

*If you know anyone who was missed on the initial email, please forward this information to them!*



## 🎯 The Grand Challenge

Our collective goal is to push the boundaries of computational protein design. Everyone will be working towards the same high-level objective:

> ### Design a protein that:
> 1.  **Binds a Flavin** (FAD, FMN, or Lumiflavin)
> 2.  **Binds Mandelate** in a potentially catalytic orientation

To tackle this, we have organized into three distinct, synergistic sub-projects. Choose the one that excites you the most!

---

## 🚀 The Projects

Each project leverages a different state-of-the-art methodology to approach our grand challenge. Find a high-level summary below, with full details for each project further down.

| Project | Computational Methods |  Starting Scaffolds  | Key Concept                                                 |
| :------ | :--------------------------| :--------------------------- | :---------------------------------------------------------- |
| **A**   | `RASSCoL` | `Deltaprot` Scaffolds                      | Introduce catalytic activity into Deltaprot scaffolds.    |
| **B**   | `Ligand Docking` + `coTIMED` `ligandMPNN`|  `Natural Flavoproteins`  from the Flavin "79" dataset | Ensure substrate binding in potentially photoactive flavoproteins.|
| **C**   | `Theozyme Design` + `RF-Diffusion`                     | `*De-Novo*` Proteins| Build a novel enzyme from the ground up, starting with chemistry. |


---


### Project A: RASSCoL on Deltaprot Scaffolds

**Objective: Repurpose geometrically elegant scaffolds for new function using rapid sidechain sampling.**

This project aims to expand the capabilities of `RASSCoL` (a rapid method for sampling sidechains in the presence of ligands) from coiled-coils to globular proteins. We'll be using a fascinating library of `Deltaprot` scaffolds, designed by Tadas (UoE). These are compact α-helical bundles with idealized geometries, making them perfect candidates for swapping out entire helices to create new binding pockets.

-   **Core Method:** `RASSCoL`
-   **Target Ligands:** Lumiflavin (LMF) + Mandelate
-   **Scaffolds:** 30 parametrically designed Deltaprots
-   **Background:** Builds on Kasia's successful work designing LMF-binding coiled-coils.
-   **Key Concept:** Deltaprots are *Compact α-helical bundles that can adopt just 30 deltahedral geometries in which helix axes lie along the edges of idealized polyhedra.*

<p align="center">
  <img src=".assets/images/deltaprot_example.png" alt="Image of a Deltaprot structure" width="250" />
  <br>
  <em>A visualization of a Deltaprot scaffold, highlighting its geometric α-helical arrangement.</em>
</p>

---

### Project B: AI-Enhanced Docking into Natural Flavoproteins

**Objective: Introduce a new catalytic activity into existing, highly photoactive flavoproteins.**

This project starts with a unique dataset of 79 natural flavoproteins, curated by Eugene using ML methods. Experimental work by Harry and Junfeng has shown that several of these proteins are highly fluorescent - a metric we are using as a proxy for photoactivity. The missing piece is substrate binding. Your mission is to engineer it.

-   **Core Methods:** Ligand Docking + AI-powered Sequence Design
-   **Target Ligand:** Mandelate
-   **Scaffolds:** The "Flavin 79" Dataset
-   **AI Tools:** `coTIMED` / `ligandMPNN`
-   **Key Concept:** Introduce a mandelate binding site near the native flavin cofactor to create a novel enzyme from a natural, photoactive scaffold.

<p align="center">
  <img src=".assets/images/1VHN_active_site.png" alt="Active site of 1VHN" width="450" />
  <br>
  <em>The active site of protein 1VHN, a flavoprotein from our dataset, showing the bound FMN cofactor.</em>
</p>


For a more detailed discussion of this project, please see the [Project B README](./Project_B_Active_Site_Redesign/Project_B_Active_Site_Redesign.md).

---

### Project C: De Novo Design from First Principles

**Objective: Build a novel enzyme from the ground up, starting with the chemistry of the reaction.**

This project takes a "bottom-up" approach. We begin with a "theozyme"—a precise, geometric arrangement of functional groups needed to stabilize the reaction's transition state. Using QM calculations from Linus and Marta as our guide, we will use generative AI to "hallucinate" protein scaffolds that can perfectly house this catalytic geometry.

-   **Core Methods:** Theozyme placement + Generative Scaffolding + AI Sequence Design
-   **Target Reaction:** LMF + Mandelate
-   **AI Tools:** `RF-Diffusion All Atom`, AI sequence designers
-   **Key Concept:** A theozyme is the minimal catalytic unit of an enzyme. By building a protein around it, we can design for function from first principles.

<p align="center">
  <img src=".assets/images/theozyme_scaffolding.png" alt="Illustration of theozyme-based design" width="800" />
  <br>
  <em>An illustration from the RFDiffusion paper showing a designed protein scaffold built around a functional motif.</em>
</p>

---



## 📚 Resources & Links

-   **Papers:**
    -   [Murzin & Finkelstein (1988) - Deltahedral Geometries](https://www.sciencedirect.com/science/article/pii/002228368890366X)
    -   [RFDiffusion Paper](https://www.biorxiv.org/content/10.1101/2023.10.09.561603v1.full.pdf)
    -   [LigandMPNN Paper](https://www.nature.com/articles/s41592-025-02626-1)
    -   [GNINA paper](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-025-00973-x)
    -   [ORCA Manual](https://www.faccts.de/docs/orca/6.0/manual/)
-   **Tools:**
    -   [GNINA GitHub](https://github.com/gnina/gnina)
    -   [RASSCoL Documentation](link-to-tool)
    -   [RFDiffusion GitHub](https://github.com/baker-laboratory/rf_diffusion_all_atom)
    -   [LigandMPNN GitHub](https://github.com/dauparas/LigandMPNN)

## ❓ Questions?

If you have any questions, please reach out to **Eugene** at eshrimpt@ed.ac.uk!

<hr>

<div align="center">
  <h3>Let's build some amazing proteins! 🎉</h3>
</div>