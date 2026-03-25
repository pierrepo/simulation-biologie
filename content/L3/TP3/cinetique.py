#%matplotlib inline
import matplotlib.pyplot as plt

def vitesse_michaelis_menten(S, Vmax, Km):
    return (Vmax * S) / (Km + S)

def show_cinetique(Vmax=8, Km=2):
    dt = 0.1
    temps = [0]
    S = [10]
    P = [0]
               
    for point in range(0, 100):
        v = vitesse_michaelis_menten(S[-1], Vmax, Km)
        temps.append(temps[-1] + dt)
        S.append(S[-1] - v*dt)
        P.append(P[-1] + v*dt)
    
    fig, ax = plt.subplots()
    ax.set_xlabel("Temps")
    ax.set_ylabel("Concentration")
    ax.set_title("Concentration en fonction du temps")
    ax.plot(temps, S, color="green", label="substrat")
    ax.plot(temps, P, color="orange",  label="produit")
    ax.legend()
