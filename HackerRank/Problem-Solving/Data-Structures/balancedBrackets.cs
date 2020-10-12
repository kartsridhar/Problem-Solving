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

    // Complete the isBalanced function below.
    static string isBalanced(string s) {
        var dict = new Dictionary<char, char>();
        dict.Add('(', ')');
        dict.Add('{', '}');
        dict.Add('[', ']');

        var stack = new Stack<char>();
        if(!dict.ContainsKey(s[0]) || !dict.ContainsValue(s[s.Length - 1])) return "NO";

        for(var i = 0; i < s.Length; i++) {
            if(dict.ContainsKey(s[i])) stack.Push(dict[s[i]]);
            else {
                if(stack.Count != 0 && stack.Peek() == s[i]) stack.Pop();
                else return "NO";
            }
        }
        return (stack.Count == 0) ? "YES" : "NO";
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int t = Convert.ToInt32(Console.ReadLine());

        for (int tItr = 0; tItr < t; tItr++) {
            string s = Console.ReadLine();

            string result = isBalanced(s);

            textWriter.WriteLine(result);
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
