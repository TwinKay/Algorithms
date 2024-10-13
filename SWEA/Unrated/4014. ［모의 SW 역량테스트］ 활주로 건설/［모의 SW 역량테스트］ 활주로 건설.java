import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;

    static int N, X, T;
    static int[][] graph;
    static int res;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            token = new StringTokenizer(br.readLine());
            N = Integer.parseInt(token.nextToken());
            X = Integer.parseInt(token.nextToken());
            graph = new int[N][N];

            for (int i = 0; i < N; i++) {
                token = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(token.nextToken());
                }
            }
            res = 0;
            for (int i = 0; i < N; i++) {
                if (isValid(graph[i])) {
                    res++;
                }
            }

            for (int i = 0; i < N; i++) {
                int[] col = new int[N];
                for (int j = 0; j < N; j++) {
                    col[j] = graph[j][i];
                }
                if (isValid(col)) {
                    res++;
                }
            }
            sb.append("#").append(t).append(" ").append(res).append("\n");
        }
        System.out.println(sb);
    }

    static boolean isValid(int[] road){
        boolean[] build = new boolean[N];

        for(int i = 0; i < N-1; i++){
            if(road[i] == road[i+1]) {
                continue;
            }

            else if (road[i]+1 == road[i+1]){
                for(int j = 0; j < X; j++){
                    int idx = i-j;
                    if(idx < 0 || road[idx] != road[i] || build[idx]){
                        return false;
                    }
                    build[idx] = true;
                }
            }

            else if(road[i] - 1 == road[i+1]){
                for(int j = 1; j <= X; j++){
                    int idx = i+j;
                    if(idx >= N || road[idx] != road[i+1] || build[idx]){
                        return false;
                    }
                    build[idx] = true;
                }
                i += X-1;
            }
            else{
                return false;
            }
        }
        return true;
    }
}