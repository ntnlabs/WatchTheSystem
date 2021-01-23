import psutil, socket, guizero
from time import sleep

msg = ""
serverAddressPort = ("rainbow", 12345)
bufferSize = 32
Run = False

def Start_meranie():
  global Run
  Run = True
  stop.enable()
  start.disable()

def Stop_meranie():
  global Run
  Run = False
  stop.disable()
  start.enable()

def Ukonci_meranie():
  exit()

def Read_Send():
  if Run:
    msg = "cpu:"+str(int(psutil.cpu_percent()))
    UDPClientSocket.sendto(msg.encode(), serverAddressPort)

aplikacia = guizero.App(title="Meranie CPU na dialku")
okienko = guizero.Box(aplikacia, layout = "grid")
start = guizero.PushButton(okienko, command=Start_meranie, text = "Start", grid = [0,0])
stop = guizero.PushButton(okienko, command=Stop_meranie, text = "Stop", grid = [1,0])
koniec = guizero.PushButton(okienko, command=Ukonci_meranie, text = "Koniec", grid = [2,0])
stop.disable()

try:
  UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
  aplikacia.repeat(400, Read_Send)
  aplikacia.display()
      
except KeyboardInterrupt:
 pass
