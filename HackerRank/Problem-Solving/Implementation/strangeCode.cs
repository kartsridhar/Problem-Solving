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

    // Complete the strangeCounter function below.
    static long strangeCounterNaive(long t) {
        long startTime = 3;
        long currentTime = startTime;
        for(long i = 1; i < t; i++) {
            if(currentTime == 1) {
                startTime *= 2;
                currentTime = startTime;
            }
            else
                currentTime -= 1;
        }
        return currentTime;
    }

    static long strangeCounter(long t) {
        var times = new Stack<long>();
        times.Push(1);
        while(times.Peek() <= t) {
            var next = 2 * times.Peek() + 2;
            times.Push(next);
        }
        return times.Peek() - t;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        long t = Convert.ToInt64(Console.ReadLine());

        long result = strangeCounter(t);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
