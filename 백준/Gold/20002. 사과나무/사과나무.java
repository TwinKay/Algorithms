import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N;
    static int[][] arr,sumArr;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(token.nextToken());
            }
        }
        sumArr = new int[N+1][N+1];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                sumArr[i][j] = sumArr[i-1][j] + sumArr[i][j-1] - sumArr[i-1][j-1] + arr[i-1][j-1];
            }
        }

        int res = Integer.MIN_VALUE;
        for(int s = 1; s <= N; s++){
            for(int r = 1; r <= N - s + 1; r++){
                for(int c = 1; c <= N - s + 1; c++){
                    int r2 = r+s-1;
                    int c2 = c+s-1;

                    int subSum = sumArr[r2][c2]
                            - sumArr[r-1][c2]
                            - sumArr[r2][c-1]
                            + sumArr[r-1][c-1];
                    res = Math.max(res, subSum);
                }
            }
        }
        System.out.println(res);
    }
}