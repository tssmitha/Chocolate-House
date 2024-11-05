class Chocolate:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class ChocolateHouse:
    def __init__(self):
        self.chocolates = [
            Chocolate("Dark Chocolate", 2.50),
            Chocolate("Milk Chocolate", 2.00),
            Chocolate("White Chocolate", 2.75),
            Chocolate("Chocolate Truffles", 3.50),
            Chocolate("Chocolate Covered Almonds", 4.00),
        ]

    def display_chocolates(self):
        print("\nAvailable Chocolates:")
        for index, chocolate in enumerate(self.chocolates, start=1):
            print(f"{index}. {chocolate}")

    def place_order(self):
        self.display_chocolates()
        choice = input("\nEnter the number of the chocolate you want to order: ")

        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(self.chocolates):
                chocolate_ordered = self.chocolates[choice_index]
                print(f"\nYou have ordered: {chocolate_ordered.name} for ${chocolate_ordered.price:.2f}")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to Choco Haven!")
    chocolate_house = ChocolateHouse()

    while True:
        chocolate_house.display_chocolates()
        chocolate_house.place_order()

        more_orders = input("\nWould you like to order more chocolates? (yes/no): ").strip().lower()
        if more_orders != 'yes':
            print("Thank you for visiting Choco Haven! Goodbye!")
            break

if __name__ == "__main__":
    main()
