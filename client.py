# lets import some stuff :)
import psutil, socket, guizero
from time import sleep

# define variables
msg = ""                                  # the message that will be sent
serverAddressPort = ("rainbow", 12345)    # server hostname/ip and port
bufferSize = 32                           # buffer size
Run = False                               # just in case we wanna control the main loop

# let's start the sending
def Start_meranie():
  global Run
  Run = True
  stop.enable()
  start.disable()

# do not send any data anymore
def Stop_meranie():
  global Run
  Run = False
  stop.disable()
  start.enable()

# most important function
def Ukonci_meranie():
  exit()

# collect data pack it and send it away
def Read_Send():
  if Run:
    msg = "cpu:"+str(int(psutil.cpu_percent()))
    UDPClientSocket.sendto(msg.encode(), serverAddressPort)

# let's build the gui
aplikacia = guizero.App(title="Meranie CPU na dialku")
okienko = guizero.Box(aplikacia, layout = "grid")
start = guizero.PushButton(okienko, command=Start_meranie, text = "Start", grid = [0,0])
stop = guizero.PushButton(okienko, command=Stop_meranie, text = "Stop", grid = [1,0])
koniec = guizero.PushButton(okienko, command=Ukonci_meranie, text = "Koniec", grid = [2,0])
stop.disable()

# main loop
try:
  UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
  aplikacia.repeat(400, Read_Send)
  aplikacia.display()
      
except KeyboardInterrupt:
 pass
