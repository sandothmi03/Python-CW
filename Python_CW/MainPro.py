import random

list_of_inputs = []
headers = ["Horse ID", "Horse Name", "Jockey Name", "Age", "Breed", "Wins and Runs", "Group"]

selected_horses = None
TIME_INDEX = None


def ahd():  # Function to add horse details
    while True:
        horse_id = input("\t\tEnter the horse's ID\t\t\t: ")
        if horse_id.isdigit() and len(horse_id) == 3:
            horse_id = int(horse_id)
            if not is_duplicate_horse_id(horse_id):
                break
            else:
                print("\t\tDuplicate input. HorseID should be unique.")
        else:
            print("\t\tInvalid input. HorseID should be a 3-digit number.")

    while is_duplicate_horse_id(horse_id):
        print("\t\tDuplicate input. HorseID should be unique.")
        horse_id = input("\t\tEnter the horse's ID\t\t\t: ")
        if horse_id.isdigit() and len(horse_id) == 3:
            horse_id = int(horse_id)
        else:
            print("\t\tInvalid input. HorseID should be a 3-digit number.")

    while True:
        horse_name = input("\t\tEnter the horse's name\t\t\t: ")
        if horse_name and not any(char.isdigit() for char in horse_name):
            break
        else:
            print("\t\tInvalid input. Horse name should not contain numerical values, and cannot be null.")

    while True:
        jockey_name = input("\t\tEnter the jockey's name\t\t\t: ")
        if jockey_name and not any(char.isdigit() for char in jockey_name):
            break
        else:
            print("\t\tInvalid input. Jockey name should not contain numerical values, and cannot be null.")

    age = None
    while age is None:
        try:
            age = int(input("\t\tEnter the horse's age\t\t\t: "))
            if not (3 < age < 25):
                print("\t\tInvalid input. Age should be a positive integer, must be higher than 3, lower than 25.")
                age = None
        except ValueError:
            print("\t\tInvalid input. Enter an integer for age.")
            age = None

    while True:
        breed = input("\t\tEnter the horse's breed\t\t\t: ")
        if breed and not any(char.isdigit() for char in breed):
            break
        else:
            print("\t\tInvalid input. Breed cannot be null and should not contain numeric characters.")

    won_record = None
    ran_record = None
    while won_record is None or not (0 <= won_record <= ran_record):
        try:
            won_record = int(input("\t\tEnter the number of times horse won\t\t: "))
            ran_record = int(input("\t\tEnter the number of times horse ran\t\t: "))
            if not (0 <= won_record <= ran_record):
                print("\t\t Invalid inputs. Ran record should be bigger than won record")
        except ValueError:
            print("\t\tInvalid input. Enter numeric values for race records.")
            won_record = None
            ran_record = None

    while True:
        horse_group = input("\t\tEnter the horse's group (A, B, C, D)\t: ").upper()
        if horse_group in {'A', 'B', 'C', 'D'}:
            break
        else:
            print("\t\tInvalid input. Enter a valid group (A, B, C, D) and cannot be null.")



    print('\t\tData entered successfully')  # Display success message and store details in the list
    details = [horse_id, horse_name, jockey_name, age, breed, (won_record, ran_record), horse_group]
    list_of_inputs.append(details)

def is_duplicate_horse_id(horse_id):
    try:
        horse_id = int(horse_id)
        return horse_id in [details[0] for details in list_of_inputs]
    except ValueError:
        return False


