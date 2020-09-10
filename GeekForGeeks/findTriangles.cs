using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution
{

    static int FindTriangles(int n, List<int> nums)
    {
        var count = 0;
        nums = nums.OrderByDescending(num => num).ToList();
        for(var i = 0; i < n - 1; i++)
        {
            var start = i + 1;
            var end = n - 1;
            while(start < end)
            {
                if(nums[start] + nums[end] > nums[i])
                {
                    count += (end - start);
                    start += 1;
                }
                else
                {
                    end -= 1;
                }
            }

        }
        return count;
    }

    static void Main(string[] args)
    {
        int t = int.Parse(Console.ReadLine());
        for(int i = 0; i < t; i++)
        {
            int n = int.Parse(Console.ReadLine());
            List<int> nums = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse).ToList();
            int result = FindTriangles(n, nums);
            Console.WriteLine(result);
        }
    }
}
