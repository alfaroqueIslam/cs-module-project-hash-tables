class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_head(self, node):
		node.next = self.head
		self.head = node

	def find(self, value):
		cur = self.head

		while cur is not None:
			if cur.value == value:
				return cur

			cur = cur.next

		# If we get here, it's not in the list
		return None
		
	def delete(self, value):

		# Special case of empty list

		if self.head is None:
			return None

		# Special case of deleting the head of the list

		if self.head.value == value:
			old_head = self.head
			self.head = self.head.next
			old_head.next = None
			return old_head

		# General case

		prev = self.head
		cur = self.head.next

		while cur is not None:
			if cur.value == value:
				prev.next = cur.next
				cur.next = None
				return cur

			prev = prev.next
			cur = cur.next

		# If we get here, we didn't find it
		return None
			


	def __str__(self):
		r = ""

		# Traverse the list
		cur = self.head

		while cur is not None:
			r += f'{cur.value}'

			if cur.next is not None:
				r += ' -> '

			cur = cur.next
		
		return r


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [LinkedList()] * self.capacity
        self.items = 0

    def __repr__(self): 
        return f"HashEntry({repr(self.key)},{repr(self.value)})"   


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table)
        


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.items/self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.get_load_factor() > 0.7:
            self.capacity = self.capacity * 2
            self.resize(self.capacity)
        if self.get(key):
            index = self.hash_index(key)
            current = self.table[index].head
            n = 1
            while n == 1:
                if current.key == key:
                    current.value = value
                    n = 0
                current = current.next
        else:
            index = self.hash_index(key)
            self.table[index].insert_at_head(HashTableEntry(key, value))
            self.items += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        current = self.table[index].head
        if current:
            last_node = None
            while current:
                if current.key == key:
                    if last_node:
                        last_node.next = current.next
                    else:
                        self.table[index] = current.next
                last_node = current
                current = current.next
        while self.get(key):
            self.delete(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        try:
            current = self.table[index].head
        except AttributeError:
            return None
        if current:
            while current:
                if current.key == key:
                    return current.value
                current = current.next
        return None



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        lst = [LinkedList()] * new_capacity
        for i in range(len(self.table)):
            if self.table[i].head.key is not None:
                current = self.table[i].head
                n = 1
                while n == 1:
                    index = self.hash_index(current.key)
                    lst[index].insert_at_head(HashTableEntry(current.key, current.value))
                    if current.next == None:
                        n = 0
                    current = current.next
        self.table = lst




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # for i in range(1, 13):
    #     ht.delete(f"line_{i}")
    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
