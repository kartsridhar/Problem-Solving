/*
// Sample code to perform I/O:

name = Console.ReadLine();                  // Reading input from STDIN
Console.WriteLine("Hi, {0}.", name);        // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

INPUT
1
7
100 80 60 70 60 75 85

OUTPUT 
1 1 1 2 1 4 6
*/

// Write your code here
using System;
using System.Collections;
using System.Linq;
using System.Collections.Generic;

class Program {
    static void Main(string[] args) {
        Solution();
    }
    private static void Solution() {
        int t = Convert.ToInt32(Console.ReadLine());
        for(int i=0; i<t; i++) {
            int n = Convert.ToInt32(Console.ReadLine());
            int[] towers = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            int[] signal = new int[n];
            for(int j=0; j<n; j++) {
                signal[j] = 1;
            }
            for(int k=0; k<n; k++) {
                if(k==0){
                    signal[k] = 1; 
                }
                else {
                    for(int x=k-1; x>=0; x--) {
                        if(towers[k] >= towers[x]) {
                            signal[k] += 1;
                        }
                        else {
                            break;
                        }
                    }
                }
            }
            Console.WriteLine(String.Join(" ", signal.ToList()));
        }
    }
}