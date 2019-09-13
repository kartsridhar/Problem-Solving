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
            string s = Console.ReadLine().ToString();
            int n = s.Length;
            Stack stack = new Stack();
            for (int i = 0; i < n; i++)
            {
                if (stack.Count == 0)
                {
                    stack.Push(s[i]);
                }
                else
                {
                    if ((char)stack.Peek() == s[i])
                    {
                        stack.Pop();
                    }
                    else
                    {
                        stack.Push(s[i]);
                    }
                }
            }
            List<char> result = new List<char>();
            while (stack.Count != 0)
            {
                result.Add((char)stack.Pop());
            }
            result.Reverse();
            Console.WriteLine(String.Join("", result.ToList()));
        }
    }
}