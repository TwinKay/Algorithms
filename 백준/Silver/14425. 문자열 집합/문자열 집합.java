import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,M;
    static List<String> strs;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        strs = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            strs.add(input.readLine());
        }
        int cnt = 0;
        for (int i = 0; i < M; i++) {
            String str = input.readLine();
            for (String s : strs) {
                if (s.equals(str)) {
                    cnt++;
                    break;
                }
            }
        }
        System.out.println(cnt);
    }
}