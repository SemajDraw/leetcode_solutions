"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string
using the following formula.
(ASCII Value of First Letter * 100) + ASCII Value of Second Letter
ord() ascii value of character
chr() character of ascii value
"""


class HashTable(object):

    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        location = self.calculate_hash_value(string)
        if self.table[location] is None:
            self.table[location] = [string]
        else:
            self.table[location].append(string)

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        value = self.calculate_hash_value(string)
        if self.table[value]:
            if string in self.table[value]:
                return value
        return -1

    @staticmethod
    def calculate_hash_value(string):
        """Helper function to calulate a
        hash value from a string."""
        return (ord(string[0]) * 100) + ord(string[1])


if __name__ == '__main__':
    # Setup
    hash_table = HashTable()

    # Test calculate_hash_value
    # Should be 8568
    print(hash_table.calculate_hash_value('UDACITY'))

    # Test lookup edge case
    # Should be -1
    print(hash_table.lookup('UDACITY'))

    # Test store
    hash_table.store('UDACITY')
    # Should be 8568
    print(hash_table.lookup('UDACITY'))

    # Test store edge case
    hash_table.store('UDACIOUS')
    # Should be 8568
    print(hash_table.lookup('UDACIOUS'))
