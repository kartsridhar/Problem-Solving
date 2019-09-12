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
            int[] vals = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int n = vals[0];
            int k = vals[1];
            int[] nums = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int s = 0;
            for (int i=0; i<k; i++)
            {
                s += nums[i];
            }
            int m = s; 
            for(int i=0; i<k-1; i++)
            {
                s += nums[n - 1 - i] - nums[k - 1 - i];
                if (s >= m)
                    m = s;
            }
            Console.WriteLine($"{m}");
        }
    }
}