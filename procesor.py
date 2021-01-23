#!/usr/bin/env python

import rainbowhat as rh
import time
import random
import socket

running = True

@rh.touch.A.press()
def touch_a(channel):
 global running
 running = False


rh.rainbow.clear()
rh.rainbow.show()
rh.display.clear()
rh.display.show()

cpu_load = 1

try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  server_address = ('', 12345)
  sock.bind(server_address)
  sock.setblocking(0)
  Got_Data = False
  while running:
    Got_Data = False
    try:
      data, address = sock.recvfrom(32)
      Got_Data = True
    except socket.error:
      pass

    if ( Got_Data == True):
      clean_data = data.decode()
      type,cpu_str = clean_data.split(":")
      cpu_load = int(cpu_str)
      if (type == "cpu"):
        rh.display.clear()
        rh.display.print_str(cpu_str)
        rh.display.show()
        rh.rainbow.clear()
        if ( cpu_load < 15):
          rh.rainbow.set_pixel(0, 1, 8, 1)
        if ( cpu_load > 15):
          rh.rainbow.set_pixel(0, 1, 16, 1)
        if ( cpu_load > 30):
          rh.rainbow.set_pixel(1, 1, 16, 1)
        if ( cpu_load > 45):
          rh.rainbow.set_pixel(2, 16, 8, 1)
        if ( cpu_load > 60):
          rh.rainbow.set_pixel(3, 16, 8, 1)
        if ( cpu_load > 75):
          rh.rainbow.set_pixel(4, 16, 1, 1)
        if ( cpu_load > 90):
          rh.rainbow.set_pixel(5, 16, 1, 1)
        if ( cpu_load > 99):
          rh.rainbow.set_pixel(6, 64, 1, 1)
        rh.rainbow.show()
    time.sleep(0.1)

except KeyboardInterrupt:
 pass

rh.rainbow.clear()
rh.rainbow.show()
rh.display.clear()
rh.display.show()
