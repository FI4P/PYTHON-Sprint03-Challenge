from Modules.messages import Messages
import requests

messages = Messages()

class Exames:
    def __init__(self):
        self._exames = {
           "Exame": ["hemograma", "raio x", "ressonancia magnetica"],
           "Sigla" : ["HEMO", "RX", "RM"],
           "Seção" : ["HE", "BIO", "BIO"],
           "Descrição": ["O hemograma é um exame de sangue que avalia diversos componentes do sangue, como glóbulos vermelhos, glóbulos brancos, plaquetas e hemoglobina. Ele é usado para diagnosticar diversas doenças, como anemia, infecções, leucemia e problemas de coagulação sanguínea.", "O raio-X é um exame de imagem que utiliza radiação para visualizar ossos, órgãos e tecidos do corpo. Ele é usado para diagnosticar diversas doenças, como fraturas, pneumonia, tumores e doenças cardíacas." , "A ressonância magnética (RM) é um exame de imagem que utiliza um campo magnético e ondas de rádio para gerar imagens detalhadas do corpo. Ela é usada para diagnosticar diversas doenças, como tumores, doenças musculares e articulares, problemas na coluna vertebral e doenças do cérebro."] 
        }
    
    def searchExames(self, exameInput):
        messages.applicationDivisor()
        messages.optionMessage("\033[1;34m Digite o nome do exame: \033[0m")
        exameInput = input(exameInput).lower()
        title = exameInput.upper()
        index = 0
        if(exameInput not in self._exames["Exame"]):
            messages.errorMessages("empty")
            messages.spaceDivisor(3)
        else:
            messages.applicationDivisor()
            for key in self._exames.keys():
                if(key == "Exame"):
                    for exame in range(len(self._exames[key])):
                        if(exameInput == self._exames[key][exame]):
                            index = exame
                            exameObj = {}
                            break
                exameObj[key] = self._exames[key][index]
            messages.optionMessage(f"\033[1;34m {title} \033[0m")
            messages.optionMessage(f"""
Exame:{exameObj["Exame"]}
Sigla:{exameObj["Sigla"]}
Seção:{exameObj["Seção"]}
Descrição:{exameObj["Descrição"]}
                                   """)
            messages.spaceDivisor(3)
        return
            
                
                        
              