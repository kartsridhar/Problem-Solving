# Enter your code here. Read input from STDIN. Print output to STDOUT
class Editor:
    sequence = ""
    memory = []

    def _append(self, word):
        self.memory.append(self.sequence)
        self.sequence += word
    
    def _delete(self, k):
        self.memory.append(self.sequence)
        self.sequence = self.sequence[:-k]
    
    def _print(self, k):
        print(self.sequence[k])
    
    def _undo(self):
        self.sequence = self.memory.pop()

if __name__ == '__main__':
    editor = Editor()
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            editor._append(query[1])
        elif query[0] == '2':
            editor._delete(int(query[1]))
        elif query[0] == '3':
            editor._print(int(query[1]) - 1)
        else:
            editor._undo()
