import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int T;
    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t = 0; t < T; t++) {
            token = new StringTokenizer(input.readLine());
            int start = Integer.parseInt(token.nextToken());
            int second = Integer.parseInt(token.nextToken());
            int res = start-second/7+second/4;
            sb.append(res).append("\n");
        }
        System.out.println(sb);
    }
}