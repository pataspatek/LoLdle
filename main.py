import sqlite3


# Create a connection to the database
conn = sqlite3.connect('loldle.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

def main():
    while True:
        gender = input("Enter the champion gender (or 'None'): ")
        position = input("Enter the champion position (or 'None'): ")
        species = input("Enter the champion species (or 'None'): ")
        resource = input("Enter the champion resource (or 'None'): ")
        range_type = input("Enter the champion range type (or 'None'): ")
        regions = input("Enter the champion regions (or 'None'): ")
        release_year = input("Enter the champion release year (or 'None'): ")
        print()

        champion = find_champion(gender=gender, position=position, species=species, resource=resource, range_type=range_type, regions=regions, release_year=release_year)


def find_champion(gender=None, position=None, species=None, resource=None, range_type=None, regions=None, release_year=None, not_resource=None):
    # Build the SQL query based on the user input
    query = "SELECT champion, COUNT(*) AS attribute_count FROM champions WHERE 1=1"
    if gender:
        query += f" AND gender = '{gender.lower()}'"
    if position:
        query += f" AND position = '{position.lower()}'"
    if species:
        query += f" AND species = '{species.lower()}'"
    if resource:
        query += f" AND resource = '{resource.lower()}'"
    if range_type:
        query += f" AND range_type = '{range_type.lower()}'"
    if regions:
        query += f" AND regions = '{regions.lower()}'"
    if release_year:
        query += f" AND release_year = '{release_year}'"
    if not_resource:
        query += f" AND resource != '{not_resource.lower()}'"
    query += " GROUP BY champion ORDER BY attribute_count DESC LIMIT 5"
    
    # Execute the query and fetch the results
    cursor.execute(query)
    result = cursor.fetchall()
    
    # If a champion was found, return its name
    if result:
        for champ in result:
            print(champ[0])
        print()


if __name__ == '__main__':
    main()


