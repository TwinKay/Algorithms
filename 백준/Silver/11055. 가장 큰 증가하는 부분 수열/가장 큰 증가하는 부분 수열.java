import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N, res;
    static int[] arr, dp;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        token = new StringTokenizer(input.readLine());
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        dp = new int[N];
        dp[0] = arr[0];
        res = arr[0];
        for (int i = 1; i < N; i++) {
            dp[i] = arr[i];
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], dp[j]+arr[i]);
                }
            }
            res = Math.max(res, dp[i]);
        }
        System.out.println(res);
    }
}