import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int from = Integer.parseInt(token.nextToken());
        int to = Integer.parseInt(token.nextToken());
        token = new StringTokenizer(input.readLine());
        int X = Integer.parseInt(token.nextToken());
        int diff = Integer.parseInt(token.nextToken());
        int cnt = 0;
        for (int i = from; i <= to; i++) {
            if (Math.abs(i - X) <= diff) cnt++;
        }
        if (cnt == 0) System.out.println("IMPOSSIBLE");
        else System.out.println(cnt);
    }
}