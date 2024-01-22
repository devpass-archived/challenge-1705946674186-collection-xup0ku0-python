class Collection:
    def __init__(self):
        // Add your solution here!

    def add_element(self, element):
        // Add your solution here!

    def remove_element(self, element):
        // Add your solution here!

    def get_element_index(self, element):
        // Add your solution here!

    def get_length(self):
        // Add your solution here!

if __name__ == '__main__':
    collection = Collection()
    collection.add_element(1)
    collection.add_element(2)
    collection.add_element(3)
    print(f'Length: {collection.get_length()}')  # Expected: 3
    print(f'Index of 2: {collection.get_element_index(2)}')  # Expected: 1
    collection.remove_element(2)
    print(f'Length: {collection.get_length()}')  # Expected: 2
    print(f'Index of 2: {collection.get_element_index(2)}')  # Expected: -1
