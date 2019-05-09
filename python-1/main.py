# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

import csv
from collections import Counter

def iter_dataset_list(column_name, itervalue = 0):
    data = []
    with open('data.csv', 'r', encoding='UTF-8') as csvfile:
        read = csv.DictReader(csvfile, delimiter=',')
        count = 0
        for row in read: 
            data.append(row[column_name])
            if (itervalue != 0) and (count == itervalue): 
                break
            count+=1
    return data

def iter_dataset_dict(**columns):
    data = []
    with open('data.csv', 'r', encoding='UTF-8') as csvfile:
        read = csv.DictReader(csvfile, delimiter=',')
        for row in read:
            dic = {columns['column1']: row[columns['column1']], columns['column2']: float(row[columns['column2']])}
            data.append(dic)
    return data

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
def q_1():
    return len(Counter(iter_dataset_list('nationality')))

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    return len(Counter(iter_dataset_list('club')))

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    return iter_dataset_list('full_name', 19) # 0-19

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    list = iter_dataset_dict(column1='full_name', column2='eur_wage')
    list.sort(reverse=True, key=lambda value: value['eur_wage'])
    
    # get first 10 players order by eur_wage descendent
    result = []
    for name in list[:10]: 
        result.append(name['full_name'])
    return result    

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    list = iter_dataset_dict(column1='full_name', column2='age')
    list.sort(reverse=True, key=lambda value: value['age'])
    
    # get first 10 players order by age descendent and alphabetical name 
    result = []
    for name in list[:10]: 
        result.append(name['full_name'])
    return result

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    list_complete = iter_dataset_list('age')

    list_keys = list(map(int, Counter(list_complete).keys()))
    list_values = Counter(list_complete).values()

    result = {}
    for age, count in zip(list_keys, list_values):
        result[age] = count
    return result
