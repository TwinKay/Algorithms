import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        String s = input.readLine();
        char[] chars = s.toCharArray();
        sb.append("h");
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == 'e') sb.append("ee");
        }
        sb.append("y");
        System.out.println(sb);
        
    }
}