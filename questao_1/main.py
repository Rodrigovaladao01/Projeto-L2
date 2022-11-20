from robot import Robot
from inputProcess import InputProcess

def main():
  #CRIAÇÃO DO ROBO E
  rob = Robot(0,0)
  fileCommands = InputProcess('input.txt', rob)

  #PROCESSAMENTO DOS COMANDOS
  fileCommands.processData()

main()