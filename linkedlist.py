from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, id, title, quantity, price):
        """Add new product node to the end of Linked List"""
        # Check if Linked List is empty
        if self.head is None:
            self.head = Node(id, title, quantity, price, None)
            return True

        # Iterate through each node of Linked List, stop at last node (where node's next is None)
        node = self.head
        while node.next:
            # Check if ID or Title existed in Linked List
            if id == node.id or id == node.next.id:
                print("Invalid ID. Please check again!")
                return False
            if title == node.title or title == node.next.title:
                print("Invalid Title. Please check again!")
                return False

            node = node.next

        # and create a new node (which is next of current node, and point it's next to None)
        node.next = Node(id, title, quantity, price, None)
        return True

    def create_list(self, data):
        """Create a Linked List"""
        for i in data:
            self.add_to_end(i["ID"], i["Title"], i["Quantity"], i["Price"])

    def get_length(self):
        """Count number of nodes in Linked List"""
        node = self.head
        count = 0
        # Move to next node and increase count by 1, return count is length of Linked List
        while node:
            node = node.next
            count += 1
        return count

    def access_node_at_index(self, index):
        """Access node at provided index and return a dictionary of product's data"""
        # Check if input index is within Linked List range
        if index < 0 or index > self.get_length():
            print("Invalid Index")
            return

        node = self.head
        count = 0
        # Iterate to the position that equals input index
        while node:
            if count == index:
                get_data = {"ID": node.id, "Title": node.title, "Quantity": node.quantity, "Price": node.price}
                break
            node = node.next
            count += 1
        # Return a dictionary of product's data
        return get_data

    def access_node_by_id(self, id):
        """Access node's data by input ID"""
        # Check if list is empty
        if self.head is None:
            print("Invalid Data!")
            return

        # Find the node that has id match with input id, and print it
        node = self.head
        while node:
            if node.id == id:
                data = {'ID': node.id, 'Title': node.title, 'Quantity': node.quantity, 'Price': node.price}
                return data
            node = node.next
        # Return False if no id matches
        return False

    def delete_by_id(self, id):
        """Delete a node by provided ID"""
        # Check if list is empty
        if self.head is None:
            print("Invalid Data!")
            return

        # If delete first Node, point head to next node (second node)
        if self.head.id == id:
            self.head = self.head.next
            return True

        # Find the node that has next node's id match with input id
        node = self.head
        while node.next:
            if node.next.id == id:
                print(f"{'ID':^5} | {'Title':^15} | {'Quantity':^10} | {'Price':^8}")
                print("----------------------------------------------")
                print(f"{node.next.id:<5} | {node.next.title:<15} | {node.next.quantity:^10} | {node.next.price:<10}")

                # Point current node to the node after next node to remove next node
                node.next = node.next.next
                return True
            node = node.next
        # Return False if no id matches
        return False

    def add_node(self, node, next_node):
        """Add a Node to Linked List"""
        node.next = next_node

    def sort_by_id(self):
        """Sort products in Linked List by ID"""
        # Check if list has 2 or more nodes to sort
        if self.get_length() > 1:
            node = self.head

            # Create a list of Nodes
            lst = []
            while node:
                lst.append(node)
                node = node.next

            # Sort Nodes list by ID
            lst = sorted(lst, key=lambda node: node.id)

            # Create a new Linked List, add sorted Nodes from Nodes list
            new_ll = LinkedList()
            # Set new Linked List head the first Node of Nodes list
            new_ll.head = lst[0]
            # Iterate through Nodes list to add Nodes to new Linked List
            for i in range(len(lst) - 1):
                new_ll.add_node(lst[i], lst[i + 1])
                # Set last Node point next to None
                if i + 1 == len(lst) - 1:
                    lst[i + 1].next = None
            return new_ll

        # If Linked List has less than 2 nodes, return it
        return self


    def show_list(self):
        """Display products data in Linked List"""
        # Check if Linked List is empty
        if self.head is None:
            print("Invalid Data")
            return

        node = self.head
        # Print product's data with alignment
        print(f"{'ID':^5} | {'Title':^15} | {'Quantity':^10} | {'Price':^8}")
        print("----------------------------------------------")

        # Iterate and print each product's data in Linked List
        while node:
            print(f"{node.id:<5} | {node.title:<15} | {node.quantity:^10} | {node.price:<8}")
            node = node.next


if __name__ == "__main__":
    ll = LinkedList()
    lst = [{'ID': '001', 'Title': 'Apple', 'Quantity': 3, 'Price': 100.0},
           {'ID': '002', 'Title': 'Orange', 'Quantity': 4, 'Price': 90.0},
           {'ID': '003', 'Title': 'Jackfruit', 'Quantity': 5, 'Price': 150.0},
           {'ID': '004', 'Title': 'Avocado', 'Quantity': 10, 'Price': 70.0}]
    for i in lst:
        ll.add_to_end(i['ID'], i['Title'], i['Quantity'], i['Price'])
    ll.show_list()
