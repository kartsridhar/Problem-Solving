using System;
using System.Collections.Generic;
using System.IO;

public class Editor {
    public string sequence = "";
    public Stack<string> memory = new Stack<string>();

    public void append(string word) {
        memory.Push(sequence);
        sequence += word;
    }

    public void delete(int k) {
        memory.Push(sequence);
        sequence = sequence.Substring(0, sequence.Length - k);  
    }

    public void print(int k) {
        Console.WriteLine(sequence[k]);
    }

    public void undo() {
        sequence = memory.Pop();
    }
}

class Solution {
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        Editor editor = new Editor();
        
        int q = int.Parse(Console.ReadLine());
        for(var i = 0; i < q; i++) {
            var query = Console.ReadLine().Split(' ');
            if(query[0] == "1") {
                editor.append(query[1]);
            }
            else if(query[0] == "2") {
                int k = int.Parse(query[1]);
                editor.delete(k);
            }
            else if(query[0] == "3") {
                int k = int.Parse(query[1]) - 1;
                editor.print(k);
            }
            else {
                editor.undo();
            }
        }
    }
}
