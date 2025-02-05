import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int[] arr;
    static int[][][] dp;
    public static void main(String[] args) throws IOException {
        StringTokenizer token = new StringTokenizer(input.readLine());
        int size = token.countTokens();
        arr = new int[size-1];
        for (int i = 0; i < size-1; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }

        dp = new int[5][5][arr.length+1];
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < arr.length+1; k++) {
                    dp[i][j][k] = -1;
                }
            }
        }

        System.out.println(dance(0,0,0));
    }

    static int dance(int left, int right, int cnt) {
        if (cnt == arr.length) return 0;
        if (dp[left][right][cnt] != -1) return dp[left][right][cnt];
        dp[left][right][cnt] = Math.min(dance(arr[cnt],right,cnt+1) + power(left,arr[cnt]), dance(left,arr[cnt],cnt+1) + power(right,arr[cnt]));
        return dp[left][right][cnt];
    }

    static int power(int before, int after) {
        int diff = Math.abs(before - after);
        if (diff == 0) return 1;
        else if (before == 0) return 2;
        else if (diff == 1 || diff == 3) return 3;
        else return 4;

    }
}