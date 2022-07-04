from linkedlist import LinkedList
from operations import Operations
from stack_and_queue import Stack, Queue


def menu():
    func = Operations()
    print()
    print('WELCOME TO PRODUCT MANAGEMENT PROGRAM')

    while True:

        func.show_menu()

        try:
            choice = int(input("Enter a function you would like to execute:\n"))
        except ValueError:
            print("Please enter a number displayed on the Menu")
            continue
        else:
            if choice < 0 or choice > 10:
                print("Please enter a number displayed on the Menu")
                continue

        # 0. ========================================================================
        if choice == 0:
            print("Exit.")
            print("Thank you. See you again!")
            break

        # 1. ========================================================================
        elif choice == 1:
            print("Choice 1: Load data from file and display")
            file_path = input("Please enter the file path:\n")
            data = func.read_file(file_path)
            # Check if file path is correct
            if not data:
                continue
            else:
                print("File is loaded successfully!")
                print()
                ll = LinkedList()
                ll.create_list(data)
                ll.show_list()

        # 2. ========================================================================
        elif choice == 2:
            print("Choice 2: Input & add to the end")
            data = func.new_product()

            # Check if Linked List has been created
            try:
                add_product = ll.add_to_end(data["ID"], data["Title"], data["Quantity"], data["Price"])
            except UnboundLocalError:
                # Create a Linked List manually if one has not been created
                invalid = input("Linked List has not been created. Would you like to create a Linked List?\n")
                if invalid[0].lower() == "y":
                    ll = LinkedList()
                    add_product = ll.add_to_end(data["ID"], data["Title"], data["Quantity"], data["Price"])
                else:
                    continue

            if not add_product:
                continue

            print("Product added successfully!")

        # 3. ========================================================================
        elif choice == 3:
            print("Choice 3: Display data")
            # If data has not been input (Choice 1 has not been made)
            try:
                ll.show_list()
            # notify and go back to menu
            except UnboundLocalError:
                print("Invalid Data!")
                continue

        # 4. ========================================================================
        elif choice == 4:
            print("Choice 4: Save product list to file")
            data = []
            try:
                for i in range(ll.get_length()):
                    new = ll.access_node_at_index(i)
                    data.append(new)
            except UnboundLocalError:
                print("Invalid Data!")
                continue
            else:
                to_write = func.write_file(data)
                # If file path is not valid
                if not to_write:
                    continue

        # 5. ========================================================================
        elif choice == 5:
            print("Choice 5: Search by ID")
            search_id = input("Please enter product ID:\n")
            try:
                product = ll.access_node_by_id(search_id)
            except UnboundLocalError:
                print("Invalid Data Source! Please input data first!")
                continue
            else:
                if not product:
                    print("ID is not in the dataset")
                    print("-1")
                else:
                    func.show_one(product)

        # 6. ========================================================================
        elif choice == 6:
            print("Choice 6: Delete by ID")
            try:
                delete_id = input("Please enter product ID:\n")
            except UnboundLocalError:
                print("Invalid Data Source! Please input data first!")
                continue
            else:
                delete_data = ll.delete_by_id(delete_id)
                if not delete_data:
                    print("ID is not in the dataset!")
                else:
                    print("The product is removed from the dataset successfully!")

        # 7. ========================================================================
        elif choice == 7:
            print("Choice 7: Sorted by ID")
            try:
                ll = ll.sort_by_id()
            except UnboundLocalError:
                print("Invalid Data!")
                continue
            else:
                ll.show_list()

        # 8. ========================================================================
        elif choice == 8:
            print("Choice 8: Convert to binary")
            try:
                id = input("Please enter product ID:\n")
                data = ll.access_node_by_id(id)
            except UnboundLocalError:
                print("Invalid Data Source! Please input data first!")
                continue
            else:
                if not data:
                    print("ID is not in the dataset")
                else:
                    func.show_one(data)
                    binary = func.to_binary(data["Quantity"])
                    print(f"Convert quantity to binary: {binary}")

        # 9. ========================================================================
        elif choice == 9:
            print("Choice 9: Load to stack and display")
            st = Stack()
            data = func.read_file(file_path)
            for i in data:
                st.add_top(i)
            print(f"{'ID':^5} | {'Title':^15} | {'Quantity':^10} | {'Price':^8}")
            print("----------------------------------------------")
            for n in range(st.size()):
                top = st.pop_top()
                print(f"{top['ID']:<5} | {top['Title']:<15} | {top['Quantity']:^10} | {top['Price']:^8}")

        # 10. ========================================================================
        elif choice == 10:
            print("Choice 10: Load to queue and display")
            q = Queue()
            data = func.read_file(file_path)
            for i in data:
                q.add_new(i)
            print(f"{'ID':^5} | {'Title':^15} | {'Quantity':^10} | {'Price':^8}")
            print("----------------------------------------------")
            for m in range(q.size()):
                first = q.pop_first()
                print(f"{first['ID']:<5} | {first['Title']:<15} | {first['Quantity']:^10} | {first['Price']:^8}")


if __name__ == "__main__":
    menu()