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

public class Point {
    public int X;
    public int Y;

    public Point(int xVal, int yVal) {
        this.X = xVal;
        this.Y = yVal;
    }

    public override string ToString() {
        return $"({this.X}, {this.Y})";
    }
}

class Solution {

    static List<List<int>> maze;
    static List<List<bool>> visited;
    static Queue<Point> moves = new Queue<Point>();

    static void makeMove(Point point) {
        int val = maze[point.X][point.Y];

        // RIGHT
        for(var i = point.X; (i < maze.Count && maze[i][point.Y] != -1); i++) {
            maze[i][point.Y] = Math.Max(val + 1, maze[i][point.Y]);
            moves.Enqueue(new Point(i, point.Y));
        }

        // LEFT
        for(var i = point.X; (i >= 0 && maze[i][point.Y] != -1); i--) {
            maze[i][point.Y] = Math.Max(val + 1, maze[i][point.Y]);
            moves.Enqueue(new Point(i, point.Y));
        }

        // DOWN
        for(var j = point.Y; (j < maze.Count && maze[point.X][j] != -1); j++) {
            maze[point.X][j] = Math.Max(val + 1, maze[point.X][j]);
            moves.Enqueue(new Point(point.X, j));
        }

        // UP
        for(var j = point.Y; (j >= 0 && maze[point.X][j] != -1); j--) {
            maze[point.X][j] = Math.Max(val + 1, maze[point.X][j]);
            moves.Enqueue(new Point(point.X, j));
        }
    }   

    // Complete the minimumMoves function below.
    static int minimumMoves(string[] grid, int startX, int startY, int goalX, int goalY) {
        // Init maze and visited
        for(var i = 0; i < grid.Length; i++) {
            for(var j = 0; j < grid.Length; j++) {
                if(grid[i][j] == '.') maze[i][j] = 100;
                else maze[i][j] = -1;
            }
        }
        visited = Enumerable.Repeat(Enumerable.Repeat(false, grid.Length).ToList(), grid.Length).ToList();

        Point current = new Point(startX, startY);
        moves.Enqueue(current);
        maze[current.X][current.Y] = 0;
        
        while(moves.Count != 0) {
            current = moves.Dequeue();
            if(!visited[current.X][current.Y]) {
                visited[current.X][current.Y] = true;
                makeMove(current);
            }
        }
        return maze[goalX][goalY];
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        string[] grid = new string [n];

        for (int i = 0; i < n; i++) {
            string gridItem = Console.ReadLine();
            grid[i] = gridItem;
        }

        string[] startXStartY = Console.ReadLine().Split(' ');

        int startX = Convert.ToInt32(startXStartY[0]);

        int startY = Convert.ToInt32(startXStartY[1]);

        int goalX = Convert.ToInt32(startXStartY[2]);

        int goalY = Convert.ToInt32(startXStartY[3]);

        int result = minimumMoves(grid, startX, startY, goalX, goalY);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
