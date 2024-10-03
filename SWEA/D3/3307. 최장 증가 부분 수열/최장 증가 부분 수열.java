import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();
    static int N;
    static int[] arr;
    static List<Integer> lst;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            N = Integer.parseInt(input.readLine());
            arr = new int[N];
            token = new StringTokenizer(input.readLine());
            for (int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(token.nextToken());
            }
            lst = new ArrayList<>();
            lst.add(arr[0]);
            for (int i = 1; i < N; i++) {
                if (lst.get(lst.size() - 1) < arr[i]) {
                    lst.add(arr[i]);
                }else{
                    int idx = Collections.binarySearch(lst, arr[i]);
                    if (idx < 0) {
                        idx = -idx - 1;
                        lst.set(idx, arr[i]);
                    }
                }
            }
            sb.append("#").append(t).append(" ").append(lst.size()).append("\n");
        }
        System.out.println(sb);
    }
}