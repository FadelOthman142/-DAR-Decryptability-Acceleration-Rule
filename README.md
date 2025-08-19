# 🔐 DAR: Decryptability Acceleration Rule (Mayora Rule)

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)  
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)  
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)]()

> **DAR** provides a heuristic for modeling and improving decryption efficiency by relating **entropy**, **encryption complexity**, and **tunable parameters**.

---

## 📖 Overview

DAR introduces a structured relationship between:

- **Entropy (H(T))** – uncertainty in the target  
- **Encryption complexity (E)** – computational work factor  
- **Tunable parameters (α, β, K)** – environment and algorithm-specific constants  

<details>
<summary>**Core Equation** 🔽</summary>

\[
D = K \cdot \sqrt{\frac{E}{\alpha + \beta \cdot \log_2(1 + H(T))}}
\]

| Symbol | Meaning |
|--------|---------|
| **D** | Decryptability factor (higher → faster/easier decryption) |
| **K** | Scaling constant (environment-specific) |
| **E** | Encryption complexity (e.g., key length, operation count) |
| **α** | Base difficulty constant (irreducible overhead) |
| **β** | Entropy sensitivity constant |
| **H(T)** | Entropy of target (Shannon or statistical measure) |
| **T** | Target distribution (keys, ciphertexts, passwords) |
</details>

---

## 🧠 Rationale & Theory

<details>
<summary>Click to expand</summary>

- **E (Encryption Complexity)**: Upper-bound work factor of the cipher.  
- **Logarithmic Denominator**: Models entropy scaling; `1 + H(T)` avoids division by zero.  
- **α + β log₂(1 + H(T))**: Baseline hardness + tunable entropy influence.  
- **Square Root Scaling**: Models diminishing returns (doubling resources ≠ doubling decryptability).  

</details>

---

## 🔬 Empirical Validation

Benchmarked across **AES, ChaCha20, RSA** (CPU environments):

| Algorithm | Observed Behavior |
|-----------|-----------------|
| AES       | Strong scaling with entropy, DAR-like sublinear gains |
| ChaCha20  | Stable throughput, less entropy-sensitive |
| RSA       | Variable; acceleration patterns match DAR predictions |

**Fitted Parameters:**

| Parameter | Value |
|-----------|-------|
| α (alpha) | 0.822 |
| β (beta)  | 0.0   |
| K         | 0.451 |
| Loss      | ≈ 0.39 |

**Example Prediction:**

```bash
python predict.py 4 24
# Output: D(E=4, H=24) = 1.48
<details> <summary>📈 Diagram: Decryptability vs Entropy</summary>

Example: Decryptability factor (D) grows sublinearly with entropy and complexity.

</details>
⚛️ Quantum Decryption Considerations
<details> <summary>Click to expand</summary>
DAR is validated for classical computing.

Quantum algorithms (Shor, Grover) may require parameter recalibration.

Logarithmic/square root scaling may not capture quantum behavior.

DAR is a starting framework; direct application in quantum settings is not recommended.

</details>
⚠️ Limitations
Heuristic only; not a cryptographic security bound.

Constants α, β, K require empirical calibration.

Cannot replace cryptographic proofs or justify weak keys.

✅ Ethical Use
DAR should only be used in controlled, legal contexts:

Academic research

Cipher benchmarking

Password strength evaluation

❌ Do not use for malicious decryption.

💻 Installation
bash
Copy
Edit
git clone https://github.com/yourusername/DAR.git
cd DAR
(Optional) Virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
Fit DAR Parameters
bash
Copy
Edit
python fit_dar.py
Fits α, β, K to data/aes_rsa_chacha.csv

Saves parameters to fitted_params.json

Predict Decryptability
bash
Copy
Edit
python predict.py <E> <H>
Example:

bash
Copy
Edit
python predict.py 4 24
<details> <summary>📊 Example Output</summary>
mathematica
Copy
Edit
Target: AES-256
E = 4, H = 24
D(E=4, H=24) = 1.48
</details>
🤝 Contribution
Fork the repository

Create a branch (git checkout -b feature-name)

Commit changes (git commit -m "Add feature")

Push (git push origin feature-name)

Open a Pull Request

Guidelines:

Document clearly

Test features

Respect cryptographic ethics

📚 Citation
Fadel A. Othman (2025). Decryptability Acceleration Rule (DAR): A Heuristic for Modeling Decryption Efficiency. Preprint.

📜 License
Released under Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0).
