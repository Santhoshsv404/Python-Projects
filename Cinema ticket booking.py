#Project---Cinema Ticket Booking

films={
          "Finding Dory":[3,5],
          "Bourne":[18,5],
          "Tarzan":[15,1],
          "Ghost Busters":[12,5]
          }
while True:
    choice=input('which film would you like to watch?:').strip().title()

    if choice in films:
           age=int(input("How old are you?:").strip())

          #check user age

           if age>=films[choice][0]:
               
               #check enough seats
               num_seats=films[choice][1]

               if num_seats>0:
                   print("Enjoy the film!")
                   films[choice][1]=films[choice][1]-1
               else:
                       print("sorry we are sold out")
           else:
                    print("Your too young to see that film!")  
      
    else:
            print("we don't have that film...")


