import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
 
public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer tokens;
    static List<int[]> cands;
 
    public static void Permu(int cnt, int max, int[] arr, int[] save) {
        if (cnt == save.length) {
            cands.add(save.clone());
            return;
        }
        for (int i = 0; i < max; i++) {
 
            save[cnt] = arr[i];
            Permu(cnt + 1, max, arr, save);
 
        }
    }
 
    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 0; t < T; t++) {
            tokens = new StringTokenizer(input.readLine());
            int n = Integer.parseInt(tokens.nextToken());
            int x = Integer.parseInt(tokens.nextToken());
            int m = Integer.parseInt(tokens.nextToken());
 
 
            int[] arr = new int[x+1];
            for (int i = 0; i < x+1; i++) {
                arr[i] = i;
            }
            cands = new ArrayList<>();
            Permu(0, x+1, arr, new int[n]);
 
            List<int[]> missions = new ArrayList<>();
            for (int a = 0; a < m; a++) {
                tokens = new StringTokenizer(input.readLine());
                int l = Integer.parseInt(tokens.nextToken());
                int r = Integer.parseInt(tokens.nextToken());
                int s = Integer.parseInt(tokens.nextToken());
                missions.add(new int[]{l, r, s});
            }
 
            List<int[]> passes = new ArrayList<>();
            for (int[] cand : cands) {
                boolean passFlag = true;
                for (int[] mission : missions) {
                    int left = mission[0];
                    int right = mission[1];
                    int num = mission[2];
 
                    int cnt = 0;
                    for (int i = left; i <= right; i++) {
                        cnt += cand[i-1];
                    }
 
                    if (cnt != num) {
                        passFlag = false;
                        break;
                    }
 
                }
                if (passFlag) {
                    passes.add(cand);
                }
            }
 
            List<int[]> lastCands = new ArrayList<>();
 
            int maxCnt = 0;
            for (int[] pass : passes){
                int cnt = 0;
                for (int c : pass){
                    cnt += c;
                }
                if (cnt > maxCnt) {
                    maxCnt = cnt;
                }
            }
            for (int[] pass : passes){
                int cnt = 0;
                for (int c : pass){
                    cnt += c;
                }
                if (cnt == maxCnt){
                    lastCands.add(pass);
                }
            }
            if (lastCands.isEmpty()){
                sb.append("#").append(t+1).append(" ").append(-1).append("\n");
            }else {
                sb.append("#").append(t+1).append(" ");
                int[] res = lastCands.get(0);
                for (int s : res){
                    sb.append(s).append(" ");
                }
                sb.append("\n");
            }
        }
        output.write(sb.toString());
        output.flush();
    }
}