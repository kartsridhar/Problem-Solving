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

    // Complete the caesarCipher function below.
    static string caesarCipher(string s, int k) {
        var alphabet = "abcdefghijklmnopqrstuvwxyz".ToList();
        var key = (alphabet.Skip(k % 26)).Concat(alphabet.Take(k % 26)).ToList();
        var encrypted = "";
        for(var i = 0; i < s.Length; i++) {
            if(alphabet.Contains(Char.ToLower(s[i]))) {
                if(Char.IsUpper(s[i])) {
                    encrypted += Char.ToUpper(key[alphabet.IndexOf(Char.ToLower(s[i]))]);
                }
                else {
                    encrypted += key[alphabet.IndexOf(s[i])];
                }
            }
            else {
                encrypted += s[i];
            }
        }   
        return encrypted;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        string s = Console.ReadLine();

        int k = Convert.ToInt32(Console.ReadLine());

        string result = caesarCipher(s, k);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
