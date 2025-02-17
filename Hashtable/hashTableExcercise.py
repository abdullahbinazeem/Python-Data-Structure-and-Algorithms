class HashTable:
    def __init__(self):
        self.MAX = 20
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def add(self, key, value):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key,value)
                break
        else:
            self.arr[h].append((key,value))
    
    def get(self, key):
        h = self.get_hash(key)
        
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
      

if __name__ == '__main__':
    t = HashTable()
    
    with open("nyc_weather.csv", "r") as f:
        for line in f:
            tokens = line.split(",")
            try:
                print(int(tokens[1]))
                t.add(tokens[0], tokens[1])
            except:
                print("Wrong data type")
    
    print(t.arr)