def uhd(): # Function to update horse details
    global list_of_inputs

    while True:
        update_id = input("Enter the Horse ID to Update: ")
        if update_id.isdigit() and any(details[0] == int(update_id) for details in list_of_inputs):
            break
        else:
            print("Invalid input. Please enter a valid Horse ID.")

    # Remove the horse with the specified ID from the list
    updated_list = [details for details in list_of_inputs if details[0] != int(update_id)]

    # If the lists are the same length, the ID was not found
    if len(updated_list) == len(list_of_inputs):
        print(f"No horse found with ID {update_id}. Update operation aborted.")
    else:
        list_of_inputs = updated_list

    while True:
        horse_id = input("\t\tEnter the horse's ID\t\t\t: ")
        if horse_id.isdigit() and len(horse_id) == 3:
            horse_id = int(horse_id)
            if not is_duplicate_horse_id(horse_id):
                break
            else:
                print("\t\tDuplicate input. HorseID should be unique.")
        else:
            print("\t\tInvalid input. HorseID should be a 3-digit number.")

    while is_duplicate_horse_id(horse_id):
        print("\t\tDuplicate input. HorseID should be unique.")
        horse_id = input("\t\tEnter the horse's ID\t\t\t: ")
        if horse_id.isdigit() and len(horse_id) == 3:
            horse_id = int(horse_id)
        else:
            print("\t\tInvalid input. HorseID should be a 3-digit number.")

    while True:
        horse_name = input("\t\tEnter the horse's name\t\t\t: ")
        if horse_name and not any(char.isdigit() for char in horse_name):
            break
        else:
            print("\t\tInvalid input. Horse name should not contain numerical values, and cannot be null.")

    while True:
        jockey_name = input("\t\tEnter the jockey's name\t\t\t: ")
        if jockey_name and not any(char.isdigit() for char in jockey_name):
            break
        else:
            print("\t\tInvalid input. Jockey name should not contain numerical values, and cannot be null.")

    age = None
    while age is None:
        try:
            age = int(input("\t\tEnter the horse's age\t\t\t: "))
            if not (3 < age < 25):
                print("\t\tInvalid input. Age should be a positive integer, must be higher than 3, lower than 25.")
                age = None
        except ValueError:
            print("\t\tInvalid input. Enter an integer for age.")
            age = None

    while True:
        breed = input("\t\tEnter the horse's breed\t\t\t: ")
        if breed and not any(char.isdigit() for char in breed):
            break
        else:
            print("\t\tInvalid input. Breed cannot be null and should not contain numeric characters.")

    won_record = None
    ran_record = None
    while won_record is None or not (0 <= won_record <= ran_record):
        try:
            won_record = int(input("\t\tEnter the number of times horse won\t\t: "))
            ran_record = int(input("\t\tEnter the number of times horse ran\t\t: "))
            if not (0 <= won_record <= ran_record):
                print("\t\t Invalid inputs. Ran record should be bigger than won record")
        except ValueError:
            print("\t\tInvalid input. Enter numeric values for race records.")
            won_record = None
            ran_record = None

    while True:
        horse_group = input("\t\tEnter the horse's group (A, B, C, D)\t: ").upper()
        if horse_group in {'A', 'B', 'C', 'D'}:
            break
        else:
            print("\t\tInvalid input. Enter a valid group (A, B, C, D) and cannot be null.")


    print('\t\tData entered successfully') # Display success message and store updated details in the list
    details = [horse_id, horse_name, jockey_name, age, breed, (won_record, ran_record), horse_group]
    list_of_inputs.append(details)


def dhd():  # Function to delete horse details
    global list_of_inputs

    while True:
        delete_id = input("Enter the Horse ID to Delete: ")
        if delete_id.isdigit() and any(details[0] == int(delete_id) for details in list_of_inputs):
            break
        else:
            print("Invalid input. Please enter a valid Horse ID.")

    print('Horse_id deleted successfully')
    list_of_inputs = [details for details in list_of_inputs if details[0] != int(delete_id)]


def print_details_table(headers, data):  # Function to print horse details table
    for details in data:
        for header, value in zip(headers, details):
            print(f"{header}: {value}", end=", ")
        print("\n" + "-" * 120)  # Separating lines between sets

def vhd():  # Function to view horse details table
    # Bubble sort to sort list_of_inputs based on Horse ID
    n = len(list_of_inputs)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if list_of_inputs[j][0] > list_of_inputs[j + 1][0]:
                list_of_inputs[j], list_of_inputs[j + 1] = list_of_inputs[j + 1], list_of_inputs[j]

    print("Horse details sorted by Horse ID:")
    print_details_table(headers, list_of_inputs)
    print('\n')


def shd():  # Function to save horse details to a text file
    try:
        with open("Horse_Details.txt", "a") as file:
            file.write(",".join(headers) + "\n")  # Writing headers to the file
            for details in list_of_inputs:
                details_str = ", ".join(f"{header}: {value}" for header, value in zip(headers, details))
                file.write(details_str + "\n")
                file.write("-" * 120 + "\n")
        print("\tData saved successfully!")
    except Exception as e:
        print(f"Error saving data: {e}")


def print_selected_horses(headers, selected_horses):  # Function to print selected horses for the major round
    print("\n\t\tSelected Horses for the Major Round\n")
    print("\t".join(headers))
    for horse_details in selected_horses:
        print_details_table(headers, [horse_details])

def sdd(): # Function to select horses randomly for the major round
    global list_of_inputs

    # Check if there are enough horses
    if len(list_of_inputs) < 20:
        print("Not enough horses to proceed with the major round. Please add more horses.")
        return None

    # Organize horses into groups based on a group identifier
    grouped_horses = {}
    for horse_details in list_of_inputs:
        # Assuming 'Group' is at index 6 in the list (adjust based on the actual structure)
        group_id = horse_details[6]
        if group_id not in grouped_horses:
            grouped_horses[group_id] = []
        grouped_horses[group_id].append(horse_details)

    # Check if there are enough horses in each group
    if any(len(group) < 1 for group in grouped_horses.values()):
        print("Not enough horses in each group to proceed with the major round. Please add more horses to each group.")
        return

    selected_horses = [random.choice(group) for group in grouped_horses.values()]

    print_selected_horses(headers, selected_horses)
    return selected_horses

winning_horses = []  # New list to store winning horses' details

