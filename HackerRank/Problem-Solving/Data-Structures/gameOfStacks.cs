using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    /*
     * Complete the twoStacks function below.
     */
    static int twoStacks(int x, int[] a, int[] b) {
        /*
         * Write your code here.
         */
        var stackA = new Stack<int>(a.Reverse());
        var stackB = new Stack<int>(b.Reverse());
        var temp = new Stack<int>();
        var numA = 0;
        var numB = 0;
        var result = 0;
        var sum = 0;

        // First pick only from A
        while(stackA.Count > 0 && sum + stackA.Peek() <= x) {
            var top = stackA.Pop();
            sum += top;
            temp.Push(top);
            numA += 1;
        }
        result = Math.Max(result, numA + numB);

        // Adjust picks by comparing the tops of both
        while(temp.Count > 0 && stackB.Count > 0) {
            var top = stackB.Pop();
            sum += top;
            numB += 1;
            while(temp.Count > 0 && sum > x) {
                sum -= temp.Pop();
                numA -= 1;
            }
            result = Math.Max(result, numA + numB);
        }

        // Pick only from B to see if can still increase the number of turns
        while(stackB.Count > 0 && sum + stackB.Peek() <= x) {
            sum += stackB.Pop();
            numB += 1;
        } 
        result = Math.Max(result, numA + numB);

        return result;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int g = Convert.ToInt32(Console.ReadLine());

        for (int gItr = 0; gItr < g; gItr++) {
            string[] nmx = Console.ReadLine().Split(' ');

            int n = Convert.ToInt32(nmx[0]);

            int m = Convert.ToInt32(nmx[1]);

            int x = Convert.ToInt32(nmx[2]);

            int[] a = Array.ConvertAll(Console.ReadLine().Split(' '), aTemp => Convert.ToInt32(aTemp))
            ;

            int[] b = Array.ConvertAll(Console.ReadLine().Split(' '), bTemp => Convert.ToInt32(bTemp))
            ;
            int result = twoStacks(x, a, b);

            textWriter.WriteLine(result);
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
