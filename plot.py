import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

df = pd.read_csv('./steady.csv')
#df = df.drop(labels=range(0,999000), axis=0)
fig, ax = plt.subplots()

state_labels = ['0', '1', '2', '3', '4', '5', '6', '7']

def update(frame):
    ax.clear()
    state_values = df.iloc[frame, 1:]
    ax.bar(state_labels, state_values)
    ax.set_title('Steady State Distribution')
    ax.set_xlabel('State')
    ax.set_ylabel('Prob')
    ax.set_ylim(0,0.45)

# Obtiene el número total de frames (filas en el DataFrame)
num_frames = len(df)
print(len(df))
# Crea la animación
ani = FuncAnimation(fig, update, frames=num_frames, repeat=False, interval=1)
#plt.show()
ani.save('steady.gif', writer=PillowWriter(fps=30))

