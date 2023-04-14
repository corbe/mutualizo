
# Mutualizo

 ''' Teste para empresa mutualizo

## 🚀 Começando


### 📋 Pré-requisitos

```
Python >= 3.8.15
docker-compose >= 2.0
```

### 📋 Instalação
```
#Clone o projeto em sua máquina local.
git clone git@github.com:corbe/mutualizo.git

#Acesse o diretório da aplicação.
cd mutualizo/

#Crie a aplicação.
sudo docker-compose build

#Rode a aplicação.
sudo docker-compose up
```

### 📋 Utilização
```
  # Siga os passos abaixo para utilização dos endpoints
  

  # Execute o metódo de login. [POST]

    http://127.0.0.1:8000/login    
    {
        "username": "test"
        "password": "test"
    }

    # Copie o access token retornado, e adicione ao header das demais requisições


    # Execute o metódo de reverse_string . [POST]
    http://127.0.0.1:8000/reverse-string 

    #header 
    {
        "Authorization" : "Bearer " [access_token] 
    }

    #payload
    {
        "number": "-231"
    }
  
  
    # Execute o metódo de average_words_length. [POST]
    http://127.0.0.1:8000/average-words-length

    #header 
    {
        "Authorization" : "Bearer " [access_token] 
    }

    #payload
    {
        "sentence": "Hi all, my name is Tom...I am originally from Brazil."
    }

    
    
    # Execute o metódo de matched_mismatched_words. [POST]
    http://127.0.0.1:8000/matched-mismatched-words
    
    #header 
    {
        "Authorization" : "Bearer " [access_token] 
    }

    #payload
    {
        "sentence1": "We are really pleased to meet you in our city",
        "sentence2": "The city was hit by a really heavy storm"
    }





### 📋 Swagger
```
 Documentação do projeto
```
#Abra o navegador e acesse o url docs
http://127.0.0.1:8000/docs


### 📋 Testes
```

 Para execução dos testes siga os passos


# Retorne ID do container
sudo docker ps

# Acesse o container
sudo docker exec -it [id_do_container] bash

# Execute os testes
pytest app


## 🛠️ Construído com

* [FastAPI Framework] (https://fastapi.tiangolo.com/)

Nós usamos [GIT](https://git-scm.com/) para controle de versão.

Este projeto está sob a licença OpenSource

*Sugestão de melhorias
- Adicionar variaves de username e senha do usuário no arquivo .env e variável de ambiente
- Middleware de autenticação.
- Incrementação na documentação swagger
- Internacionalização
- Incrementar documentação

* Agradeço a Mutualizo pela oportunidade de demonstrar meu trabalho.

⌨️ com ❤️ por [Daniel Corbe Hahne Latorre](https://github.com/dfront) 😊
