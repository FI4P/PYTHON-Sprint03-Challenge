import requests


class FireBaseApi:
    @staticmethod
    def fetchApi():
        endpoint = 'https://infocr-fiap-1espr-default-rtdb.firebaseio.com/exams.json'
        try:
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
                    exames['Exames'].append(data[key]["title"].lower())
                    exames["Descrição"].append(data[key]["about"])

                return exames
        except:
            print("Error ao fazer solicitação")
            