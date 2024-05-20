import requests
import logging

logging.getLogger('urllib3').setLevel(logging.ERROR)

endpoint = 'https://infocr-fiap-default-rtdb.firebaseio.com/exams.json'

response = requests.get(endpoint)
exames = {
    "Exames": [],
    "Descrição": [],
}

if(response.status_code == 200):
    data = response.json()

    for key in data.keys():
        if not(type(data[key]) != dict):
            for examKey in data[key].keys():
                if(examKey == "cantDo"):
                    for info in range(len(data[key])):
                        

                exames['Exames'].append(data[key]["title"])
                exames["Descrição"].append(data[key]["about"])
            
            

    print(exames)
else:
    print("Error ao fazer solicitação")


# try:
#     response = requests.get(endpoint)

#     response.raise_for_status()

#     data = response.json()
#     print(data)


# except requests.exceptions.RequestException as requestError:
#     print("Erro ao fazer socilicitação:", requestError)

# except ValueError as decodeError:
#     print("Erro ao decodificar o dado!", decodeError)

# except ConnectionResetError as conectionResetError:
#     print("Error ao comunicar-se com o servidor:", conectionResetError)

# finally:
#     print(data)
    





