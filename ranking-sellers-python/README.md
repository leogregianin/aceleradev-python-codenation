# Ranking de Vendedores

Numa loja de moveis pretende-se automatizar o ranking de vendedores. Com este Ranking, os donos da loja pretendem estimular os vendedores bonificando os melhores.
Você receberá algumas informações sobre os vendedores, nome, número da loja em que o vendedor trabalha e valor vendido no mês.

## Observações

- Mostrar o vendedor com maior valor em vendas.
- Listar todos os vendedores ordenados pelo valor vendido, do maior para o menor.
- Mostrar o melhor vendedor de uma determinada loja. Você receberá a lista de vendedores e deverá fazer um filtro nesta lista pela loja e retornar o nome do vendedor com o maior valor em vendas.
- Também é estipulado uma meta para vendas de R$ 500,00. Então é necessário listar os vendedores que não atigiram esta meta, em ordem crescente pelo valor de venda.

Em todas as funções, você receberá uma lista de vendedores, contendo um dicionario com os dados do vendedor:

Ex:

    Entrada:
        vendedores = [
            {"name": "Joana", "store": 2, "value": 1200.00},
        ]

    Saida:
        vendedores = ['Joana']

> OBS: Deve ser considerado a situação em que a função recebe lista de vendedores vazia.

## Tópicos

Neste desafio você vai aprender:

- Python
    - Lambda, Lists, Dict
- Testes unitários

## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`
