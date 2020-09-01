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

    // Complete the cavityMap function below.
    static string[] cavityMap(string[] grid) {
        var dim = grid.Length;
        var matrix = new List<List<int>>();
        for(var i = 0; i < dim; i++) {
            var nums = grid[i].ToList().Select(c => int.Parse(c.ToString())).ToList();
            matrix.Add(nums);
        }
        
        var result = new List<string>();
        for(var i = 0; i < dim; i++) {
            var str = "";
            for(var j = 0; j < dim; j++) {
                if(i >= 1 && i < dim - 1 && j >= 1 && j < dim - 1) {
                    if(matrix[i][j] > matrix[i-1][j] && matrix[i][j] > matrix[i][j+1]
                    && matrix[i][j] > matrix[i+1][j] && matrix[i][j] > matrix[i][j-1])
                        str += "X";
                    else
                        str += matrix[i][j].ToString();
                }
                else
                    str += matrix[i][j].ToString();
            }
            result.Add(str);
        }
        return result.ToArray();
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        string[] grid = new string [n];

        for (int i = 0; i < n; i++) {
            string gridItem = Console.ReadLine();
            grid[i] = gridItem;
        }

        string[] result = cavityMap(grid);

        textWriter.WriteLine(string.Join("\n", result));

        textWriter.Flush();
        textWriter.Close();
    }
}
