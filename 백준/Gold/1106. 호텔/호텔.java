// 누적해서 해결하려다 블로그를 통해 C+100 참고

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int C, N;
    static int[][] arr;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        C = Integer.parseInt(token.nextToken());
        N = Integer.parseInt(token.nextToken());
        arr = new int[N][2];

        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            arr[i][0] = Integer.parseInt(token.nextToken());
            arr[i][1] = Integer.parseInt(token.nextToken());
        }

        dp = new int[C+101];
        Arrays.fill(dp, Integer.MAX_VALUE/2);
        dp[0] = 0;

        for (int i = 0; i < N; i++) {
            int cost = arr[i][0];
            int people = arr[i][1];

            for (int j = people; j < dp.length; j++) {
                dp[j] = Math.min(dp[j], dp[j-people]+cost);
            }
        }

        int res = Integer.MAX_VALUE;
        for (int i = C; i < dp.length; i++) {
            res = Math.min(res, dp[i]);
        }

        System.out.println(res);
    }
}