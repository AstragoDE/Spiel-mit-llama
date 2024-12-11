#alt + z

#import pygame

#Variabeln

lama_url = "https://212.132.112.15:11434/api/chat"

lama_model = "llama3.1:8b-instruct-q5.K_M"

prompt = "p"

prompt__sp = "sp"

prompt_bew = "bew"

prompt1 = "1"

prompt2 = "2"

prompt3 = "3"

prompt4 = "4"

antwort = "a"

data = {
    "model":lama_model,
    "messages":[
        {
            "role":"system",
            "content":prompt,
        }
    ],
    "stream":False,
}




# Meine Sachen
ort="title_screen"
global ort
global gespräch

def char_1

def gespräch():
  print(1)
  

def laufen():
  if ort == "title_screen":
    if mouse and mouse:
      ort = "bedroom_1"
  if ort == "bedroom_1":
    if mouse and mouse:
      ort = "hallway_1"
      

def GoderL():
  if gespräch==0:
    laufen()
  if gespräch==1:
    gespräch()


while True:
  mouse_x, mouse_y = pygame.mouse.get_pos()
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
  Hintergrund()
  pygame.display.update()

def main():
    d




main()
