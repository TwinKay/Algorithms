import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;


    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(token.nextToken());
        int m = Integer.parseInt(token.nextToken());
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            char[] chars = input.readLine().toCharArray();
            for (char c : chars) {
                if (c=='+') {
                    cnt++;
                    break;
                }
            }
        }
        System.out.println(cnt);
    }
}


