import random
import inquirer
my_health = 80
zombi_health = 15

while True:
    questions = [
    inquirer.List('number',
                message="Choose a number",
                choices=[1, 2, 3, 4, 5],
            ),
    ]
    answers = inquirer.prompt(questions)
    my_choice = (answers['number'])

    zombi_choice = random.randint(1, 5)
    print("zombinin secimi", zombi_choice)

    if my_choice == zombi_choice:
        zombi_health -=  my_choice
        print("zombi cani ", zombi_health)
    else:  
        my_health -= zombi_choice
        print("menim canim: ", my_health)

    if my_health<=0 or zombi_health<=0:
        if my_health <= 0:
            print("zombi uddu")
        elif zombi_health <= 0:
            print("men uddum hahaha")
        exit()
        
       





