from Population import Solve
import random
import time
random.seed(time.time())

class GeneticAlgorithm:
    def __init__(self):
        self.epochs =10
        self.populationSize = 2
        self.rateCrossover = 0.90
        self.rateMutation = 0.5

    """IRÁ RETORNAR UM 'SOLVE' ALEATORIO COM BASE EM CALCULOS ALEATORIOS"""
    def rouletteWheel(self, population: list[Solve]) -> Solve:
        total_cost = sum(solve.cost() for solve in population)
        r = random.random() * total_cost
        acc = 0
        for solve in population:
            acc += solve.cost()
            if r <= acc:
                return solve
        raise Exception("Wrong Values")

    def run(self) -> Solve:
        """IRÁ CRIAR A PRIMEIRA POPULAÇÃO"""
        population: list[Solve] = []

        for _ in range(self.populationSize):
            solve = Solve()
            population.append(solve)

        steps = 0
        while steps < self.epochs:
            '''IRÁ GERAR A NOVA GERAÇÃO'''
            nextGeneration: list[Solve] = []

            for _ in range(self.populationSize // 2):
                first_parent = self.rouletteWheel(population)
                child1, child2 = first_parent.clone(), first_parent.clone()

                if random.random() < self.rateCrossover:
                    second_parent = self.rouletteWheel(population)
                    child1, child2 = first_parent.crossover_ordered(second_parent)

                nextGeneration.append(child1)
                nextGeneration.append(child2)

            for child in nextGeneration:
                if random.random() < self.rateMutation:
                    child.mutate()

            population = nextGeneration[:self.populationSize]
            print('step ', steps)
            steps += 1

        bestSolve = population[0]
        for solve in population:
            if solve.cost() < bestSolve.cost():
                bestSolve = solve

        return bestSolve

def register_results(percurso, distancia, num_execucao):
    with open('results.txt', 'a') as file:
        file.write(f" Route = {percurso}, Distance = {distancia}\n")

if __name__ == "__main__":
    ga = GeneticAlgorithm()
    num_repeticoes = 30
    for i in range(1, num_repeticoes + 1):
        best_solve = ga.run()
        percurso = best_solve.decode()  # Supondo que o percurso possa ser obtido assim
        distancia = best_solve.cost()
        register_results(percurso, distancia, i)
    print("Complete executions. Results recorded in results.txt")
