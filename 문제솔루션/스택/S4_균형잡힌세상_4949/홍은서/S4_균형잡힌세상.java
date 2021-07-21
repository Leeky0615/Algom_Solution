package 스택.S4_균형잡힌세상_4949.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;


public class S4_균형잡힌세상 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        while (true){
            String s= br.readLine();
            if(s.equals(".")){
                return;
            }
            System.out.println(check(s));

        }
    }

    private static String check(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '[' || c == '(') { // 여는 괄호는 일단 집어넣음
                stack.push(c);
            }
            else if (c == ']') {
                if(stack.empty() || stack.peek() != '['){
                    return "no";
                }else{
                    stack.pop();
                }
            }
            else if(c == ')'){
                if(stack.empty() || stack.peek() != '('){
                    return "no";
                }else{
                    stack.pop();
                }
            }
        }
        if(stack.isEmpty()){
            return "yes";
        }else{
            return "no";
        }
    }
}
