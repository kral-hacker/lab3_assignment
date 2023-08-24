class FlightTable:
    def __init__(self):
        self.data = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        matches = [match for match in self.data if team_name in (match["Team 01"], match["Team 02"])]
        return matches

    def search_by_location(self, location):
        matches = [match for match in self.data if match["Location"] == location]
        return matches

    def search_by_timing(self, timing):
        matches = [match for match in self.data if match["Timing"] == timing]
        return matches

    def display_matches(self, matches):
        if not matches:
            print("No matches found.")
        else:
            for match in matches:
                print(f"Location: {match['Location']}, Team 01: {match['Team 01']}, Team 02: {match['Team 02']}, Timing: {match['Timing']}")

def main():
    flight_table = FlightTable()

    while True:
        print("\nSearch Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            team_name = input("Enter the team name: ")
            matches = flight_table.search_by_team(team_name)
            flight_table.display_matches(matches)
        elif choice == '2':
            location = input("Enter the location: ")
            matches = flight_table.search_by_location(location)
            flight_table.display_matches(matches)
        elif choice == '3':
            timing = input("Enter the timing: ")
            matches = flight_table.search_by_timing(timing)
            flight_table.display_matches(matches)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
