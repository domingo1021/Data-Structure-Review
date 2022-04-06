# Suppose S is a sorted set of data, x is a data object, and k is a search key.
# The Search, Insert, and Remove operations are called "dictionary" operations.
# The Insert, and Remove, and Minimum (or Maximum) operations are required by priority queues.

class Dictionary:
    def __init__(self, dic) -> None:
        self.dic = dic
    
    def search(self, key):
        if self.dic[key]:
            return self.dic[key]
        else: return None

    def insert(self, x: dict):
        self.dic[list(x.keys())[0]] = list(x.values())[0]
    
    def Delete(self, x: dict):
        pass

    def min(self):
        pass

    def predecessor(self, x:dict):
        pass

    def successorx(self, x:dict):
        pass

    def __str__(self) -> str:
        return f"{self.dic}"

class Sorted_Dictionary(Dictionary):
    def __init__(self, dic) -> None:
        # sort dictionary with value (Achieved by lambda)
        dic = {k:v for k, v in sorted(dic.items(), key= lambda d: d[1])}
        super().__init__(dic)

    def insert(self):
        # priority queue.
        pass

    # def __str__(self) -> str:
    #     return super().__str__()

if __name__ =="__main__":
    dictionary = {"hello":100, "world": 2000, "!!!": 20, "YA":10}
    d_object = Dictionary(dictionary)
    d_object.insert({"wow": 30000})
    print(d_object)

    # d2_object = Sorted_Dictionary(dictionary)
    # print(d2_object)