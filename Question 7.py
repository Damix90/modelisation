import numpy as np
import scipy.io.wavfile as wavfile

# Paramètres 
N = 4096
fs = 4096
T = 1.0
n = np.arange(N)

def re_epsilon(l):
    eps = np.exp(2j * np.pi * l * n / N)     # ε_l
    return eps.real                          # Re(ε_l)

def export_wav(x, filename):
    # Normalisation simple pour écrire en int16 (format wav courant)
    x = x / np.max(np.abs(x))
    x16 = np.int16(32767 * x)
    wavfile.write(filename, fs, x16)

for l in [400, 600, 1000]:
    x = re_epsilon(l)
    export_wav(x, f"Re_epsilon_{l}.wav")

# Vérification "mathématique" : comparer Re(ε_l) à cos(2π l n / N)
l = 600
x_num = re_epsilon(l)
x_theo = np.cos(2*np.pi*l*n/N)
print("Erreur max :", np.max(np.abs(x_num - x_theo)))