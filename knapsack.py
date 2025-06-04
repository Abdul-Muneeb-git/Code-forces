import random

# Problem Parameters
NUM_ITEMS = 5
MAX_WEIGHT = 10
POPULATION_SIZE = 10
MUTATION_RATE = 0.1
GENERATIONS = 50
items = [random.randint(1,30) for i in range(NUM_ITEMS)]
weights = [random.randint(1,30) for i in range(NUM_ITEMS)]

# Initialize Population
def initialize_population(size, num_items):
    population = [[random.randint(0,1) for i in range(num_items)] for j in range(size)]
    return population


# Fitness Function
def fitness(chromosome):
    w = 0
    total = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total += items[i]
            w += weights[i]

    if w > MAX_WEIGHT:
        return 0
    return total

# Selection Function
def select(population):
    tournament_size = 3
    selected = random.sample(population, tournament_size)
    selected.sort(key = lambda x : fitness(x), reverse = True)
    return selected[0]



# Crossover Function
def crossover(parent1, parent2):
    point = random.randint(1, NUM_ITEMS - 1)
    return parent1[:point] + parent2[point:]

# Mutation Function
def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# Genetic Algorithm Execution
def genetic_algorithm():
    population = initialize_population(POPULATION_SIZE, NUM_ITEMS)
    best_solution = None
    best_fitness = 0

    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = select(population)
            parent2 = select(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

        # Track best solution
        for chrom in population:
            fit = fitness(chrom)
            if fit > best_fitness:
                best_fitness = fit
                best_solution = chrom

    return best_solution, best_fitness
# Main Function
def main():

    print(items, weights)
    best_solution, best_fitness = genetic_algorithm()
    print(f"Best Solution: {best_solution}")
    print(f"Best Fitness (Total Value): {best_fitness}")
if __name__ == "__main__":
    main()
