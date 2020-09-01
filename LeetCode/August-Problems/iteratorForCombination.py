def generateCombinations(string, length, lastSeen=[]):
    combinations = []
    if len(lastSeen) == length:
        return [lastSeen]
    
    for key, val in enumerate(string):
        stringCopy = lastSeen.copy()
        stringCopy.append(val)
        combinations += generateCombinations(string[key+1:], length, stringCopy)  
        print(combinations)
            
    return [''.join(i) for i in combinations]

def generateCombinationsAlt(string, length):
    return sorted([''.join(c) for c in itertools.combinations(string, length)])

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = generateCombinations(characters, combinationLength)
        self.length = len(self.combinations)
        self.position = -1

    def next(self) -> str:
        self.position += 1
        if self.position <= self.length:
            return self.combinations[self.position]
        
    def hasNext(self) -> bool:
        return self.position + 1 < self.length

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()