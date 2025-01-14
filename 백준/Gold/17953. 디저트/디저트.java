import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,M;
    static int[][] arr, dp;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        arr = new int[M][N];
        dp = new int[M][N];

        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(token.nextToken());
            }
        }
        for (int i = 0; i < M; i++) {
            dp[i][0] = arr[i][0];
        }
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int k = 0; k < M; k++) {
                    if (k==j){
                        dp[j][i] = Math.max(dp[j][i], dp[k][i-1]+arr[j][i]/2);
                    }else{
                        dp[j][i] = Math.max(dp[j][i], dp[k][i-1]+arr[j][i]);
                    }
                }
            }
        }
        int res = Integer.MIN_VALUE;
        for (int i = 0; i < M; i++) {
            res = Math.max(res, dp[i][N-1]);
        }
        System.out.println(res);
    }
}