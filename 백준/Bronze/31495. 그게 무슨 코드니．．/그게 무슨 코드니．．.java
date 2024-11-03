import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static char[] chars;

    public static void main(String[] args) throws IOException {
        chars = input.readLine().toCharArray();
        if (chars.length <= 2) {
            sb.append("CE");
        } else {
            if (chars[0] == '"' && chars[chars.length - 1] == '"') {
                for (int i = 1; i < chars.length - 1; i++) {
                    sb.append(chars[i]);
                }
                if (sb.length() == 0) {
                    sb.append("CE");
                }
            } else {
                sb.append("CE");
            }
        }
        System.out.println(sb);
    }
}