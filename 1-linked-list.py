"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        counter = 1 
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

        # First attempt: superfluous run time 
        """ 
        counter = 1 
        current = self.head
        if position < 1:
            return None
        while counter != position:
            if current == None:
                return None
            current = current.next
            counter += 1
        else:
            return current
        """
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        current = self.head
        list_length = 1
        while current:
            list_length += 1
            current = current.next
        if position < 2 or position > list_length: # or (invalid new_element)
            return None
        counter = 1
        current = self.head
        while current and counter < position:
            if counter == position - 1:
                new_element.next = current.next 
                current.next = new_element 
                break
            current = current.next
            counter += 1

    def delete(self, value):
        """Delete the first node with a given value."""

        current = self.head
        ll_length = 1

        while current.next:
            current = current.next
            ll_length += 1

        current = self.head
        counter = 1
        while counter != ll_length + 1:
            if current.value == value:
                if counter == 1:
                    self.head = current.next
                    break
                elif counter == ll_length:
                    counter_two = 1
                    current_two = self.head
                    while counter_two <= counter - 1:
                        if counter_two == counter -1:
                            current_two.next = None
                            break
                        current_two = current_two.next
                        counter_two += 1
                else:
                    counter_two = 1
                    current_two = self.head
                    while counter_two <= counter - 1:
                        if counter_two == counter -1:
                            current_two.next = current.next
                            break
                        current_two = current_two.next
                        counter_two += 1
            counter += 1
            current = current.next


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)

# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)