from Modules.messages import Messages
from Modules.Api import FireBaseApi

import requests

messages = Messages()

class Exames:
    def __init__(self):
        response = FireBaseApi.fetchApi()
 
        self._exames = response
    def searchExames(self, exameInput):
        messages.applicationDivisor()
        messages.optionMessage("\033[1;34m Digite o nome do exame: \033[0m")
        exameInput = input(exameInput).lower()
        title = exameInput.upper()
        index = 0
        if(exameInput not in self._exames["Exames"]):
            messages.errorMessages("empty") 
            messages.spaceDivisor(3)
        else:
            messages.applicationDivisor()
            for key in self._exames.keys():
                if(key == "Exames"):
                    for exame in range(len(self._exames[key])):
                        if(exameInput == self._exames[key][exame]):
                            index = exame
                            exameObj = {}
                            break
                exameObj[key] = self._exames[key][index]
                if(key == "NãoPraticar"):
                    numerator = 1
                    cantPracticeArray = []
                    for cantDo in range(len(self._exames[key][index])):
                        cantPractice = ""
                        cantPractice = f"{numerator}- {self._exames[key][index][cantDo]}"
                        cantPracticeArray.append(cantPractice)
                        numerator += 1
                    cantPracticeString = " ".join(cantPracticeArray)
                    exameObj[key] = cantPracticeString
                if(key == "Preparos"):
                    numerator = 1
                    preparesArray = []
                    for preparesSteps in range(len(self._exames[key][index])):
                        prepares = ""
                        prepares = f"{numerator}- {self._exames[key][index][preparesSteps]}"
                        preparesArray.append(prepares)
                        numerator += 1
                        preparesString = " ".join(preparesArray)
                    exameObj[key] = preparesString
                if(key == "InfosLudicas"):
                    numerator = 1
                    infosArray = []
                    for ludicInfos in range(len(self._exames[key][index])):
                        infos = ""
                        infos = f"{numerator}- {self._exames[key][index][ludicInfos]}"
                        infosArray.append(infos)
                        numerator += 1
                        infosString = " ".join(infosArray)
                    exameObj[key] = infosString
                        
                        
                        
                        
                    
            messages.optionMessage(f"\033[1;34m {title} \033[0m")
            messages.optionMessage(f"""
Exame:{exameObj["Exames"]}
Descrição:{exameObj["Descrição"]}
Não Praticar:{exameObj["NãoPraticar"]}
Informações Lúdicas: {exameObj["InfosLudicas"]}
Preparos: {exameObj["Preparos"]}

                                   """)
            messages.spaceDivisor(3)
        return