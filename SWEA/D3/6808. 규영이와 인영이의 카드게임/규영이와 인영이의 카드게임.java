import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
 
public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer tokens;
    static List<Integer> enemyArr;
    static List<Integer> myArr;
    static int res1;
    static int res2;
 
    public static void Permu(int cnt, List<Integer> myArr, boolean[] visited, int[] save) {
        if (cnt == 9) {
            int myScore = 0;
            int enemyScore = 0;
            for (int i = 0; i < 9; i++) {
                if (save[i]>enemyArr.get(i)){
                    myScore += save[i]+enemyArr.get(i);
                } else if (save[i]<enemyArr.get(i)){
                    enemyScore += enemyArr.get(i)+save[i];
                }
 
            }
            if (myScore>enemyScore){
                res1 ++;
            } else if (myScore<enemyScore){
                res2 ++;
            }
            return;
        }
        for (int i = 0; i < 9; i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            save[cnt] = myArr.get(i);
            Permu(cnt + 1, myArr, visited, save);
            visited[i] = false;
        }
    }
 
    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
 
        for (int t=0; t<T; t++) {
            res1 = 0;
            res2 = 0;
            myArr = new ArrayList<>();
            enemyArr = new ArrayList<>();
            tokens = new StringTokenizer(input.readLine());
             
            for (int i = 0; i < 9; i++) {
                enemyArr.add(Integer.parseInt(tokens.nextToken()));
            }
            for (int i=1; i<19; i++){
                if (!enemyArr.contains(i)){
                    myArr.add(i);
                }
            }
 
            Permu(0, myArr, new boolean[9], new int[9]);
            System.out.println("#"+(t+1)+" "+res2+ " "+res1);
        }
    }
}