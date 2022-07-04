class Node:
    def __init__(self, id, title, quantity, price, next=None):
        """Create a node that contain data of a product"""
        self.id = id
        self.title = title
        self.quantity = quantity
        self.price = price
        self.next = next