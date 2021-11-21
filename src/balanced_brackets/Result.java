package balanced_brackets;

import java.util.Stack;

class Result {

    /*
     * Complete the 'isBalanced' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     * 
     * https://www.hackerrank.com/challenges/balanced-brackets/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues
     */

    public static String isBalanced(String s) {
        // Write your code here

        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c=='(' || c=='[' || c=='{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return "NO";
                char firstChar = stack.peek();
                if(
                    firstChar == '(' && c == ')'
                    || firstChar == '[' && c == ']'
                    || firstChar == '{' && c == '}'
                ) {
                    stack.pop();
                } else {
                    return "NO";
                }
            }
        }
        if (stack.isEmpty()) return "YES";
        return "NO";
    }

}
