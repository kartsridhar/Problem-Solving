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

    // Complete the gemstones function below.
    static int gemstones(string[] arr) {
        var result = new HashSet<char>(arr[0]);
        for(var i = 1; i < arr.Length; i++) {
            result.IntersectWith(new HashSet<char>(arr[i]));
        }
        return result.Count;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        string[] arr = new string [n];

        for (int i = 0; i < n; i++) {
            string arrItem = Console.ReadLine();
            arr[i] = arrItem;
        }

        int result = gemstones(arr);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
