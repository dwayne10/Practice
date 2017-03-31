class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index_to_num = {}
        self.num_to_index = {}
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.num_to_index:
            self.num_to_index[val] = self.length
            self.index_to_num[self.length] = val
            self.length += 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.num_to_index:
            i = self.num_to_index[val]
            if i == self.length - 1:
                del self.num_to_index[val]
                del self.index_to_num[i]
            else:
                # replace it with the last element
                last_num = self.index_to_num[self.length - 1]
                del self.index_to_num[self.length - 1]
                self.num_to_index[last_num] = i
                self.index_to_num[i] = last_num
                del self.num_to_index[val]
            self.length -= 1

            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.length == 0:
            return None
        import random
        random_index = random.randint(0, self.length - 1)
        return self.index_to_num[random_index]
