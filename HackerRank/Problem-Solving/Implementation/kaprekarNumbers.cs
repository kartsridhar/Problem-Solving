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

    // Complete the kaprekarNumbers function below.
    static void kaprekarNumbers(long p, long q) {
        var result = new List<long>();
        for(long i = p; i <= q; i++) {
            int d = i.ToString().Length;
            var square = (i*i).ToString().ToList();
            long left = 0;
            long right = long.Parse(String.Join("", square));
            int diff = square.Count - d;
            if (diff != 0) {
                left = long.Parse(String.Join("", square.Take(diff)));
                right = long.Parse(String.Join("", square.Skip(diff)));
            }
            if (left + right == i)
                result.Add(i);
        }
        if (result.Count != 0)
            Console.WriteLine(String.Join(" ", result));
        else
            Console.WriteLine("INVALID RANGE");
    }

    static void Main(string[] args) {
        long p = long.Parse(Console.ReadLine());

        long q = long.Parse(Console.ReadLine());

        kaprekarNumbers(p, q);
    }
}
