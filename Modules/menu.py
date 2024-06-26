from Modules.messages import Messages
from Modules.exames import Exames
messages = Messages()
exames = Exames()


class Menu:

    def __init__(self):
        self._menu = {
            "Options": ["1", "2", "3", "4", "0"],
            "Functionalities": ["Contato", "Localização","Busca exames", "Área Kids", "Sair do sistema"]
        }
    
    def showMenuApplication(self):
        messages.welcomeMessage()
        messages.applicationDivisor()
        messages.optionMessage("\033[1;34m Selecione uma das opções disponíveis: \033[0m")

        for i in range(len(self._menu["Options"])):
            print(f"\033[92m{self._menu['Options'][i]}\033[0m - {self._menu['Functionalities'][i]}")


        messages.applicationDivisor()

        return self.inputValidation("", self._menu["Options"])
    

    def inputValidation(self, optionInput, possibleOptions, action = "option"):
        messages.optionMessage("\033[1;34m Sua opção: \033[0m")
        option = input(optionInput)
        while (option not in possibleOptions):
            messages.errorMessages(action)
            option = input(optionInput)
        return option

    def verifyOption(self, selectedOption):
        if selectedOption == "1":
            messages.applicationDivisor()
            messages.optionMessage("\033[1;34m                                            CONTATO INFOCR    \033[0m")
            messages.optionMessage("\033[1;34m Sobre o Instituto\033[0m")
            messages.optionMessage('O Instituto da Criança do Hospital das Clínicas é considerado centro de referência nacional em saúde da criança e atende pacientes do Sistema Único de Saúde e de operadoras de planos de saúde (Saúde Suplementar).')
            
            messages.spaceDivisor(3)
        
            messages.optionMessage("\033[1;34m Contato\033[0m")
            messages.optionMessage("""ICr Instituto da Criança e do Adolescente
(11) 2661-8500
Marcação de consultas – de 2ª a 6ª feira
ICr – (11) 2661-8635, das 7:00 às 16:00
ITACI – (11) 2661-8962 ou (11) 2661-8963, das 14:00 às 16:00
Agendamento de exames – de 2ª a 6ª feira
(11) 2661-8548 ou (11) 2661-8670 ou pessoalmente no 2º andar do ICr – das 11:00 às 15:00""")
        
            messages.spaceDivisor(3)
        
            return
        
    
        if(selectedOption == "2"): 
            messages.applicationDivisor()
            messages.optionMessage("\033[1;34m                                            LOCALIZAÇÃO INFOCR    \033[0m")
            messages.optionMessage("\033[1;34m Endereço\033[0m")
            messages.optionMessage("Av. Dr. Enéas Carvalho de Aguiar, 647 - Cerqueira César, São Paulo - SP, 05403-000")
        
            messages.spaceDivisor(3)
        
            
            return 
        if(selectedOption == "3"): 
            
            exames.searchExames("")
            
        if(selectedOption == "4"): 
            messages.applicationDivisor()
            messages.optionMessage("\033[1;34m                                           Área Kids    \033[0m")
            messages.optionMessage("\033[1;34m Dicas para se divertir durante os exames \033[0m")
            
            messages.optionMessage("""•Leve um brinquedo ou livro para se distrair.
•Imagine que você está em um lugar mágico e divertido.
•Respire fundo e relaxe.
•Converse com o médico se tiver alguma dúvida ou medo.
                                                                      """)

            messages.spaceDivisor(1)

            messages.optionMessage("\033[1;34m Lembre-se! \033[0m")
            
            messages.optionMessage("""•Os exames são rápidos e seguros.
•Eles ajudam os médicos a cuidar da sua saúde.
•Você não está sozinho! Muitas crianças já fizeram esses exames e se divertiram.
                                                                      """)
            
            messages.spaceDivisor(1)

            messages.optionMessage("\033[92m Com essas dicas, você estará pronto para viver grandes aventuras no mundo dos exames!    \033[0m")
            messages.spaceDivisor(3)





           
        






   
