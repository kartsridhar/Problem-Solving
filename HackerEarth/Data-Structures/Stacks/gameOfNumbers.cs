/*
// Sample code to perform I/O:

name = Console.ReadLine();                  // Reading input from STDIN
Console.WriteLine("Hi, {0}.", name);        // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
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
            int n = Convert.ToInt32(Console.ReadLine());
            List<int> nums = new List<int>();
            for(int i=0; i<n; i++)
            {
                nums.Add(Convert.ToInt32(Console.ReadLine()));
            }
            List<int> greater = new List<int>();
            for(int i=0; i<n; i++)
            {
                int temp = -1;
                for(int j=i; j<n; j++)
                {
                    if (nums[j] > nums[i])
                    {
                        temp = j;
                        break;
                    }
                }
                greater.Add(temp);
            }
            List<int> smaller = new List<int>();
            for(int i=0; i<n; i++)
            {
                int temp = -1;
                for(int j=greater[i]; j<n; j++)
                {
                    if (greater[i] == -1)
                        break;
                    else if (nums[j] < nums[greater[i]])
                    {
                        temp = nums[j];
                        break;
                    }
                }
                smaller.Add(temp);
            }
            Console.WriteLine(String.Join(" ", smaller.ToList()));
        }
    }
}