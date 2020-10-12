using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

public class Queue {
    public Stack<int> stack1 = new Stack<int>();
    public Stack<int> stack2 = new Stack<int>();

    public void Enqueue(int val) {
        stack1.Push(val);
    }

    public void Dequeue() {
        if(stack2.Count != 0)
            stack2.Pop();
        else {
            while(stack1.Count != 0) {
                stack2.Push(stack1.Pop());
            }
            stack2.Pop();
        }
    }

    public void Print() {
        if(stack2.Count != 0)
            Console.WriteLine(stack2.Peek());
        else {
            while(stack1.Count != 0) {
                stack2.Push(stack1.Pop());
            }
            Console.WriteLine(stack2.Peek());
        }
    }
}

class Solution {
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        var q = int.Parse(Console.ReadLine());
        Queue queue = new Queue();
        
        for(int i = 0; i < q; i++) {
            var query = Console.ReadLine().Split(' ');
            if(query[0] == "1") {
                var num = int.Parse(query[1]);
                queue.Enqueue(num);
            }
            if(query[0] == "2") {
                queue.Dequeue();
            }
            if(query[0] == "3") {
                queue.Print();
            }
        }
    }
}
