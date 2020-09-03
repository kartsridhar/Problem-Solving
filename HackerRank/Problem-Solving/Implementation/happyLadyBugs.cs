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
    // Complete the happyLadybugs function below.
    static string happyLadybugs(string b) {
        // 1. If count of any colour is not > 1 and it has at least 1 underscore, return false
        var uniqueColours = new HashSet<char>(b.ToList());
        foreach(var i in uniqueColours) {
            if(b.Count(j => j == i) == 1 && i != '_')
                return "NO";
        }

        // 2. If there is no underscore in the string then check if it is happy. if it is not, return false
        if(!b.Contains('_')) {
            for(var i = 1; i < b.Length - 1; i++) {
                if(b[i] != b[i-1] && b[i] != b[i+1])
                    return "NO";
            }
        }
        return "YES";
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int g = Convert.ToInt32(Console.ReadLine());

        for (int gItr = 0; gItr < g; gItr++) {
            int n = Convert.ToInt32(Console.ReadLine());

            string b = Console.ReadLine();

            string result = happyLadybugs(b);

            textWriter.WriteLine(result);
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
