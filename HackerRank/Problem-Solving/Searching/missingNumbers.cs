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

    // Complete the missingNumbers function below.
    static List<int> missingNumbers(int[] arr, int[] brr) {
        var adict = new Dictionary<int, int>();
        for(var i = 0; i < arr.Length; i++) {
            if(!adict.ContainsKey(arr[i])) {
                adict.Add(arr[i], 1);
            }
            else {
                adict[arr[i]] += 1;
            }
        }

        var bdict = new Dictionary<int, int>();
        for(var i = 0; i < brr.Length; i++) {
            if(!bdict.ContainsKey(brr[i])) {
                bdict.Add(brr[i], 1);
            }
            else {
                bdict[brr[i]] += 1;
            }
        }

        var result = new List<int>();
        foreach(var i in bdict.Keys) {
            if(!adict.ContainsKey(i) || adict[i] != bdict[i])
                result.Add(i);
        }
        result.Sort();
        return result;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp))
        ;
        int m = Convert.ToInt32(Console.ReadLine());

        int[] brr = Array.ConvertAll(Console.ReadLine().Split(' '), brrTemp => Convert.ToInt32(brrTemp))
        ;
        List<int> result = missingNumbers(arr, brr);

        textWriter.WriteLine(String.Join(" ", result));

        textWriter.Flush();
        textWriter.Close();
    }
}
