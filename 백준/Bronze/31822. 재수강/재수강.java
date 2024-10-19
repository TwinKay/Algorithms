import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N,cnt;

    public static void main(String[] args) throws IOException {
        String s = input.readLine();
        s = s.substring(0,5);
        N = Integer.parseInt(input.readLine());
        cnt = 0;
        for (int i = 0; i < N; i++) {
            String cand = input.readLine();
            cand = cand.substring(0,5);
            if (s.equals(cand)) {
                cnt ++;
            }
        }
        System.out.println(cnt);
    }
}