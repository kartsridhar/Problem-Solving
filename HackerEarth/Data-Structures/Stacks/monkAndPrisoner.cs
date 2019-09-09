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
            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            List<int> x = new List<int>();
            List<int> y = new List<int>();
            for (int i=0; i<n; i++)
            {
                int xtemp = -1;
                for (int j=0; j<i; j++)
                {
                    if (arr[j] > arr[i])
                        xtemp = j + 1;
                }
                x.Add(xtemp);
                int ytemp = -1;
                for (int k=i; k<n; k++)
                {
                    if (arr[k] > arr[i])
                    {
                        ytemp = k + 1;
                        break;
                    }                      
                }
                y.Add(ytemp);
            }
            var output = x.Zip(y, (a, b) => a + b).ToList();
            Console.WriteLine(String.Join(" ", output));
        }
    }
}