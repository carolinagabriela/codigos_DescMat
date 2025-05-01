import json

personagens = [
    {
        "nome": "Homem-Aranha",
        "sexo": "masculino",
        "animacao": True,
        "superpoder": True,
        "tipo": "herói",
        "universo": "Marvel",
        "idade": 18,
        "protagonista": True
    },
    {
        "nome": "Batman",
        "sexo": "masculino",
        "animacao": False,
        "superpoder": False,
        "tipo": "herói",
        "universo": "DC",
        "idade": 35,
        "protagonista": True
    },
    {
        "nome": "Mulher Maravilha",
        "sexo": "feminino",
        "animacao": True,
        "superpoder": True,
        "tipo": "herói",
        "universo": "DC",
        "idade": 28,
        "protagonista": True
    },
    {
        "nome": "SpongeBob",
        "sexo": "masculino",
        "animacao": True,
        "superpoder": False,
        "tipo": "animação",
        "universo": "Nickelodeon",
        "idade": 20,
        "protagonista": True
    },
    {
        "nome": "Superman",
        "sexo": "masculino",
        "animacao": False,
        "superpoder": True,
        "tipo": "herói",
        "universo": "DC",
        "idade": 30,
        "protagonista": True
    },
    {
        "nome": "Hulk",
        "sexo": "masculino",
        "animacao": True,
        "superpoder": True,
        "tipo": "herói",
        "universo": "Marvel",
        "idade": 35,
        "protagonista": True
    },
    {
        "nome": "Elsa",
        "sexo": "feminino",
        "animacao": True,
        "superpoder": True,
        "tipo": "animação",
        "universo": "Disney",
        "idade": 21,
        "protagonista": True
    },
    {
        "nome": "Harry Potter",
        "sexo": "masculino",
        "animacao": False,
        "superpoder": True,
        "tipo": "magia",
        "universo": "Harry Potter",
        "idade": 18,
        "protagonista": True
    },
    {
        "nome": "Gandalf",
        "sexo": "masculino",
        "animacao": False,
        "superpoder": True,
        "tipo": "fantasia",
        "universo": "Senhor dos Anéis",
        "idade": 1000,
        "protagonista": True
    },
    {
        "nome": "Katniss Everdeen",
        "sexo": "feminino",
        "animacao": False,
        "superpoder": False,
        "tipo": "herói",
        "universo": "Jogos Vorazes",
        "idade": 17,
        "protagonista": True
    },
    {
        "nome": "Sherlock Holmes",
        "sexo": "masculino",
        "animacao": False,
        "superpoder": False,
        "tipo": "detetive",
        "universo": "Clássicos",
        "idade": 40,
        "protagonista": True
    },
    {
        "nome": "Darth Vader",
        "sexo": "masculino",
        "animacao": False,
        "superpoder": True,
        "tipo": "sci-fi",
        "universo": "Star Wars",
        "idade": 45,
        "protagonista": False
    },
    {
        "nome": "Fiona",
        "sexo": "feminino",
        "animacao": True,
        "superpoder": False,
        "tipo": "animação",
        "universo": "Shrek",
        "idade": 25,
        "protagonista": True
    },
    {
        "nome": "Groot",
        "sexo": "masculino",
        "animacao": True,
        "superpoder": True,
        "tipo": "herói",
        "universo": "Marvel",
        "idade": 300,
        "protagonista": False
    },
    {
        "nome": "Black Widow",
        "sexo": "feminino",
        "animacao": False,
        "superpoder": True,
        "tipo": "herói",
        "universo": "Marvel",
        "idade": 30,
        "protagonista": True
    }
]

with open('personagens.json', 'w') as arquivo:
    json.dump(personagens, arquivo)