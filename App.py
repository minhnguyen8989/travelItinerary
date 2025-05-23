"""
Title:       Critical Thinking Assignment #2
Author:      Minh Nguyen
Created:     2025-05-23
Last Edited: 2025-05-23
Description: This program collects travel itinerary details for three destinations.
            For each destination, the user is prompted to input the city name, country name, duration of stay (in days), and budget (in dollars).
            The program validates numeric inputs to ensure they are non-negative and then displays a formatted travel itinerary.
User Input:
        - City name (String)
        - Country name (String)
        - Duration of stay (Integer)
        - Budget (Integer)
Program Output:
        - City name (String)
        - Country name (String)
        - Duration of stay (Integer)
        - Budget (Integer)
"""

# Function to collect and return travel information for a single destination
def get_destination_info(index):
    print(f"\nEnter destination number {index + 1}")

    # Get city and country names from the user input
    city = input("Enter the name of city: ").strip()
    country = input("Enter the name of the country for the city: ").strip()

    # Loop to validate that duration is a non-negative integer and cast input to Integer
    while True:
        try:
            duration = int(input("Enter the duration of stay (in days) for the city: "))
            if duration < 0:
                raise ValueError("Duration should NOT be negative")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number. ({e})")

    # Loop to validate that budget is a non-negative integer and cast input to Integer
    while True:
        try:
            budget = int(input("Enter the budget (in dollars) for the city: "))
            if budget < 0:
                raise ValueError("Budget should NOT be negative")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number. ({e})")

    # Store all destination information input in a dictionary
    destination = {
        "city": city,
        "country": country,
        "duration": duration,
        "budget": budget
    }

    return destination


def main():
    # Loop destinations information 3 times through list
    destinations = [get_destination_info(i) for i in range(3)]

    # Display the structured travel itinerary
    print("\nYour Travel Itinerary:")
    for i, dest in enumerate(destinations, start=1):
        print(f"\nDestination {i}:")
        print(f"  City: {dest['city']}")
        print(f"  Country: {dest['country']}")
        print(f"  Duration of Stay: {dest['duration']} days")
        print(f"  Budget: {dest['budget']} units")


if __name__ == "__main__":
    main()
