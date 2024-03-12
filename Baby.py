from random import choice

questions=["why the sky is blue?:"
          ,"why is there a face on the moon?:"
          ,"where are all the dinosaurs?:"]
question =choice(questions)
answer =input(question).strip().lower()
while answer !="just because":
     answer =input("why?:").strip().lower()
print("ohh....okayyy")
