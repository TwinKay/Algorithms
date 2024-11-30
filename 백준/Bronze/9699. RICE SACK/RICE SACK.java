import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        for (int i=1; i<=N; i++) {
            token = new StringTokenizer(input.readLine());
            int max = Integer.MIN_VALUE;
            for (int j=0; j<5; j++) {
                int s = Integer.parseInt(token.nextToken());
                max = Math.max(max, s);
            }
            sb.append("Case #" + i + ": " + max + "\n");
        }
        System.out.println(sb);
    }
}