import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());
        char[] chars = new char[n];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < n; i++) {
            chars[i] = token.nextToken().charAt(0);
        }
        char c = input.readLine().charAt(0);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (chars[i] == c) cnt++;
        }
        System.out.println(cnt);
    }
}


