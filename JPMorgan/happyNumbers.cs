public class Solution {
    public int Compute(string number) {
        int sum = 0;
        foreach(var d in number) {
            int digit = int.Parse(d.ToString());
            sum += (digit * digit);
        }
        return sum;
    }
    
    public bool IsHappy(int n) {
        HashSet<int> seenNumbers = new HashSet<int>();
        while(true) {
            if(!seenNumbers.Contains(n)) {
                if(n == 1)
                    return true;
                else {
                    seenNumbers.Add(n);
                    n = Compute(n.ToString());
                }
            }
            else
                return false;
        }
    }
}