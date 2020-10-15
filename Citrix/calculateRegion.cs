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



class Result
{

    /*
     * Complete the 'calculateTotalRegion' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts INTEGER_ARRAY heights as parameter.
     */

    public static long calculateTotalRegion(List<int> heights)
    {
        var n = heights.Count;
        var sum = 0;
        
        for(var i = 0; i < n; i++) 
        {
            /*
            1. find the largest left index (0 to i-1)
            2. find the smallest right index(i+1, n-1)
            3. if you find an element at l larger than the ith, break. Do the same with r.
            4. ensure l and r are >= 0 and <= n to keep in range
            5. sum += (r - l + 1)
            */
            var left = Math.Max(0, i - 1);
            var right = Math.Min(i + 1, n - 1);
            
            while(left >= 0) 
            {
                if(heights[left] > heights[i]) 
                {
                    left++;
                    break;
                }
                left--;
            }
            while(right < n)
            {
                if(heights[right] > heights[i])
                {
                    right--;
                    break;
                }
                right++;
            }
            
            // Ensure range
            left = (left < 0) ? left + 1 : left;
            right = (right >= n) ? right - 1 : right;
            
            // Update sum
            sum += (right - left + 1);
        }
        return sum;
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int heightsCount = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> heights = new List<int>();

        for (int i = 0; i < heightsCount; i++)
        {
            int heightsItem = Convert.ToInt32(Console.ReadLine().Trim());
            heights.Add(heightsItem);
        }

        long result = Result.calculateTotalRegion(heights);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
