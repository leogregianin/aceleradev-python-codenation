# Cálculo dos custos de uma aplicação serverless

A arquitetura serverless vem sendo adotada por diversas empresas no mercado graças a uma série de benefícios como escalabilidade e baixo custo.
Mas ao mesmo tempo que fornece benefícios ela também aumenta a complexidade em alguns aspectos, como o cálculo do custo final da operação. O objetivo deste desafio é criar uma calculadora que facilite este cálculo.

A arquitetura da nossa aplicação é:

- Quando o usuário faz uma requisição para nossa API enviamos uma mensagem para uma fila de processos com os dados a serem executados (por exemplo: os itens que o usuário comprou)
- Quando a mensagem é recebida na fila o fornecedor de cloud automaticamente executa duas funções que implementam a regra de negócio (por exemplo: cálculo do frente de uma compra)

Após consulta ao site do fornecedor de cloud escolhido coletamos os seguintes custos:

- Valor por mensagem recebida na fila: U$ 0.00000040
- Valor por execução da função: U$ 0.0000002
- Valor por tempo de execução: além do valor inicial o fornecedor cobra U$ 0.0002080 por segundo executado

Precisamos calcular os seguintes cenários:

- 50 requisições por dia (50 itens na fila, sendo que cada item dispara 2 funções)
- 100 requisições por dia (100 itens na fila, sendo que cada item dispara 2 funções)
- 1000 requisições por dia (1000 itens na fila, sendo que cada item dispara 2 funções)
- 5000 requisições por dia (5000 itens na fila, sendo que cada item dispara 2 funções)

## Observações

- Para fins de cálculo vamos considerar que o tempo de execução de cada função é de 3 segundos
- A calculadora deve mostrar os valores mensais e anuais de cada cenário
- Considerar que as execuções ocorrem em todos os dias do mês, incluindo fins de semana e feriados
- Não é necessário considerar anos bissextos

## Tópicos

Neste desafio você vai aprender:

- Python
- Testes unitários

## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`