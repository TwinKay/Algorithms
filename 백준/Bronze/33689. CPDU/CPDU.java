import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            String s = input.readLine();
            if (s.charAt(0)=='C') cnt++;
        }
        System.out.println(cnt);
    }
}
