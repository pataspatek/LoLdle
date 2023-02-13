import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="loldle"
)

# Create a cursor
mycursor = mydb.cursor()


def main():

    # Close connection
    mycursor.close()
    mydb.close()


def add_data():
    while True:
        # Ask for champion name
        champion_name = input("Enter champion name ('off' to exit): ").capitalize()
        
        if champion_name == "Off":
            show_table()
            break
        
        # Check if champion exists in the table
        mycursor.execute("SELECT COUNT(*) FROM champions WHERE champion=%s", (champion_name, ))
        try:
            result = mycursor.fetchone()[0]
        except IndexError:
            result = 0

        if result == 1:
            print("Champion already exists in table.")
        else:
            # Ask for input for other columns
            gender = input("Enter gender: ").capitalize()
            position = input("Enter position: ").capitalize()
            species = input("Enter species: ").capitalize()
            resource = input("Enter resource: ").capitalize()
            range_type = input("Enter range type: ").capitalize()
            regions = input("Enter regions: ").capitalize()
            release_year = input("Enter release year: ")

            # Insert the data into the table
            sql = "INSERT INTO champions (champion, gender, position, species, resource, range_type, regions, release_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (champion_name, gender, position, species, resource, range_type, regions, release_year)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Champion added to table.")

    print("Adding is over...")


def remove_champ():
    # Ask for champion name
    champion_name = input("Enter champion name to remove: ")

    # Delete the row from the table
    sql = "DELETE FROM champions WHERE champion=%s"
    val = (champion_name.capitalize(), )
    mycursor.execute(sql, val)
    mydb.commit()

    # Print confirmation message
    print(f"{mycursor.rowcount} row(s) deleted")


def show_table():
    # Select all rows from the table
    mycursor.execute("SELECT * FROM champions")

    # Fetch all rows
    rows = mycursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor and connection
    mycursor.close()
    mydb.close()


def how_many_rows():
    # Execute SELECT COUNT(*) statement
    mycursor.execute("SELECT COUNT(*) FROM champions")

    # Get the result
    result = mycursor.fetchone()[0]

    # Print the number of rows
    print("Number of rows:", result)


if __name__ == '__main__':
    main()