def whd(selected_horses):  # Function to display winning horses' details
    global winning_horses, TIME_INDEX

    # Check if there are enough horses
    if selected_horses is None or len(selected_horses) < 3:
        print("Not enough horses to determine the top 3 winners.")
        return

    # Assign a random time between 0 to 90s for each selected horse
    for horse in selected_horses:
        horse.append(round(random.randint(20, 120) / 10) * 10)  # Round to nearest multiple of 10

    # Define the index for time in the horse details
    TIME_INDEX = len(selected_horses[0]) - 1

    top_3_winners = selected_horses[:3]
    for horse in selected_horses[3:]:
        if len(horse) > TIME_INDEX and len(top_3_winners[0]) > TIME_INDEX:
            if horse[TIME_INDEX] < top_3_winners[0][TIME_INDEX]:
                top_3_winners[2] = top_3_winners[1]
                top_3_winners[1] = top_3_winners[0]
                top_3_winners[0] = horse
            elif horse[TIME_INDEX] < top_3_winners[1][TIME_INDEX]:
                top_3_winners[2] = top_3_winners[1]
                top_3_winners[1] = horse
            elif horse[TIME_INDEX] < top_3_winners[2][TIME_INDEX]:
                top_3_winners[2] = horse
        else:
            print("Not enough elements in horse details to access TIME_INDEX.")
            print("Horse details:", horse)

    # Display the details of the top 3 winners with their times
    if TIME_INDEX is not None:
        print_top_3_winners_with_times(headers, top_3_winners)

    # Save the winning horses
    winning_horses = top_3_winners


def print_top_3_winners_with_times(headers, top_3_winners):
    print("\nTop 3 Winners:")
    print("{:<5} {:<15} {:<10} {:<10}".format("Rank", "Horse", "Time (s)", "Time"))  # Adjust format based on your data structure

    # Manually find the winners in ascending order by rank
    rank_1, rank_2, rank_3 = None, None, None
    for winner in top_3_winners:
        if rank_1 is None or winner[TIME_INDEX] < rank_1[TIME_INDEX]:
            rank_3 = rank_2
            rank_2 = rank_1
            rank_1 = winner
        elif rank_2 is None or winner[TIME_INDEX] < rank_2[TIME_INDEX]:
            rank_3 = rank_2
            rank_2 = winner
        elif rank_3 is None or winner[TIME_INDEX] < rank_3[TIME_INDEX]:
            rank_3 = winner

    for rank, winner in enumerate([rank_1, rank_2, rank_3], start=1):
        print("{:<5} {:<15} {:<10} {:<10}".format(rank, winner[0], winner[TIME_INDEX], convert_to_seconds(winner[TIME_INDEX])))

def convert_to_seconds(time_in_seconds):
    return f"{time_in_seconds} s"


def vwh():
    global winning_horses, TIME_INDEX

    if TIME_INDEX is None or not winning_horses:
        print("No winning horses data available. Please run the WHD (Display Winning Horses) option first.")
        return

    for i in range(len(winning_horses)):
        for j in range(i + 1, len(winning_horses)):
            if winning_horses[j][TIME_INDEX] < winning_horses[i][TIME_INDEX]:
                # Swap the horses if the j-th horse finished earlier than the i-th horse
                winning_horses[i], winning_horses[j] = winning_horses[j], winning_horses[i]

    # Display the details of the top 3 winning horses
    print("\nVisualization of Winning Horses:")
    for rank, horse in enumerate(winning_horses, start=1):
        time_in_seconds = horse[TIME_INDEX]
        stars = '*' * (time_in_seconds // 10)  # One '*' for every 10 seconds
        print(f"Horse ID: {horse[0]}, {horse[1]}: {stars} {time_in_seconds}s ({rank}st Place)")


def esc():
    print("Exiting the program.")

race_started = False  # Add this line to initialize the variable

while True:
    print("""
            \n\t\t\t\t\t\t Menu
            \n\t\tType AHD for adding horse details
            \tType UHD for updating horse details
            \tType DHD for deleting horse details
            \tType VHD for viewing the registered horses' details table
            \tType SHD for saving the horse details to the text file
            \tType SDD for selecting four horses randomly for the major round
            \tType WHD for displaying the winning horses' details
            \tType VWH for visualizing the time of the winning horses
            \tType ESC to exit the program 
        """)
    opt = input("\n\tType the option you want : ")
    opt = opt.upper()

    if opt == 'AHD' and not race_started:
        ahd()
    elif opt == 'UHD' and not race_started:
        uhd()
    elif opt == 'DHD' and not race_started:
        dhd()
    elif opt == 'VHD':
        vhd()
    elif opt == 'SHD' and not race_started:
        shd()
    elif opt == 'SDD' and not race_started:
        selected_horses = sdd()
        race_started = True  # Set the flag to True after starting the race
    elif opt == 'WHD':
        whd(selected_horses)
    elif opt == 'VWH':
        vwh()
    elif opt == 'ESC':
        esc()
        break
    else:
        print("\nInvalid option, Enter a valid option again")
        continue
