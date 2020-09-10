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

    // Complete the separateNumbers function below.
    static void separateNumbers(string s) {
        var possible = false;
        var bestStart = "";
        var i = 1; 
        var count = 0;
        while(count < (s.Length / 2) && !possible) {
            var start = long.Parse(String.Join("", s.ToList().Take(i)));
            var sequence = "";
            while(sequence.Length < s.Length) {
                sequence += start.ToString();
                start += 1;
            }
            if(string.Equals(sequence, s)) {
                bestStart = String.Join("", s.ToList().Take(i));
                possible = true;
            }
            else {
                i += 1;
                count += 1;
            }
        }
        var result = possible ? ("YES " + bestStart) : "NO";
        Console.WriteLine(result);
    }   

    static void Main(string[] args) {
        int q = Convert.ToInt32(Console.ReadLine());

        for (int qItr = 0; qItr < q; qItr++) {
            string s = Console.ReadLine();

            separateNumbers(s);
        }
    }
}
