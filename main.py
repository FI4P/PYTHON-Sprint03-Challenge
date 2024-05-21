
#Imports
from Modules.menu import Menu
from Modules.messages import Messages
menuApplication = Menu()
applicationMessages = Messages()

def main():
    while True:
        menuId = menuApplication.showMenuApplication()
        if menuId == "0":
            break
        menuApplication.verifyOption(menuId)
    
    applicationMessages.applicationDivisor()
    applicationMessages.byeMessage()
    
     
main()
    
    
    
    





