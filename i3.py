from app import generate_seating as gs

'''import sqlite3
import random

class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        # Fitness function: lower is better
        fitness = 0
        for i in range(len(self.genes) - 1):
            if self.genes[i].get('DEPARTMENT_ID') == self.genes[i + 1].get('DEPARTMENT_ID'):
                fitness += 1
        return fitness

def generate_initial_population(population_size, students):
    population = []
    for _ in range(population_size):
        genes = random.sample(students, len(students))
        individual = Individual(genes)
        population.append(individual)
    return population

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1.genes) - 1)
    child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
    return Individual(child_genes)

def mutate(individual):
    mutation_point1, mutation_point2 = random.sample(range(len(individual.genes)), 2)
    individual.genes[mutation_point1], individual.genes[mutation_point2] = (
        individual.genes[mutation_point2],
        individual.genes[mutation_point1],
    )
    return individual

def genetic_algorithm(population_size, generations, students, bench_capacity):
    population = generate_initial_population(population_size, students)

    for generation in range(generations):
        population.sort(key=lambda x: x.fitness)

        if population[0].fitness == 0:
            break  # Solution found

        new_population = [population[0]]  # Keep the best individual

        # Create the next generation using crossover and mutation
        for _ in range(population_size - 1):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            if random.random() < 0.2:  # Mutation probability
                child = mutate(child)
            new_population.append(child)

        population = new_population

    best_solution = population[0]
    return best_solution.genes

def main():
    connection = sqlite3.connect('University.db')
    cursor = connection.cursor()

    # Fetch classroom capacity from the database (replace 'ITA' with the actual classroom ID)
    classroom_id = 'ITA'
    cursor.execute("SELECT BENCH_CAPACITY FROM CLASSROOM WHERE CLASSROOM_ID=?", (classroom_id,))
    bench_capacity = cursor.fetchone()[0]

    # Fetch students from the last two departments from the database
    department_id_1 = 5001
    department_id_2 = 5003
    cursor.execute("SELECT * FROM STUDENT WHERE DEPARTMENT_ID IN (?, ?)", (department_id_1, department_id_2))
    students = [{'NAME': row[0], 'REGISTER_NUMBER': row[1], 'DEPARTMENT_ID': row[4]} for row in cursor.fetchall()]

    # Run the genetic algorithm
    best_solution_genes = genetic_algorithm(population_size=50, generations=100, students=students, bench_capacity=bench_capacity)

    # Print the final seating arrangement
    print("Final Seating Arrangement:")
    for i, student in enumerate(best_solution_genes):
        print(f"Seat {i + 1}: {student['NAME']} ({student['DEPARTMENT_ID']})")

    connection.close()

if __name__ == "__main__":
    main()

import sqlite3
import random

class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        # Fitness function: lower is better
        fitness = 0
        for i in range(len(self.genes) - 1):
            if self.genes[i].get('DEPARTMENT_ID') == self.genes[i + 1].get('DEPARTMENT_ID'):
                fitness += 1
        return fitness

def generate_initial_population(population_size, students):
    population = []
    for _ in range(population_size):
        genes = random.sample(students, len(students))
        individual = Individual(genes)
        population.append(individual)
    return population

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1.genes) - 1)
    child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
    return Individual(child_genes)

def mutate(individual):
    mutation_point1, mutation_point2 = random.sample(range(len(individual.genes)), 2)
    individual.genes[mutation_point1], individual.genes[mutation_point2] = (
        individual.genes[mutation_point2],
        individual.genes[mutation_point1],
    )
    return individual

def genetic_algorithm(population_size, generations, students, bench_capacity):
    population = generate_initial_population(population_size, students)

    for generation in range(generations):
        population.sort(key=lambda x: x.fitness)

        if population[0].fitness == 0:
            break  # Solution found

        new_population = [population[0]]  # Keep the best individual

        # Create the next generation using crossover and mutation
        for _ in range(population_size - 1):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            if random.random() < 0.2:  # Mutation probability
                child = mutate(child)
            new_population.append(child)

        population = new_population

    best_solution = population[0]
    return best_solution.genes

def main():
    connection = sqlite3.connect('University.db')
    cursor = connection.cursor()

    # Fetch classroom capacity from the database (replace 'ITA' with the actual classroom ID)
    classroom_id = 'ITA'
    cursor.execute("SELECT BENCH_CAPACITY FROM CLASSROOM WHERE CLASSROOM_ID=?", (classroom_id,))
    bench_capacity = cursor.fetchone()[0]

    # Fetch students from the last two departments from the database
    department_id_1 = 5001
    department_id_2 = 5003
    cursor.execute("SELECT * FROM STUDENT WHERE DEPARTMENT_ID IN (?, ?)", (department_id_1, department_id_2))
    students = [{'NAME': row[0], 'REGISTER_NUMBER': row[1], 'DEPARTMENT_ID': row[4]} for row in cursor.fetchall()]

    # Run the genetic algorithm
    best_solution_genes = genetic_algorithm(population_size=50, generations=100, students=students, bench_capacity=bench_capacity)

    # Store the final seating arrangement in a list
    final_seating_arrangement = []
    for i, student in enumerate(best_solution_genes):
        final_seating_arrangement.append(f"Seat {i + 1}: {student['NAME']} ({student['DEPARTMENT_ID']})")

    # Remove repeated names from the list
    final_seating_arrangement = list(dict.fromkeys(final_seating_arrangement))

    # Print the final seating arrangement
    print("Final Seating Arrangement:")
    for seat in final_seating_arrangement:
        print(seat)

    connection.close()

if __name__ == "__main__":
    main()

import sqlite3
import random

class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        # Fitness function: lower is better
        fitness = 0
        for i in range(len(self.genes) - 1):
            if self.genes[i].get('DEPARTMENT_ID') == self.genes[i + 1].get('DEPARTMENT_ID'):
                fitness += 1
        return fitness

def generate_initial_population(population_size, students):
    population = []
    for _ in range(population_size):
        genes = random.sample(students, len(students))
        individual = Individual(genes)
        population.append(individual)
    return population

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1.genes) - 1)
    child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
    return Individual(child_genes)

def mutate(individual):
    mutation_point1, mutation_point2 = random.sample(range(len(individual.genes)), 2)
    individual.genes[mutation_point1], individual.genes[mutation_point2] = (
        individual.genes[mutation_point2],
        individual.genes[mutation_point1],
    )
    return individual

def genetic_algorithm(population_size, generations, students, bench_capacity):
    population = generate_initial_population(population_size, students)

    for generation in range(generations):
        population.sort(key=lambda x: x.fitness)

        if population[0].fitness == 0:
            break  # Solution found

        new_population = [population[0]]  # Keep the best individual

        # Create the next generation using crossover and mutation
        for _ in range(population_size - 1):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            if random.random() < 0.2:  # Mutation probability
                child = mutate(child)
            new_population.append(child)

        population = new_population

    best_solution = population[0]
    return best_solution.genes

def main():
    connection = sqlite3.connect('University.db')
    cursor = connection.cursor()

    # Fetch classroom capacity from the database (replace 'ITA' with the actual classroom ID)
    classroom_id = 'ITA'
    cursor.execute("SELECT BENCH_CAPACITY FROM CLASSROOM WHERE CLASSROOM_ID=?", (classroom_id,))
    bench_capacity = cursor.fetchone()[0]

    # Fetch students from the last two departments from the database
    department_id_1 = 5001
    department_id_2 = 5003
    cursor.execute("SELECT * FROM STUDENT WHERE DEPARTMENT_ID IN (?, ?)", (department_id_1, department_id_2))
    students = [{'NAME': row[0], 'REGISTER_NUMBER': row[1], 'DEPARTMENT_ID': row[4]} for row in cursor.fetchall()]

    # Run the genetic algorithm
    best_solution_genes = genetic_algorithm(population_size=50, generations=100, students=students, bench_capacity=bench_capacity)

    # Store the final seating arrangement in a list
    final_seating_arrangement = []
    for i, student in enumerate(best_solution_genes):
        final_seating_arrangement.append(f"Seat {i + 1}: {student['NAME']} ({student['DEPARTMENT_ID']})")

    # Remove repeated names from the list and keep the first allotted seat number
    unique_seating_arrangement = []
    seen_names = set()
    for seat in final_seating_arrangement:
        name = seat.split(":")[1].strip()
        if name not in seen_names:
            unique_seating_arrangement.append(seat)
            seen_names.add(name)

    # Print the final unique seating arrangement
    print("Final Unique Seating Arrangement:")
    for seat in unique_seating_arrangement:
        print(seat)

    connection.close()

if __name__ == "__main__":
    main()'''

