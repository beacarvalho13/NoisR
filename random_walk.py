import random
import matplotlib.pyplot as plt


def random_walk(num_steps, prob_left, num_particles):
    particle_paths = []
    for j in range(num_particles):
        position = 0
        path = [position]
        for i in range(int(num_steps)):
            x = random.uniform(0, 1)
            if x <= prob_left:
                position = position + 1
            else:
                position = position - 1
            path.append(position)
        particle_paths.append(path)
    
    create_plot(num_steps, particle_paths)
    return particle_paths



def create_plot(num_steps, particle_paths):

    time = [x for x in range(len(particle_paths[0]))]  
    
    for particle_path in particle_paths:
        plt.plot(particle_path, time)
    
    plt.title('Random Walk - N particles')
    plt.xlabel('Position')
    plt.ylabel('Time')
    plt.show()


num_steps = int(input("Qual é o número de passos?"))
prob = input("Qual é a probabilidade de ir para a esquerda?")
prob_left = float(prob)
num_particles = int(input("Qual é o número de partículas?"))

random_walk(num_steps, prob_left, num_particles)
