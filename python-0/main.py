import json

json_api = """{
  "uf": [
    {
      "nome": "Acre",
      "sigla": "AC",
      "extensao": 164123.040
    },
    {
      "nome": "Alagoas",
      "sigla": "AL",
      "extensao": 27778.506
    },
    {
      "nome": "Amapá",
      "sigla": "AP",
      "extensao": 142828.521
    },
    {
      "nome": "Amazonas",
      "sigla": "AM",
      "extensao": 1559159.148
    },
    {
      "nome": "Bahia",
      "sigla": "BA",
      "extensao": 564733.177
    },
    {
      "nome": "Ceará",
      "sigla": "CE",
      "extensao": 148920.472
    },
    {
      "nome": "Distrito Federal",
      "sigla": "DF",
      "extensao": 5779.999
    },
    {
      "nome": "Espírito Santo",
      "sigla": "ES",
      "extensao": 46095.583
    },
    {
      "nome": "Goiás",
      "sigla": "GO",
      "extensao": 340111.783
    },
    {
      "nome": "Maranhão",
      "sigla": "MA",
      "extensao": 331937.450
    },
    {
      "nome": "Mato Grosso",
      "sigla": "MT",
      "extensao": 903366.192
    },
    {
      "nome": "Mato Grosso do Sul",
      "sigla": "MS",
      "extensao": 357145.532
    },
    {
      "nome": "Minas Gerais",
      "sigla": "MG",
      "extensao": 586522.122
    },
    {
      "nome": "Pará",
      "sigla": "PA",
      "extensao": 1247954.666
    },
    {
      "nome": "Paraíba",
      "sigla": "PB",
      "extensao": 56585.000
    },
    {
      "nome": "Paraná",
      "sigla": "PR",
      "extensao": 199307.922
    },
    {
      "nome": "Pernambuco",
      "sigla": "PE",
      "extensao": 98311.616
    },
    {
      "nome": "Piauí",
      "sigla": "PI",
      "extensao": 251577.738
    },
    {
      "nome": "Rio de Janeiro",
      "sigla": "RJ",
      "extensao": 43780.172
    },
    {
      "nome": "Rio Grande do Norte",
      "sigla": "RN",
      "extensao": 52811.047
    },
    {
      "nome": "Rio Grande do Sul",
      "sigla": "RS",
      "extensao": 281730.223
    },
    {
      "nome": "Rondônia",
      "sigla": "RO",
      "extensao": 237590.547
    },
    {
      "nome": "Roraima",
      "sigla": "RR",
      "extensao": 224300.506
    },
    {
      "nome": "Santa Catarina",
      "sigla": "SC",
      "extensao": 95736.165
    },
    {
      "nome": "São Paulo",
      "sigla": "SP",
      "extensao": 248222.362
    },
    {
      "nome": "Sergipe",
      "sigla": "SE",
      "extensao": 21915.116
    },
    {
      "nome": "Tocantins",
      "sigla": "TO",
      "extensao": 277720.520
    }
  ]
}"""

def ordenarExtensao(value):
  return value['extensao']

def os10MaioresEstadosDoBrasil():
    result = []
    data = json.loads(json_api)["uf"]
    data.sort(reverse=True, key=ordenarExtensao)
    for estado in data[:10]: 
      result.append(estado["nome"])
    return result
