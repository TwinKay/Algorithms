import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int N;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        token = new StringTokenizer(input.readLine());
        int cnt = 0;
        for (int i = 0; i < 5; i++) {
            int a = Integer.parseInt(token.nextToken());
            if (N==a) cnt++;

        }
        System.out.println(cnt);


    }
}