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

    // Complete the checkMagazine function below.
    static void checkMagazine(string[] magazine, string[] note) {
        var mag = magazine.ToList().OrderBy(k => k).ToList();
        var not = note.ToList().OrderBy(k => k).ToList();
        var i = 0; 
        var j = 0;
        var matchCount = 0;
        while(i < note.Length && j < magazine.Length) {
            if(not[i] == mag[j]) {
                matchCount += 1;
                i += 1;
            }
            j += 1;
        }
        var result = (matchCount == note.Length) ? "Yes" : "No";
        Console.WriteLine(result);
    }

    static void Main(string[] args) {
        string[] mn = Console.ReadLine().Split(' ');

        int m = Convert.ToInt32(mn[0]);

        int n = Convert.ToInt32(mn[1]);

        string[] magazine = Console.ReadLine().Split(' ');

        string[] note = Console.ReadLine().Split(' ');

        checkMagazine(magazine, note);
    }
}
