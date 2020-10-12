using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

public class Editor {
    public string sequence = "";
    public Stack<string> memory = new Stack<string>();

    public void append(string word) {
        memory.Push($"LENGTH {word.Length}");
        sequence += word;
    }

    public void delete(int k) {
        var list = sequence.ToList();
        var length = sequence.Length - k;
        var toDelete = String.Join("", list.Skip(length));
        memory.Push(toDelete);
        sequence = String.Join("", list.Take(length));
        // Console.WriteLine($"deleted = {toDelete} and keep = {sequence}");
    }

    public void print(int k) {
        Console.WriteLine(sequence[k]);
    }

    public void undo() {
        var top = memory.Pop().Split(' ');
        if(top[0].Equals("LENGTH")) {
            var index = int.Parse(top[1]);
            sequence = String.Join("", sequence.ToList().Take(sequence.Length - index));
        }
        else {
            sequence += top[0];
        }
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
