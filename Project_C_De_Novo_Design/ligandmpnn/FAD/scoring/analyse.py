import torch
import numpy as np

print(torch.__version__)

amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 
               'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']


file = "/home/GENPENZ_ai/GENPENZ_Hackathon_25/Project_C_De_Novo_Design/ligandmpnn/FAD/scoring/FAD_0.pt"

# Load the .pt file
data = torch.load(file, weights_only=False)

# Inspect the contents
print("Data keys:")
print(data.keys())
print()

probs = data['probs']
print("Shape of data probabilities:")
print(probs.shape)  # e.g., [100, 20] for a 100-residue protein
print()

# Compute average probabilities across batches
if isinstance(probs, np.ndarray):
    # If probs is a NumPy array, use np.mean
    avg_probs = np.mean(probs, axis=0)  # Shape: [248, 21]
else:
    # If probs is a PyTorch tensor, use torch.mean
    avg_probs = torch.mean(probs, dim=0)  # Shape: [248, 21]
most_likely_aa = [amino_acids[np.argmax(avg_probs[i])] for i in range(avg_probs.shape[0])]
print("Consensus sequence:", ''.join(most_likely_aa))
