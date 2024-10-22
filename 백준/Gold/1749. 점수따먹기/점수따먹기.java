import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static int[][] arr, dp;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        arr = new int[N+1][M+1];
        dp = new int[N+1][M+1];
        for (int i = 1; i <= N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 1; j <= M; j++) {
                arr[i][j] = Integer.parseInt(token.nextToken());
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j];
            }
        }

        int res = Integer.MIN_VALUE;
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                for (int k = 1; k <= i; k++) {
                    for (int l = 1; l <= j; l++) {
                        res = Math.max(res, dp[i][j] - dp[k-1][j] - dp[i][l-1] + dp[k-1][l-1]);
                    }
                }
            }
        }
        System.out.println(res);
    }
}