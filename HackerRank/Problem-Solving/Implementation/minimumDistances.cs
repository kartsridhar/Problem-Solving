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

    // Complete the minimumDistances function below.
    static int minimumDistances(int[] a) {
        var duplicates = new HashSet<int>(a);

        foreach(var i in a) {
            if(duplicates.Contains(i)) 
                duplicates.Remove(i);
            else
                duplicates.Add(i);
        }

        if(duplicates.Count == 0) 
            return -1;

        int minDiff = 99999;
        foreach(var i in duplicates) {
            int diff = a.ToList().IndexOf(i);
            for(var j = diff+1; j < a.Length; j++) {
                if(a[j] == i && (Math.Abs(diff - j) < minDiff)) {
                    minDiff = Math.Abs(diff - j);
                    break;
                }
            }
        }
        return minDiff;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int[] a = Array.ConvertAll(Console.ReadLine().Split(' '), aTemp => Convert.ToInt32(aTemp))
        ;
        int result = minimumDistances(a);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
