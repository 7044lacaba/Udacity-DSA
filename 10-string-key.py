"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        a = str(ord(string[0]))
        b = str(ord(string[1]))
        hash = int(a + b)
        hash_index = hash - 1

        self.table[hash_index] = {hash:string}



    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        a = str(ord(string[0]))
        b = str(ord(string[1]))
        hash = int(a + b)
        hash_index = hash - 1

        for item in self.table:
            try:
                x = item[hash]
                return hash
            except:
                pass
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        a = str(ord(string[0]))
        b = str(ord(string[1]))
        hash = int(a + b)

        return hash
    
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
