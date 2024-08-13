import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static int res = 0;
    public static void Permu(int cnt, int[] kit, int k, boolean[] visited, int[] save){
        if(cnt == kit.length){
            int total = 0;
            for (int weight : save){
                total = total + weight - k;
                if (total < 0){
                    return;
                }
            }
            res ++;
            return;
        }
        for(int i = 0; i < kit.length; i++){
            if(visited[i]){
                continue;
            }
            visited[i] = true;
            save[cnt] = kit[i];
            Permu(cnt+1, kit, k, visited, save);
            visited[i] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(tokens.nextToken());
        int k = Integer.parseInt(tokens.nextToken());
        tokens = new StringTokenizer(input.readLine());
        int[] kit = new int[n];
        for (int i = 0; i < n; i++) {
            kit[i] = Integer.parseInt(tokens.nextToken());
        }
        Permu(0,kit,k,new boolean[n],new int[n]);
        System.out.println(res);
    }
}