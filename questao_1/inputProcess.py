class InputProcess:
    def __init__(self, nameFile, robot):
        self.nameFile = nameFile
        self.robot = robot

        self.heightLimit = 0
        self.widthLimit = 0
        self.commandRobot = []

    def inputData(self):
        file = open(self.nameFile,"r")

        #INICIO DA LEITURA DO ARQUIVO
        size = file.readline().split("\n")[0].split(" ")
        self.heightLimit = size[0]
        self.widthLimit = size[1]	

        #OS COMANDOS DO ROBO SAO LIDOS E ARMAZENADOS EM UMA LISTA
        self.commandRobot = file.readlines()

    def processData(self):
        #LEITURA DOS COMANDOS DO ROBO
        self.inputData()

        #VERIFICACAO DOS COMANDOS DO ROBO
        if(len(self.commandRobot) == 0):
            return

        #LOOP PARA EXECUCAO DOS COMANDOS DO ROBO
        for element in self.commandRobot:
                #SEPARACAO DOS COMANDOS
                if(element[0].isdigit()):          
                    #EXIBE A POSICAO DO ROBO
                    self.robot.printRobot()

                    size = element.split("\n")[0].split(" ")
                    self.heightLimit = size[0]
                    self.widthLimit = size[1]

                    #REINICIA A POSICAO DO ROBO
                    self.robot.setPosition(0, 0)
                    self.robot.resetRotation()
                
                #EXECUCAO DOS COMANDOS
                else:
                    element = list(element.split("\n")[0])
                
                    for orientation in element:
                        self.robot.move(int(self.widthLimit), int(self.heightLimit), orientation)
        
        #EXIBE A POSICAO FINAL DO ROBO
        self.robot.printRobot()
        
