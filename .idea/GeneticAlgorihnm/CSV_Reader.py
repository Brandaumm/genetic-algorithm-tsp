import csv
import math
from Calculus import *

calculus = Calculus()

class CSV_Reader:
    def ReadDocument(self) -> None:
        with open('C:/Users/USER/Documents/cidades.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=',')
            row = 0
            for column in reader:
                    print(f'\tCidade {column[0]} X: {column[1]} Y: {column[2]}')
                    row += 1

    def CalculateCitiesDistance(self):
        cities = []

        with open('C:/Users/USER/Documents/cidades.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=',')

            """O READER POSSUI UMA LIMITAÇÃO ONDE ELE NÃO CONSEGUE REITERAR NOVAMENTE DENTRO DE UM LOOP FOR
            ASSIM FAZENDO QUE SUA SEGUNDA INTERAÇÃO EM DIANTE SEJA VAZIA, POR ISSO OPTEI DE LER TODOS OS DADOS 
            PRIMEIRO PARA EVITAR ESSA PROBLEMATICA, ESTA FORMA NÃO É NENHUM POUCO ECONOMICA DEVIDO O FATO DE USAR MUITA MEMORIA,
            PORÉM FOI A SOLUÇÃO MAIS FACIL QUE ENCONTREI PARA SOLUCIONAR O PROBLEMA SEM AJUDA DE OUTRA BIBLIOTECA"""
            data = list(reader)

            for rowA in data:
                """CIDADE PRINCIPAL"""
                cityDistance = []
                cityA = rowA
                cityName = rowA[0]
                for rowB in data:
                    """CIDADE SECUNDARIA"""
                    cityB = rowB
                    distance = calculus.CalculateDistanceFromCities(cityA,cityB)
                    cityDistance.append(distance)
                cities.append(cityDistance)


            return cities

    '''RETORNA OS NOMES DAS CIDADES APARTIR DE SEU NUMERO'''
    def citiesNames(self):
        citiesNames = []

        with open('C:/Users/USER/Documents/cidades.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                name = row[0]
                citiesNames.append(name)
        return citiesNames

    """IREI RECEBER UMA STRING COM O NOME DA CIDADE E DESTA FORMA DECOBRIR O NUMERO CORRESPONDENTE NA LISTA"""
    def cityNumber(self, cityName):
        with open('C:/Users/USER/Documents/cidades.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=',')
            index = 0
            for row in reader:
                if(cityName == row[0]):
                    return index
                index += 1
        return None






if __name__ == "__main__":
    reader = CSV_Reader()
    reader.ReadDocument()
    reader.CalculateCitiesDistance()
    reader.citiesNames()



