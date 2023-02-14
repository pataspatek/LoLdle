import sqlite3

# Create a connection to the database
conn = sqlite3.connect('loldle.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()


def main():
    # Query for all rows in database
    cursor.execute("SELECT * FROM champions")

    # Create a list of all champions
    champ_list = cursor.fetchall()

    # Run this code until the last champ remains
    while len(champ_list) > 1:

        # Choose an action
        print()
        action = (input("Do you want to REMOVE 'r' or CONFIRM 'c'? ")).lower()

        if action == "r":
            champ_list = remove_champs(champ_list)
        
        elif action == "c":
            champ_list = confirm_champs(champ_list)

        else:
            print("Invalid input!")
            continue
        
        # Show the remaining champions
        print()
        print(", ".join(champ[0] for champ in champ_list))

    print(f"Your champion is {champ_list[0][0]}!")


def remove_champs(champ_list):
    """
    Removes champions from the provided list that do not contain a specific substring.

    Parameters: champ_list (list): List of tuples containing champion information.

    Returns: list: A new list of tuples with champions that do not contain the provided substring.
    """

    remove = input("What do you want to remove? ").lower()

    new_list = []

    for champ in champ_list:
        if remove not in champ:
            new_list.append(champ)

    return new_list


def confirm_champs(champ_list):
    """
    Filters champions from the provided list that contain a specific substring.

    Parameters: champ_list (list): List of tuples containing champion information.

    Returns: list: A new list of tuples with champions that contain the provided substring.
    """

    confirm = input("What do you want to confirm? ").lower()

    new_list = []

    for champ in champ_list:
        if confirm in champ:
            new_list.append(champ)
            
    return new_list


if __name__ == '__main__':
    main()
