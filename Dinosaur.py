class Dino:
    def __init__(self, n, s, e):
        self._name = n
        self._size = s
        self._eats = e
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, n):
        self._name = n
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, s):
        self._size = s
    @property
    def eats(self):
        return self._eats
    @eats.setter
    def eats(self, e):
        self._eats = e
    def meet(self):
        if self.eats == "herbivore":
            return "Hello"
        else:
            return "CHOMP"
        
    def __lt__(self,other):
        if self.name < other.name:
            return True
        else:
            return False

def binarySearch(arr, what):
    first = 0
    last = len(arr) - 1
    mid = (last - first) // 2
    while first <= last:
        if arr[mid].name == what:
            return mid
        elif arr[mid].name < what:
            first = mid + 1
        else:
            last = mid - 1
        mid = (last + first) // 2
    return -1

##MAIN##
JurrasicPark = []
JurrasicPark.append(Dino("Barney", "medium", "herbivore"))
JurrasicPark.append(Dino("Joe", "small", "omnivore"))
JurrasicPark.append(Dino("Chrissy", "large", "carnivore"))
JurrasicPark.append(Dino("Fred", "medium", "carnivore"))
JurrasicPark.append(Dino("Jane", "small", "herbivore"))
JurrasicPark.append(Dino("Max", "large", "omnivore"))
JurrasicPark.sort()
who = input("What dino do you want to meet? ")
i = binarySearch(JurrasicPark, who)
print(JurrasicPark[i].meet())
