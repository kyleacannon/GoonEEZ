

def create_step():
    item_name = input(f"youve reached the CREATE module in commands, create a title for the thing you are about to create \n")
    local_input = input(f"youve reached the CREATE module in commands, what would you like to create \n")

    if local_input == 'task':
        item_rating = input('what is the level of importance for your task on a scale of 1-10')
        #create a task in the csv with name, type, rating, identifier(PK, or hash), UTC time and date
        #define later for simplicitiy

    elif local_input == 'project':
        item_rating = input('what is the level of importance for your task')
        #create a project in the csv with name, type, rating, identifier(PK, or hash), UTC time and date
        #define later for simplicitiy

    #LATER IN COMPLETE LINK TO OTHER TASK TO ADD ONTO TASK LIST
    elif local_input == 'conditional':
        item_rating = input('what is the level of importance for your task')
        conditional_task_name = input('what are you waiting on to get this started...')
        #create a conditional in the csv with name, type, rating, identifier(PK, or hash), UTC time and date
        #also create regular task with conditional name, highest rating
        #define later for simplicitiy

    else:
        print('we did not understand what you said refer to the docs')
        return
    return
