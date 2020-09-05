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

    // Complete the countLuck function below.
    static bool checkRange(List<List<char>> grid, int x, int y) {
        return (x >= 0 && x < grid.Count && y >= 0 && y < grid[0].Count);
    }

    static Tuple<bool, List<int>, List<List<bool>>> makeMove(List<List<bool>> visited, List<List<char>> grid, List<int> goal, List<int> current) {
        var next = new List<int>();
        var x = current[0];
        var y = current[1];
        var possible = new List<List<int>>();

        // LEFT
        if(checkRange(grid, x-1, y)) {
            if((grid[x-1][y] == '.' || grid[x-1][y] == '*') && !visited[x-1][y]) { 
                possible.Add(new List<int> {x-1, y}); 
                visited[x-1][y] = true;
            }
        }
        
        // RIGHT
        if(checkRange(grid, x+1, y)) { 
            if((grid[x+1][y] == '.' || grid[x+1][y] == '*') && !visited[x+1][y]) {
                possible.Add(new List<int> {x+1, y});
                visited[x+1][y] = true;
            }
        }

        // UP
        if(checkRange(grid, x, y-1)) {
            if((grid[x][y-1] == '.' || grid[x][y-1] == '*') && !visited[x][y-1]) {
                possible.Add(new List<int> {x, y-1});
                visited[x][y-1] = true;
            }
        }

        // DOWN
        if(checkRange(grid, x, y+1)) {
            if((grid[x][y+1] == '.' || grid[x][y+1] == '*') && !visited[x][y+1]) {
                possible.Add(new List<int> {x, y+1});
                visited[x][y+1] = true;
            }
        }
        
        if(possible.Count > 1) {
            var min = 99999;
            foreach(var i in possible) {
                var manhattan = Math.Abs(goal[0] - i[0]) + Math.Abs(goal[1] - i[1]);
                if(manhattan < min) {
                    next = i;
                    min = manhattan;
                }
            }
            return Tuple.Create(true, next, visited);
        }
        else if(possible.Count == 1) {
            next = possible[0];
            return Tuple.Create(false, next, visited);
        }
        else {
            next = new List<int>{-1, -1};
            return Tuple.Create(false, next, visited);
        }
    }

    static string countLuck(string[] matrix, int k) {
        var grid = new List<List<char>>();
        var start = new List<int>();
        var goal = new List<int>();

        var visited = new List<List<bool>>();
        var foundStart = false;
        var foundGoal = false;

        for(var i = 0; i < matrix.Length; i++) {
            var row = matrix[i].ToList();
            grid.Add(row);
            visited.Add(Enumerable.Repeat(false, row.Count).ToList());
            if(!foundGoal && row.Contains('*')) {
                goal.Add(i);
                goal.Add(row.IndexOf('*'));
                foundGoal = true;
            }
            if(!foundStart && row.Contains('M')) {
                start.Add(i);
                start.Add(row.IndexOf('M'));
                visited[start[0]][start[1]] = true;
                foundStart = true;
            }
        }

        var current = start;
        var count = 0;
        while(!current.SequenceEqual(goal)) {
            var nextBest = makeMove(visited, grid, goal, current);
            var wave = nextBest.Item1;
            if(wave) {
                count += 1;
            }
            if(!nextBest.Item2.SequenceEqual(new List<int> {-1, -1})) {
                current = nextBest.Item2;
            }   
            visited = nextBest.Item3;
        }

        if(count == k) return "Impressed";
        else return "Oops!";
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int t = Convert.ToInt32(Console.ReadLine());

        for (int tItr = 0; tItr < t; tItr++) {
            string[] nm = Console.ReadLine().Split(' ');

            int n = Convert.ToInt32(nm[0]);

            int m = Convert.ToInt32(nm[1]);

            string[] matrix = new string [n];

            for (int i = 0; i < n; i++) {
                string matrixItem = Console.ReadLine();
                matrix[i] = matrixItem;
            }

            int k = Convert.ToInt32(Console.ReadLine());

            string result = countLuck(matrix, k);

            textWriter.WriteLine(result);
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
