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



class Result
{

    /*
     * Complete the 'firstOccurrence' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. STRING s
     *  2. STRING x
     */

    public static int firstOccurrence(string s, string x)
    {
        string pattern = "";
        foreach(var i in x) 
        {
            if(i == '*') pattern += '.';
            else pattern += i;
        }
        Console.WriteLine(pattern);
        var match = Regex.Match(s, pattern);
        if(match.Success) return match.Index;
        else return -1;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        string x = Console.ReadLine();

        int result = Result.firstOccurrence(s, x);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
