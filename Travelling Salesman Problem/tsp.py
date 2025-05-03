import sys
import random
import matplotlib.pyplot as plt
import math

def initialize_tour(num_cities):
    cities = []
    for i in range(num_cities):
        cities.append((random.random() * 100, random.random() * 100))

    return cities

# Plot the best tour
def plot_tour(cities):
    #ordered_cities = np.array([cities[i] for i in tour] + )
    plt.figure(figsize=(8,6))
    #plt.plot(cities, 'o-', markersize = 8)
    cities.append(cities[0])
    plt.plot([x for x,y in cities], [y for x,y in cities], '-o')
    #plt.plot(cities[0][0], cities[0])
    plt.title("TSP Solution using Simulated Annealing")
    plt.show()

def eucildean_distance(c1,c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

def tour_cost(cities):
    total = 0
    for i in range(len(cities) - 1):
        total += eucildean_distance(cities[i], cities[i+1])
    
    return total

def swap(cities):
    temp = cities.copy()

    c1 = random.randint(0,len(cities)-1)
    c2 = random.randint(0,len(cities)-1)

    while(c1 == c2):
        c2 = random.randint(0,len(cities)-1)

    temp[c1], temp[c2] = temp[c2], temp[c1]

    return temp

num_cities = 20 # default
if (len(sys.argv) > 1):
    num_cities = int(sys.argv[1])


cities = initialize_tour(num_cities) # very original layout

T = 10000
T_min = 5
cooling_rate = .001

count = 0

current_tour = cities # always starting with current condition
current_tour_cost = tour_cost(current_tour)

#initializing minimum
min_tour_cost = tour_cost(current_tour)
min_tour = current_tour

while T > T_min:

    new_tour = swap(current_tour)
    new_tour_cost = tour_cost(new_tour)

    # delta is difference between tour_cost(new_tour) - tour_cost (current_tour)
    # hill climbing algorithm

    delta = new_tour_cost - current_tour_cost
    if (delta < 0 or random.uniform(0,1) < math.exp(-delta/T)):
        current_tour = new_tour
        current_tour_cost = new_tour_cost

    if current_tour_cost < min_tour_cost:
        min_tour_cost = current_tour_cost
        min_tour = current_tour.copy()

    print(f"min tour cost at iteration {count}: {min_tour_cost}")

    T -= T*cooling_rate
    count += 1

if current_tour_cost < min_tour_cost:
    current_tour = min_tour.copy()
    current_tour_cost = min_tour_cost

plot_tour(current_tour)

print("done")