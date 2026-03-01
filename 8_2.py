import numpy as np
import matplotlib.pyplot as plt

def spectrum_frequencies(x, fs):
    N = len(x)
    X = np.fft.fft(x)
    mag = np.abs(X)
    # fréquences associées aux indices l=0..N-1
    freqs = np.fft.fftfreq(N, d=1/fs)
    return freqs, mag

def fundamental_from_spectrum(freqs, mag, fmin=20, fmax=5000):
    """
    Estime la fondamentale = plus grand pic dans [fmin,fmax] côté fréquences positives.
    Pour éviter DC (0 Hz), on impose fmin.
    """
    mask = (freqs >= fmin) & (freqs <= fmax)
    idx = np.argmax(mag[mask])
    f0 = freqs[mask][idx]
    return f0

# --- Découpage simple en 2 moitiés (souvent suffisant) ---
Ntot = len(u)
u1 = u[:Ntot//2]
u2 = u[Ntot//2:]

# Optionnel : fenêtrage pour réduire la fuite spectrale
def hann_window(x):
    w = np.hanning(len(x))
    return x * w

u1w = hann_window(u1)
u2w = hann_window(u2)

# Spectres
f1, M1 = spectrum_frequencies(u1w, fs)
f2, M2 = spectrum_frequencies(u2w, fs)

# On ne garde que les fréquences positives (0 à fs/2)
pos1 = (f1 >= 0)
pos2 = (f2 >= 0)

# Tracé des modules
plt.figure()
plt.plot(f1[pos1], M1[pos1])
plt.title("Spectre |Û| - Note 1 (segment 1)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("|Û(f)|")
plt.xlim(0, 5000)
plt.show()

plt.figure()
plt.plot(f2[pos2], M2[pos2])
plt.title("Spectre |Û| - Note 2 (segment 2)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("|Û(f)|")
plt.xlim(0, 5000)
plt.show()

# Fondamentales (estimation)
f0_1 = fundamental_from_spectrum(f1[pos1], M1[pos1], fmin=50, fmax=2000)
f0_2 = fundamental_from_spectrum(f2[pos2], M2[pos2], fmin=50, fmax=2000)

print("Fondamentale note 1 ~", f0_1, "Hz")
print("Fondamentale note 2 ~", f0_2, "Hz")
