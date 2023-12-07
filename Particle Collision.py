import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

box_size  = float(input("Qual é o tamanho da caixa? "))
initial_pos1 = float(input("Qual é a posição inicial da partícula 1? "))
initial_pos2 = float(input("Qual é a posição inicial da partícula 2? "))
while initial_pos1 > box_size or initial_pos2 > box_size or initial_pos1 < 0 or initial_pos2 < 0:
    print("Inválido. A partícula está fora do espaço")
    box_size  = float(input("Qual é o tamanho da caixa? "))
    initial_pos1 = float(input("Qual é a posição inicial da partícula 1? "))
    initial_pos2 = float(input("Qual é a posição inicial da partícula 2? "))
initial_velocity1 = float(input("Qual é a velocidade inicial da partícula 1? "))
initial_velocity2 = float(input("Qual é a velocidade inicial da partícula 2? "))
mass1 = float(input("Qual é a massa da partícula 1? "))
mass2 = float(input("Qual é a massa da partícula 2? "))
num_frames = int(input("Quantos frames tem a animação? "))

def simulate_and_animate_collision(initial_pos1, initial_pos2, initial_velocity1, initial_velocity2, mass1, mass2, num_frames, box_size):
    ball1 = [initial_pos1]
    ball2 = [initial_pos2]
    positions1 = initial_pos1
    positions2 = initial_pos2

    for _ in range(num_frames):
        positions1 = positions1 + initial_velocity1
        positions2 = positions2 + initial_velocity2

        # Check for collision
        if positions1 + 0.1 >= positions2 - 0.1:
            positions1 = positions2
            total_mass = mass1 + mass2
            velocity1_after = ((mass1 - mass2) * initial_velocity1 + 2 * mass2 * initial_velocity2) / total_mass
            velocity2_after = ((mass2 - mass1) * initial_velocity2 + 2 * mass1 * initial_velocity1) / total_mass

            initial_velocity1 = velocity1_after
            initial_velocity2 = velocity2_after
        if positions1 <= 0:
            positions1 = 0
            initial_velocity1 = abs(initial_velocity1)   #a partícula vai ter de andar no sentido positivo

        if positions1 >= box_size:
            positions1 = box_size
            initial_velocity1 = -abs(initial_velocity1)  #a partícula vai ter de andar no sentido negativo

        if positions2 <= 0:
            positions2 = 0
            initial_velocity2 = abs(initial_velocity2)

        if positions2 >= box_size:
            positions2 = box_size
            initial_velocity2 = -abs(initial_velocity2)

        ball1.append(positions1)
        ball2.append(positions2)

    return ball1, ball2


def create_animation(positions1, positions2, box_size):
    num_frames = len(positions1)

    fig, ax = plt.subplots()
    ax.set_xlim(0, box_size)
    ax.set_ylim(-0.1, 0.1)

    global ball1, ball2
    ball_radius = 0.1
    ball1, = ax.plot(positions1[0], 0, 'bo', markersize=10)
    ball2, = ax.plot(positions2[0], 0, 'ro', markersize=10)

    def update(frame):
        ball1.set_xdata(positions1[frame] - ball_radius)
        ball2.set_xdata(positions2[frame] - ball_radius)
        return ball1, ball2

    ani = FuncAnimation(fig, update, frames=num_frames, blit=True)
    plt.show()



positions1,positions2=simulate_and_animate_collision (initial_pos1, initial_pos2, initial_velocity1, initial_velocity2, mass1, mass2, num_frames, box_size)

create_animation(positions1, positions2, box_size)
plt.close(fig)