import sqlite3
import random

class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        # Fitness function: lower is better
        fitness = 0
        for i in range(len(self.genes) - 1):
            if self.genes[i].get('DEPARTMENT_ID') == self.genes[i + 1].get('DEPARTMENT_ID'):
                fitness += 1
        return fitness
'''def get_students_from_database(department_id_1, department_id_2):
    connection = sqlite3.connect('University.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM STUDENT WHERE DEPARTMENT_ID IN (?, ?)", (department_id_1, department_id_2))
    students = [{'NAME': row[0], 'REGISTER_NUMBER': row[1], 'DEPARTMENT_ID': row[4]} for row in cursor.fetchall()]
    connection.close()
    return students'''

def generate_initial_population(population_size, students):
    population = []
    for _ in range(population_size):
        genes = random.sample(students, len(students))
        individual = Individual(genes)
        population.append(individual)
    return population

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1.genes) - 1)
    child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
    return Individual(child_genes)

def mutate(individual):
    mutation_point1, mutation_point2 = random.sample(range(len(individual.genes)), 2)
    individual.genes[mutation_point1], individual.genes[mutation_point2] = (
        individual.genes[mutation_point2],
        individual.genes[mutation_point1],
    )
    return individual

def genetic_algorithm(population_size, generations, students, bench_capacity):
    population = generate_initial_population(population_size, students)

    for generation in range(generations):
        population.sort(key=lambda x: x.fitness)

        if population[0].fitness == 0:
            break  # Solution found

        new_population = [population[0]]  # Keep the best individual

        # Create the next generation using crossover and mutation
        for _ in range(population_size - 1):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            if random.random() < 0.2:  # Mutation probability
                child = mutate(child)
            new_population.append(child)

        population = new_population

    best_solution = population[0]
    return best_solution.genes

