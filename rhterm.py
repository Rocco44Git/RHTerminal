import sys
import os
import time
import random

sudoer = 0
sayer = 1
while True:
  user = input("RHterm> ")
  if user == "--help":
      print("commands:")
      print("bye = exit")
      print("install (app) = install an app/game")
      print("credits = show credits")
      print("list --prog = list all installable programs")
      print("clear = clear screen")
  if user == "bye":
    break
  if user == "credits":
      print("RH Terminal")
      time.sleep(1)
      print("an app developed by Rocco")
      time.sleep(1)
      print("and his small company:")
      time.sleep(1)
      print("RH Tech")
      time.sleep(1)
      print("made with sh and python code")
      time.sleep(1)
      print("made by RH Tech © in 2024.")
      time.sleep(3)
      os.system('clear')
  if user == "list --prog":
      print("installable apps:")
      print("sudoer")
      print("sayer")
      print("debug")
      print("(end of list)")
  if user == "install sudoer":
      print("searching libraries...")
      time.sleep(3)
      print("found: sudoer: org.sudo.sudoer.")
      print("install? (y/n)")
      yn1 = input()
      if yn1 == "y":
          print("loading...")
          time.sleep(2)
          print("done.")
          time.sleep(0.5)
          print("unpacking util.rh...")
          time.sleep(3)
          print("unpacking sudoer.rh...")
          time.sleep(2.5)
          print("noting util + sudoer as --installable...")
          time.sleep(1.5)
          print("installing --installable...")
          time.sleep(2)
          print("installing bil 13...")
          time.sleep(1)
          print("downloading mantrap.zyx...")
          time.sleep(3)
          print("finishing installation...")
          sudoer = 1
          time.sleep(5)
          print("done!")
  if user == "sudoer" and sudoer == 1:
    print("sudoer: usage:")
    print("sudoer is a tool that brings sudo commands to RH Terminal.")
  if user == "info":
    time.sleep(2)
    print("RH Terminal Deep 14")
    print("running in python")
    print("root = false")
    print("shell: deep14bash")
    print("DE: generic")
    print("GPU: 00:11.0 RH Tech, Inc. Vertigo 1.2 GPU")
    print("Memory: err: UNSTABLE: code: 5124")
  if user == "clear":
      os.system('clear')
  if user == "install sayer":
      print("sayer is under the confirm ammount.")
      time.sleep(1.6)
      print("installation will begin immediately.")
      time.sleep(0.8)
      print("installing sayer...")
      time.sleep(1)
      print("extracting...")
      time.sleep(1)
      print("using 5.14 Mib...")
      time.sleep(1)
      print("installed!")
      sayer = 1
  if user == "sayer" and sayer == 1:
      print("what do you want me to say?")
      say = input()
      os.system('clear')
      print(say)
  if user == "sudo apt update" and sudoer == 1:
      print("connecting to debian.bookworm.org...")
      time.sleep(1)
      print("done!")
      time.sleep(1.5)
      print("connecting to terminal.rhtech.rh...")
      time.sleep(1)
      print("done!")
      time.sleep(2)
      print("all packages are up to date.")
  if "sudo apt install" in user and sudoer == 1:
      print("sorry, but at the minute, sudo apt install is not included in sudoer.")