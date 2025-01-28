import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static String S,Target;

    public static void main(String[] args) throws IOException {
        S = input.readLine();
        Target = input.readLine();
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < S.length(); i++) {
            stack.push(S.charAt(i));

            if (stack.size() >= Target.length()) {
                boolean flag = true;
                for (int j = 0; j < Target.length(); j++) {
                    if (Target.charAt(j) != stack.get(stack.size()-Target.length()+j)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    for (int j = 0; j < Target.length(); j++) {
                        stack.pop();
                    }
                }
            }
        }
        for (char c : stack) {
            sb.append(c);
        }
        if (sb.length()==0){
            sb.append("FRULA");
        }
        System.out.println(sb);
    }
}