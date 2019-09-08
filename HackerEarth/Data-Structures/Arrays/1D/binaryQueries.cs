/*
// Sample code to perform I/O:

name = Console.ReadLine();                  // Reading input from STDIN
Console.WriteLine("Hi, {0}.", name);        // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
using System;

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
            string[] nq = Console.ReadLine().Split();
            string[] q = new string[Convert.ToInt32(nq[1])];
            string[] n = Console.ReadLine().Split();

            for(int i = 0; i < q.Length; i++)
            {
                string[] query = Console.ReadLine().Split();
                int command = Convert.ToInt32(query[0]);

                if(command == 1)
                {
                    int x = Convert.ToInt32(query[1]) - 1;
                    n[x] = (n[x] == "1") ? "0" : "1";
                }
                else
                {
                    int least = Convert.ToInt32(query[2])-1;
                    int bit = Convert.ToInt32(n[least]);
                    Console.WriteLine((bit == 0) ? "EVEN" : "ODD");
                }
            }
        }
    }
}
