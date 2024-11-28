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
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            double a = Double.parseDouble(token.nextToken());
            double b = Double.parseDouble(token.nextToken());
            double m = Math.abs(a-b);
            sb.append(String.format("%.1f", m)).append("\n");
        }
        System.out.println(sb);
    }
}