def main(classroom,dept1,dept2):
    connection = sqlite3.connect('University.db')
    cursor = connection.cursor()

    # Fetch classroom capacity from the database (replace 'ITA' with the actual classroom ID)
    classroom_id = classroom
    cursor.execute("SELECT BENCH_CAPACITY FROM CLASSROOM WHERE CLASSROOM_ID=?", (classroom_id,))
    bench_capacity = cursor.fetchone()[0]

    # Fetch students from the last two departments from the database
    department_id_1 = dept1
    department_id_2 = dept2
    cursor.execute("SELECT * FROM STUDENT WHERE DEPARTMENT_ID IN (?, ?)", (department_id_1, department_id_2))
    students = [{'NAME': row[0], 'REGISTER_NUMBER': row[1], 'DEPARTMENT_ID': row[4]} for row in cursor.fetchall()]

    # Run the genetic algorithm
    best_solution_genes = genetic_algorithm(population_size=50, generations=100, students=students, bench_capacity=bench_capacity)

    # Store the final seating arrangement in a list
    final_seating_arrangement = []
    for i, student in enumerate(best_solution_genes):
        final_seating_arrangement.append(f"Seat {i + 1}: {student['NAME']} ({student['DEPARTMENT_ID']})")

    # Remove repeated names from the list and keep the first allotted seat number
    unique_seating_arrangement = []
    seen_names = set()
    for seat in final_seating_arrangement:
        name = seat.split(":")[1].strip()
        if name not in seen_names:
            unique_seating_arrangement.append(seat)
            seen_names.add(name)

    # Create a matrix format with 2 columns
    matrix_format = [unique_seating_arrangement[i:i + 2] for i in range(0, len(unique_seating_arrangement), 2)]

    # Print the final unique seating arrangement in matrix format
    print("Final Unique Seating Arrangement (Matrix Format):")
    #for row in matrix_format:
        #print(row)
    return matrix_format

    connection.close()

if __name__ == "__main__":
    main()




