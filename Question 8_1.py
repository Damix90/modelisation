import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile

fs, u = wavfile.read("2notes.wav")  # u peut être stéréo (2 colonnes)
print("fs =", fs, "Hz  |  shape =", u.shape)

# Si stéréo : on passe en mono (moyenne des canaux)
if u.ndim == 2:
    u = u.mean(axis=1)

# Convertir en float pour les calculs FFT
u = u.astype(np.float64)

plt.figure()
plt.plot(u)
plt.title("Signal temporel u_n")
plt.xlabel("n")
plt.ylabel("u_n")
plt.show()
