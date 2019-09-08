/*
// Sample code to perform I/O:

name = Console.ReadLine();                  // Reading input from STDIN
Console.WriteLine("Hi, {0}.", name);        // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
using System;
using System.Collections;
using System.Linq;

namespace HackerEarth
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution();
        }
        private static void Solution()
        {
            int n = Convert.ToInt32(Console.ReadLine());
            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            Array.Sort(arr);
            Stack stack = new Stack();
            for(int i = 0; i < n; i++)
            {
                stack.Push(arr[i]);
            }
            for(int j = n-1; j >= 0; j--)
            {
                int top = (int)stack.Peek();
                if(arr[j] < top)
                {
                    stack.Pop();
                    arr[j] = 0;
                }
            }
            int total = 0;
            for(int k = 0; k < n; k++)
            {
                total += arr[k];
            }
            Console.WriteLine("{0}", total);
        }
    }
}