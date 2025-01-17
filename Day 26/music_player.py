import os
import time
import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('Day 26/audio.wav')
sound.play()
def pause():
  pygame.mixer.pause()
  
pause()
def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    os.system("cls")
    print("1. Pause Song")
    print()
    pause_song = int(input("Select an option"))
    if pause_song == 1:
      pause()
      return
    else:
      continue

while True:
  # clear the screen 
  os.system("cls")
  # Show the menu
  print("Brandon's Music Player")
  print()
  print("1. Play")
  print("2. Quit")
  print()
  # take user's input
  user_input = int(input("Select an option: "))
  # check whether you should call the play() subroutine depending on user's input
  if user_input == 1:
    play()
  elif user_input == 2:
    exit()
  else:
    print("Please enter a valid choice.")