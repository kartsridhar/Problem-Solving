using System;
using System.Collections;
using System.Collections.Generic;
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
            string[] stuff = Console.ReadLine().Split(' ');
            int n = Convert.ToInt32(stuff[0]);
            int k = Convert.ToInt32(stuff[1]);
            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            Array.Reverse(arr);
            Stack stack = new Stack();
            for(int i=0; i<n; i++)
            {
                stack.Push(arr[i]);
            }
            List<int> popped = new List<int>();
            for (int j=0; j<k; j++)
            {
                int top = (int)stack.Peek();
                int max = popped.Max();
                if(max > top)
                {   
                    stack.Push(max);
                    popped.Remove(max);
                }
                else
                {
                    stack.Pop();
                    popped.Add(top);
                }
            }
            if (stack.Count == 0)
                Console.WriteLine("-1");
            else
                Console.WriteLine("{0}", (int)stack.Peek());
        }
    }
}