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

    // Complete the icecreamParlor function below.
    static int[] icecreamParlor(int m, int[] arr) {
        var costs = arr.ToList();
        var result = Enumerable.Repeat(0, 2).ToList();
        for(var i = 0; i < costs.Count; i++) {
            var compliment = m - arr[i];
            if(costs.Contains(compliment)) {
                result[0] = i+1;
                var j = costs.IndexOf(compliment);
                if(j != i) {
                    result[1] = j+1;
                }
                else {
                    var j2 = costs.IndexOf(compliment, j+1);
                    if(j2 == -1) continue;
                    else result[1] = j2+1;
                }
                break;
            }
        }
        result.Sort();
        return result.ToArray();
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int t = Convert.ToInt32(Console.ReadLine());

        for (int tItr = 0; tItr < t; tItr++) {
            int m = Convert.ToInt32(Console.ReadLine());

            int n = Convert.ToInt32(Console.ReadLine());

            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp))
            ;
            int[] result = icecreamParlor(m, arr);

            textWriter.WriteLine(string.Join(" ", result));
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
