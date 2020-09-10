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

    // Complete the funnyString function below.
    static string funnyString(string s) {
        var copy = String.Join("", s.Reverse());
        for(var i = 0; i < s.Length - 1; i++) {
            var diff1 = Math.Abs((int)s[i] - (int)s[i+1]);
            var diff2 = Math.Abs((int)copy[i] - (int)copy[i+1]);
            if(diff1 != diff2) return "Not Funny";
        }
        return "Funny";
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int q = Convert.ToInt32(Console.ReadLine());

        for (int qItr = 0; qItr < q; qItr++) {
            string s = Console.ReadLine();

            string result = funnyString(s);

            textWriter.WriteLine(result);
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
