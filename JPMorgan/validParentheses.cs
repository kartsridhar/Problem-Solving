public class Solution {
    public bool IsValid(string s) {
        var dict = new Dictionary<char, char>();
        dict.Add('(', ')');
        dict.Add('{', '}');
        dict.Add('[', ']');
        
        var stack = new Stack<char>();
        for(int i = 0; i < s.Length; i++) {
            if(dict.ContainsKey(s[i]))
                stack.Push(dict[s[i]]);
            else {
                if(stack.Count != 0 && stack.Peek() == s[i])
                    stack.Pop();
                else
                    return false;
            }
        }
        return (stack.Count == 0) ? true : false;
    }
}