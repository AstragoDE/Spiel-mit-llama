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





def main():
    d




main()