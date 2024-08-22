import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
 
public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
 
    static int[] arrForPerm;
    static List<int[]> permList;
     
    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            int n = Integer.parseInt(input.readLine());
            int[] calArr = new int[4];
            int[] numArr = new int[n];
            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;
 
            permList = new ArrayList<>();
 
            token = new StringTokenizer(input.readLine());
            for (int i = 0; i < 4; i++) {
                calArr[i] = Integer.parseInt(token.nextToken());
            }
            token = new StringTokenizer(input.readLine());
            for (int i = 0; i < n; i++){
                numArr[i] = Integer.parseInt(token.nextToken());
            }
 
            arrForPerm= new int[n-1];
            int cnt = 0;
            for (int i=0; i<4; i++){
                for (int j=0; j<calArr[i]; j++){
                    arrForPerm[cnt] = i;
                    cnt++;
                }
            }
            Perm(0, new int[n-1], new boolean[arrForPerm.length]);
 
            for (int[] perm : permList) {
                cnt = numArr[0];
                for (int i=0; i<n-1; i++){
                    if (perm[i]==0){
                        cnt = cnt + numArr[i+1];
                    } else if (perm[i]==1){
                        cnt = cnt - numArr[i+1];
                    } else if (perm[i]==2){
                        cnt = cnt * numArr[i+1];
                    } else{
                        cnt = cnt / numArr[i+1];
                    }
                }
                if (cnt>max){
                    max = cnt;
                }
                if (cnt<min){
                    min = cnt;
                }
            }
            sb.append("#").append(t).append(" ").append(max-min).append("\n");
        }
        System.out.println(sb.toString());
    }
 
    public static void Perm(int cnt, int[] save, boolean[] visited){
        if (cnt == arrForPerm.length){
            permList.add(save.clone());
            return;
        }
 
        for (int i=0; i<arrForPerm.length; i++){
            if (visited[i]) continue;
            if (i>0 && arrForPerm[i] == arrForPerm[i-1] && visited[i-1]) continue; // 중복된 순열 통과
            visited[i] = true;
            save[cnt] = arrForPerm[i];
            Perm(cnt+1, save, visited);
            visited[i] = false;
        }
    }
}