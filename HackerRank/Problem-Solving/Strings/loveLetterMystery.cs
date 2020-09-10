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

    // Complete the theLoveLetterMystery function below.
    static int theLoveLetterMystery(string s) {
        string first = "", second = "";
        if(s.Length % 2 == 0) {
            first = s.Substring(0, s.Length/2);
            second = String.Join("", s.Substring(s.Length/2).Reverse());
        }
        else {
            first = s.Substring(0, s.Length/2);
            second = String.Join("", s.Substring(s.Length/2 + 1).Reverse());
        }
        var count = 0;
        for(var i = 0; i < first.Length; i++) {
            count += Math.Abs(first[i] - second[i]);
        }
        return count;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int q = Convert.ToInt32(Console.ReadLine());

        for (int qItr = 0; qItr < q; qItr++) {
            string s = Console.ReadLine();

            int result = theLoveLetterMystery(s);

            textWriter.WriteLine(result);
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
