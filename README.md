# 🔐 Decryptability Acceleration Rule (DAR)

DAR is a **novel heuristic model** for estimating the decryptability of cryptographic algorithms and password spaces.  
It balances **entropy (E)** and **hardware performance (H)** into a compact equation:

```
<div align="center">
  <img src="images/dar_formula.png" alt="DAR Formula" width="350"/>
</div>
```

Where:  
- **E** = Entropy or effective keyspace size  
- **H** = Hardware factor (cores, FLOPS, parallelism efficiency)  
- **α, β, K** = Tunable constants determined by benchmarks  

---

## 🚀 Features

- Generalized for **block ciphers, stream ciphers, and public key systems**  
- Can extend beyond cryptography: **password cracking, entropy-driven optimization, compression**  
- Tunable constants for **different hardware environments**  
- Provides **predictive decryptability scores** to guide research  

---

## 🔎 Example Prediction

```bash
python predict.py 4 24
# Output:
D(E=4, H=24) = 1.48
```

This aligns with measured accelerations for AES and RSA under similar conditions.

---

## 📘 Scope & Applicability

### Cipher Classes
- **Block ciphers**: AES, DES variants  
- **Stream ciphers**: ChaCha20, RC4  
- **Public key systems**: RSA, ECC (with adjusted interpretation of `E`)  

### Beyond Cryptography
- Password cracking  
- Compression-based attacks  
- Entropy-driven optimization  

### Password Cracking Tools
DAR can be integrated into password cracking tools to:  
- Increase efficiency  
- Improve stability  
- Make cracking more predictable by modeling entropy and computational complexity  

---

## ⚙️ Tunable Parameters

| Parameter | Description |
|-----------|-------------|
| **α**     | Irreducible costs (setup, I/O, memory latency) |
| **β**     | Entropy’s influence strength |
| **K**     | Normalization factor to scale DAR outputs |

---

## ⚛️ Quantum Decryption Considerations

DAR is primarily validated for **classical computing environments**.  
Its applicability to **quantum decryption** requires caution:

- Quantum algorithms (e.g., **Shor’s, Grover’s**) introduce fundamentally different speedups.  
- DAR parameters (α, β, K) may require **recalibration** with quantum benchmarking data.  
- Logarithmic entropy scaling and square root behavior reflect **classical cryptanalysis**, which may not apply to quantum systems.  
- DAR should be treated as a **starting framework** for quantum settings.  

👉 Future work should extend DAR with **quantum-specific models and empirical data**.  

---

## ⚠️ Limitations

- DAR is **heuristic** and **not** a cryptographic security bound.  
- Constants α, β, K require **empirical calibration** per environment.  
- DAR cannot replace **cryptographic proofs** or justify weak keys.  

---

## ✅ Ethical Use

DAR should only be applied in **controlled, ethical, and legal contexts**, such as:

- Academic research  
- Benchmarking cipher resistance  
- Password strength evaluation  

❌ **Must not** be used for malicious decryption or illegal activity.  

---

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International Public License**.  
See the [LICENSE](license) file for details.
