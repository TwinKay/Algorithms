import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[][] graph;

    static int[] arrForPerm;
    static List<int[]> orders = new ArrayList<>();

    static int min = Integer.MAX_VALUE;

    public static void Perm(int cnt, int[] save, boolean[] visited){
        if (cnt == arrForPerm.length){
            orders.add(save.clone());
            return;
        }
        for (int i = 0; i < arrForPerm.length; i++){
            if (visited[i]) continue;
            visited[i] = true;
            save[cnt] = i;
            Perm(cnt + 1, save, visited);
            visited[i] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int N = Integer.parseInt(token.nextToken());
        int M = Integer.parseInt(token.nextToken());
        int k = Integer.parseInt(token.nextToken());

        arrForPerm = new int[k];
        for (int i = 0; i < k; i++) {
            arrForPerm[i] = i;
        }
        Perm(0,new int[k], new boolean[k]);

        graph = new int[N][M];
        for (int i=0; i<N; i++){
            token = new StringTokenizer(input.readLine());
            for (int j=0; j<M; j++){
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        int[][] method = new int[k][3];

        for (int t=0; t<k; t++){
            token = new StringTokenizer(input.readLine());
            int r = Integer.parseInt(token.nextToken())-1;
            int c = Integer.parseInt(token.nextToken())-1;
            int s = Integer.parseInt(token.nextToken());
            method[t] = new int[]{r,c,s};
        }

        for (int[] order : orders){
            int[][] graphCopy = new int[N][M];
            for (int i = 0; i < N; i++) {
                graphCopy[i] = graph[i].clone();
            }

            for (int t=0; t<k; t++){
                int r = method[order[t]][0];
                int c = method[order[t]][1];
                int s = method[order[t]][2];

                for (int i = 1; i <= s; i++) {
                    int top = r-i, bottom = r+i;
                    int left = c-i, right = c+i;

                    int temp = graphCopy[top][left];

                    for (int j = top; j < bottom; j++) {
                        graphCopy[j][left] = graphCopy[j + 1][left];
                    }
                    for (int j = left; j < right; j++) {
                        graphCopy[bottom][j] = graphCopy[bottom][j + 1];
                    }
                    for (int j = bottom; j > top; j--) {
                        graphCopy[j][right] = graphCopy[j - 1][right];
                    }
                    for (int j = right; j > left; j--) {
                        graphCopy[top][j] = graphCopy[top][j - 1];
                    }
                    graphCopy[top][left + 1] = temp;
                }
            }
            int eachMin = Integer.MAX_VALUE;
            for (int[] g : graphCopy){
                int temp = Arrays.stream(g).sum();
                if (temp < eachMin){
                    eachMin = temp;
                }
            }
            if (eachMin < min){
                min = eachMin;
            }
        }
        System.out.println(min);
    }
}