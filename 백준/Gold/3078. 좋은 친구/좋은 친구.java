import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,K;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            arr[i] = s.length();
        }
        long cnt = 0;
        int[] lens = new int[21];
        for (int i = 0; i < N; i++) {
            cnt += lens[arr[i]];
            lens[arr[i]]++;
            if (i-K >= 0) {
                lens[arr[i-K]]--;
            }
        }
        System.out.println(cnt);
    }
}