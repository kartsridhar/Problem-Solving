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

class Solution {

    // Complete the maxSubarray function below.
    static int maxSubsequence(int[] arr) {
        var sorted = arr.ToList().OrderBy(i => i).ToList();
        if(sorted[arr.Length - 1] <= 0) return sorted[arr.Length - 1];
        else return (from i in sorted where i > 0 select i).ToList().Sum();
    }

    static int[] maxSubarray(int[] arr) {
        var maxSubsequenceSum = maxSubsequence(arr);
        var maxSubarraySum = -99999;

        var maxEnding = 0;

        foreach(var i in arr) {
            maxEnding = Math.Max(i, maxEnding + i);
            maxSubarraySum = Math.Max(maxSubarraySum, maxEnding);
        }
        return new List<int> {maxSubarraySum, maxSubsequenceSum}.ToArray();
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int t = Convert.ToInt32(Console.ReadLine());

        for (int tItr = 0; tItr < t; tItr++) {
            int n = Convert.ToInt32(Console.ReadLine());

            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp))
            ;
            int[] result = maxSubarray(arr);

            textWriter.WriteLine(string.Join(" ", result));
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
