class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size
    
    def __hash(self, key):
        pass

    def set_item(self, key, value):
        index  = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index  = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        
        return None