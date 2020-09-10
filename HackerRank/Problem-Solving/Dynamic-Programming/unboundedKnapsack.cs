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

    private static List<List<int>> dp;

    // Complete the unboundedKnapsack function below.
    public static int unboundedKnapsack(int k, int[] arr, int length) {
        if(k == 0 || length == 0) 
            return 0;

        if(dp[length][k] != -1) 
            return dp[length][k]; 

        if(arr[length - 1] > k) 
            return unboundedKnapsack(k, arr, length - 1);
        
        dp[length][k] = Math.Max(arr[length - 1] + unboundedKnapsack(k - arr[length - 1], arr, length), unboundedKnapsack(k, arr, length - 1));

        return dp[length][k];

    }
    static int unboundedKnapsack(int k, int[] arr) {
        dp = Enumerable.Repeat((Enumerable.Repeat(-1, k+1).ToList()), arr.Length + 1).ToList();
        return unboundedKnapsack(k, arr, arr.Length);
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int t = Convert.ToInt32(Console.ReadLine());

        for(var i = 0; i < t; i++) {
            string[] nk = Console.ReadLine().Split(' ');
            
            int n = Convert.ToInt32(nk[0]);

            int k = Convert.ToInt32(nk[1]);

            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp))
            ;
            
            int result = unboundedKnapsack(k, arr);

            textWriter.WriteLine(result);
        }


        textWriter.Flush();
        textWriter.Close();
    }
}
