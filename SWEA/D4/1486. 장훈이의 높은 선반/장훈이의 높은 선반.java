import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
 
public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static int[] arr;
    static int b;
    static int min;
 
    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            token = new StringTokenizer(input.readLine());
            int n = Integer.parseInt(token.nextToken());
            b = Integer.parseInt(token.nextToken());
            arr = new int[n];
            token = new StringTokenizer(input.readLine());
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(token.nextToken());
            }
            min = Integer.MAX_VALUE;
 
            subset(0,n,new boolean[n]);
            sb.append("#").append(t).append(" ").append(min-b).append("\n");
        }
        System.out.println(sb);
    }
    public static void subset(int cnt, int r, boolean[] isSelected) {
        if (cnt == r) {
            int res = 0;
            for (int i=0; i<r; i++) {
                if (isSelected[i]) {
                    res += arr[i];
                } else {
                }
            }
 
            if (res>=b){
                min = Math.min(res, min);
            }
            return;
        }
        isSelected[cnt] = true;
        subset(cnt+1, r, isSelected);
        isSelected[cnt] = false;
        subset(cnt+1, r, isSelected);
    }
}