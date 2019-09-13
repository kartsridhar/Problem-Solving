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
            int q = Convert.ToInt32(Console.ReadLine());
            List<KeyValuePair<int, int>> kv = new List<KeyValuePair<int, int>>();
            for(int i=0; i<q; i++)
            {
                string[] vals = Console.ReadLine().Split();
                if (vals[0] == "E")
                {
                    int x = Convert.ToInt32(vals[1]);
                    int y = Convert.ToInt32(vals[2]);
                    if (kv.Count() <= 1)
                    {
                        kv.Add(new KeyValuePair<int, int>(x, y));
                    }
                    else
                    {
                        int check = 1;
                        for(int j=kv.First().Key; j != kv.Last().Key; j++)
                        {
                            if (x == j)
                            {
                                check = 0;
                                kv.Insert(j, new KeyValuePair<int, int>(x, y));
                                break;
                            }
                        }
                        if (check == 1)
                            kv.Add(new KeyValuePair<int, int>(x, y));
                    }
                }
                else
                {
                    Console.WriteLine($"{kv.First().Key} {kv.First().Value}");
                    kv.RemoveAt(0);
                }
            }
        }
    }
}