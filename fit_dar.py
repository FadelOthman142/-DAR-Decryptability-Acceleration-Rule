import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from dar_model import dar
import json

df = pd.read_csv("data/aes_rsa_chacha.csv")
aes = df[df['algo'] == 'AES']
E = aes['E'].values
H = aes['H'].values
D = aes['accel_vs_baseline'].values

def fit_func(xdata, alpha, beta, K):
    E, H = xdata
    return dar(E, H, alpha, beta, K)

params, _ = curve_fit(fit_func, (E, H), D, p0=[0.8, 0.1, 0.4])
alpha, beta, K = params

with open("fitted_params.json", "w", encoding="utf-8") as f:
    json.dump({"alpha": alpha, "beta": beta, "K": K}, f, indent=4)

print(f"Fitted DAR parameters saved: α={alpha:.4f}, β={beta:.4f}, K={K:.4f}")
