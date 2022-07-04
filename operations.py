import json


class Operations:
    """Functions for Menu"""

    def show_menu(self):
        print()
        print("+-------------- Menu --------------+")
        print(" 1. Load data from file and display")
        print(" 2. Input & add to the end")
        print(" 3. Display data")
        print(" 4. Save product list to file")
        print(" 5. Search by ID")
        print(" 6. Delete by ID")
        print(" 7. Sort by ID")
        print(" 8. Convert to Binary")
        print(" 9. Load to stack and display")
        print(" 10. Load to queue and display")
        print(" 0. Exit")
        print("+----------------------------------+")
        print()

    def read_file(self, file_path):
        """Get data from a file"""
        # Check if input file path is valid
        try:
            f = open(file_path, "r")
        except FileNotFoundError:
            print("File-path is not correct!")
            return False
        else:
            data = json.loads(f.read())
            f.close()
            return data

    def write_file(self, data):
        """Write to a file"""
        # Check if input file path is valid
        file_path = input("Please enter the output path:\n")
        try:
            f = open(file_path, "w")
        except FileNotFoundError:
            print("Cannot find file-path!")
            return False
        else:
            json_data = json.dumps(data, indent=4)
            f.write(json_data)
            f.close()
            print("Successfully saved file!")
            return True

    def new_product(self):
        """Input new product"""
        id = input("Please enter the new product ID:\n")
        title = input("Please enter the product's name:\n")

        # Make sure input quantity is a number
        while True:
            try:
                quantity = int(input("Please enter the product's quantity:\n"))
            except ValueError:
                print("Please enter a number!")
                continue
            else:
                break

        # Make sure input price is a number
        while True:
            try:
                price = float(input("Please enter the product's price:\n"))
            except ValueError:
                print("Please enter a number!")
                continue
            else:
                break

        return {"ID": id, "Title": title, "Quantity": quantity, "Price": price}

    def show_one(self, product):
        """Show information of one input product"""
        print(f"{'ID':^5} | {'Title':^15} | {'Quantity':^10} | {'Price':^8}")
        print("----------------------------------------------")
        print(f"{product['ID']:<5} | {product['Title']:<15} | {product['Quantity']:^10} | {product['Price']:<10}")

    def to_binary(self, x):
        """Convert an integer to binary using recursive"""
        # Divide number x by 2, get the remaining and a floor result
        # recurse the function with the results until x == 0
        # the first remaining is the last number the return binary
        # the last remaining is the first number of the return binary
        # * 10 so each recursion will move last digits forward 1 index and put next new remaining into last digit
        if x == 0:
            return 0
        else:
            return x % 2 + 10 * self.to_binary(x // 2)
