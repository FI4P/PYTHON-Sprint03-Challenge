import requests
import logging

logging.getLogger('urllib3').setLevel(logging.ERROR)

endpoint = 'https://infocr-fiap-default-rtdb.firebaseio.com/exams.json'

response = requests.get(endpoint)
exames = {
    "Exames": [],
    "Descrição": [],
    "NãoPraticar": [],
    "InfosLudicas": [],
    "Preparos": [],

}

if(response.status_code == 200):
    data = response.json()

    for key in data.keys():
        if not(type(data[key]) != dict):
            for examKey in data[key].keys():
                arrayInfos = []
                if(examKey == "cantDo"):
                    for cantDo in range(len(data[key][examKey])):
                        arrayInfos.append(data[key][examKey][cantDo])
                    exames["NãoPraticar"].append(arrayInfos)
                if(examKey == "ludicInfos"):
                    for ludicInfos in range(len(data[key][examKey])):
                         arrayInfos.append(data[key][examKey][ludicInfos])
                    exames["InfosLudicas"].append(arrayInfos)
                if(examKey == "preparations"):
                    for preparations in range(len(data[key][examKey])):
                         arrayInfos.append(data[key][examKey][preparations])
                    exames["Preparos"].append(arrayInfos)
        exames['Exames'].append(data[key]["title"])
        exames["Descrição"].append(data[key]["about"])
    print("==================================")

    print(exames["Exames"][0])
    print("==================================")

    print(exames["Descrição"][0])
    print("==================================")

    print(exames["NãoPraticar"][0])
    print("==================================")

    print(exames["InfosLudicas"][0])
    print("==================================")
    
    print(exames["Preparos"][0])


            

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
    





