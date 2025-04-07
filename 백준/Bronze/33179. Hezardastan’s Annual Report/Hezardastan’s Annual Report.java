import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());
        token = new StringTokenizer(input.readLine());
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int a = Integer.parseInt(token.nextToken());
            cnt+=a/2;
            if (a%2==1) cnt++;
        }
        System.out.println(cnt);
    }
}
