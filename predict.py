import argparse
import json
from dar_model import dar

with open("fitted_params.json", encoding="utf-8") as f:
    params = json.load(f)

alpha = params["alpha"]
beta = params["beta"]
K = params["K"]

parser = argparse.ArgumentParser(description="Predict Decryptability using DAR.")
parser.add_argument("E", type=float, help="Encryption complexity (E)")
parser.add_argument("H", type=float, help="Entropy of target (H)")
args = parser.parse_args()

D = dar(args.E, args.H, alpha, beta, K)
print(f"D(E={args.E}, H={args.H}) = {D:.4f}")
