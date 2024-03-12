known_users=["Santhosh","Chandhan","Karthik","manoj","jeeva","kariya","suprieee","venki","gurujii"]

while True:
    print("Hi! my name is Travis")

    name=(input("what is your name :").strip().capitalize())
    
    if name in known_users:
        print("Hello {}!".format(name))
        remove=input("would you like to be removed from the system (y/n)? :").lower().strip()
        if remove=="y":
            known_users.remove(name)
            print(known_users)
        elif remove=="n":
                print("No problem, i didn't want you to leave anyway!")
                   
    else:
        print("Hmmm! i dont think have met you yet {}".format(name))
        add_me=input("would you like to be added to the system (y/n)?:").strip().lower()
        if add_me == "y":
              known_users.append(name)
              print(known_users)
        elif add_me== "n":
            print("no worries,see you around!")

         
