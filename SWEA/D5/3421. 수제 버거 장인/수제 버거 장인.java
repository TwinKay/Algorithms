import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;
 
public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer tokens;
 
    static boolean[] isSelected;
    static int n, m;
    static int[] arr;
    static Map<Integer, Set<Integer>> map;
    static int res;
 
    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            res = 0;
            tokens = new StringTokenizer(input.readLine());
            n = Integer.parseInt(tokens.nextToken());
            m = Integer.parseInt(tokens.nextToken());
 
            isSelected = new boolean[n+1];
            arr = new int[n];
            map = new HashMap<>();
 
            for (int i = 0; i < n; i++) {
                arr[i] = i+1;
            }
 
            for (int i = 0; i < m; i++) {
                tokens = new StringTokenizer(input.readLine());
                int a = Integer.parseInt(tokens.nextToken());
                int b = Integer.parseInt(tokens.nextToken());
 
                if (!map.containsKey(a)) {
                    map.put(a, new HashSet<>());
                    map.get(a).add(b);
                } else{
                    map.get(a).add(b);
                }
                if (!map.containsKey(b)) {
                    map.put(b, new HashSet<>());
                    map.get(b).add(a);
                } else{
                    map.get(b).add(a);
                }
 
            }
            subset(1);
            sb.append("#").append(t).append(" ").append(res).append("\n");
        }
        System.out.println(sb);
    }
 
    private static void subset(int cnt) {
        if (cnt == n+1) {
            res ++;
            return;
        }
 
        if (isValid(cnt)) {
            isSelected[cnt] = true;
            subset(cnt + 1);
        }
 
        isSelected[cnt] = false;
        subset(cnt + 1);
    }
 
    private static boolean isValid(int cnt) {
        if (map.containsKey(cnt)) {
            for (int comp : map.get(cnt)) {
                if (isSelected[comp]) {
                    return false;
                }
            }
        }
        return true;
    }
}