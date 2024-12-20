import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int T;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t = 0; t < T; t++) {
            token = new StringTokenizer(input.readLine());
            String s = token.nextToken();
            char[] chars = s.toCharArray();
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());

            for (int i = 0; i < chars.length; i++) {
                if (i<a || i>=b){
                    sb.append(chars[i]);
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}