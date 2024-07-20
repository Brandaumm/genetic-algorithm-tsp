import random
import time
from CSV_Reader import *

current_time = time.time()
random.seed(current_time)

class Solve:
    reader = CSV_Reader()
    '''Gera por meio do reader.citiesNames a quantidade de cidades, soma-se + 1 para ter espaco de voltar para a primeira cidade'''
    values = list(range(len(reader.citiesNames()) + 1))

    '''Tamanho'''
    size = len(values)

    '''Faz a leitura de todas as cidades para evitar ciclos desnecessarios'''
    allCities = reader.citiesNames()

    '''Faz a leitura de todas as distancias para evitar ciclos desnecessarios'''
    allDistances = reader.CalculateCitiesDistance()


    '''Inicia aleatoriamente o vetor de cidades de tal forma que a primeira e ultima cidade sejam iguais'''
    def __init__(self):
        self.encode = [0]
        while len(self.encode) < self.size - 1:
            random_value = random.randint(1, self.size - 2)
            if random_value not in self.encode:
                self.encode.append(random_value)
        self.encode.append(self.encode[0])


    '''Ira copiar um intervalo de um solve'''
    def copy(self, other: 'Solve', position1: int, position2: int) -> None:
        for i in range(position1, position2):
            self.encode[i] = other.encode[i]

    '''Ira clonar totalmente um solve'''
    def clone(self) -> 'Solve':
        solve = Solve()
        solve.copy(self, 0, self.size - 1)
        return solve

    '''É responsavel por retornar a lista de cidade do respectivo solve'''
    def decode(self) -> list[str]:
        returnList = []
        for i in self.encode:
            returnList.append(self.allCities[i])
        return returnList


    '''Responsavel por calcular o valor das viagens por meio dos nomes das cidades'''
    def cost(self) -> float:
        data = self.decode()
        sum = 0
        ''' -1 é reponsavel para que o data[i + 1] não saia do intervalo do vetor'''
        for i in range(len(data) - 1):
            currentCityIndex = self.reader.cityNumber(data[i])
            nextCityIndex = self.reader.cityNumber(data[i + 1])
            sum += self.allDistances[currentCityIndex][nextCityIndex]
        return sum


    def fill_external(self, child: 'Solve', parent: 'Solve', min_position: int, max_position: int):
        size = len(self.encode)
        index = (max_position + 1) % size
        used = set(child.encode[min_position:max_position + 1])

        for i in range(1, size - 1):
            if i < min_position or i > max_position:
                while parent.encode[index] in used:
                    index = (index + 1) % size
                child.encode[i] = parent.encode[index]
                used.add(parent.encode[index])

        all_cities = set(self.encode)
        current_cities = set(child.encode)
        missing_cities = list(all_cities - current_cities)
        duplicate_indices = [i for i, city in enumerate(child.encode) if child.encode.count(city) > 1 and i != 0 and i != size - 1]

        for i in duplicate_indices:
            if missing_cities:
                child.encode[i] = missing_cities.pop(0)

    ''''''
    def crossover_ordered(self, other: 'Solve') -> tuple['Solve', 'Solve']:
        '''Gera filhos com sua propria composição de cidades'''
        child1 = Solve()
        child2 = Solve()

        size = len(self.encode)

        '''Gera dois números aleatórios'''
        position1 = random.randint(1, size - 3)
        position2 = random.randint(1, size - 3)

        '''Garante que os números aleatoriamente gerados serão diferentes'''
        while position2 == position1:
            position2 = random.randint(1, size - 3)

        '''Organiza-os por maior e menor'''
        start_point = min(position1, position2)
        end_point = max(position1, position2)

        '''Copia o intervalo de valores do pai para o filho'''
        child1.encode[start_point:end_point + 1] = self.encode[start_point:end_point + 1]
        child2.encode[start_point:end_point + 1] = other.encode[start_point:end_point + 1]

        '''Utiliza o fill external para complementar o crossover'''
        self.fill_external(child1, other, start_point, end_point)
        self.fill_external(child2, self, start_point, end_point)

        return child1, child2


    '''Responsavel por mutar um solve pelo ato de trocar de lugar duas cidades'''
    def mutate(self) -> None:
        position1 = random.randrange(1, self.size - 3)
        position2 = random.randrange(1, self.size - 3)
        while position2 == position1:
            position2 = random.randrange(1, self.size - 3)
        self.encode[position1], self.encode[position2] = self.encode[position2], self.encode[position1]

    def __repr__(self) -> str:
        sum = self.cost()
        return str(self.decode()) + ' -> (' + str(sum) + ', ' + str(self.cost()) + ')'
