# Trabalhando com Datetime e Numpy

Datas são bastante utilizadas em sistemas. O objetivo do desafio é trabalhar um pouco com datas e conhecer o modulo numpy, que também pode ser utilizado com datas.

## Observações

- Faça uma função que receba uma data no formato dd/mm/YYYY e determine se a mesma é  válida. A data será válida apenas se estiver no formato dd/mm/YYYY.
- Faça uma função que rebeba uma data e retorne o dia da semana correspondente. Ex: "Saturday"
- Faça uma função que receba uma data em formato string e retorne em formato datetime. Formatos válidos: "dd/mm/YYYY", "dd-mm-YYYY" , "ddmmYYYY", retorna False se a data não esta em um desses formatos.
- Faça uma função que recebe o ano e o mês e retorne todas as datas do mês. Obs: utilize o Numpy (arange).
- Faça uma função que recebe o ano e o mês e retorne a quantidade de dias úteis que ele possui. Obs: Utilize o Numpy.
- Faça uma função que recebe o ano e encontre a primeira segunda-feira de maio. O retorno deve ser uma string no formato "dd/mm/YYYY". Obs: Utilize NumPy.

## Tópicos

Neste desafio você vai aprender:

- Python
    - Datetime
    - Numpy
- Testes unitários

## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`
