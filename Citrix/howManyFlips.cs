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
     * Complete the 'theFinalProblem' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING target as parameter.
     */

    public static int theFinalProblem(string target)
    {
        var length = target.Length;
        var count = 0;
        for(var i = 0; i < length; i++) 
        {
            var flipCheck = (count % 2) ^ int.Parse(target[i].ToString());
            count += flipCheck;
        }
        return count;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string target = Console.ReadLine();

        int result = Result.theFinalProblem(target);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
