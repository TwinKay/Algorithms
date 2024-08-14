import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer tokens;

    static int n;
    static int m;
    static int k;
    static int[][] graph;
    static int[][] arr;
    static int res = Integer.MIN_VALUE;

    public static void Perm(int cnt, int[][] save) { // visited는 m*n
        if (cnt == k) {
            // 붙어있는 경우 제외
            int[][] test = save.clone();
            for (int[] a : test){
                for (int[] b : test){
                    if(Arrays.equals(a,(new int[]{b[0],b[1]-1}))){
                        return;
                    }
                    if(Arrays.equals(a,(new int[]{b[0],b[1]+1}))){
                        return;
                    }
                    if(Arrays.equals(a,(new int[]{b[0]-1,b[1]}))){
                        return;
                    }
                    if(Arrays.equals(a,(new int[]{b[0]+1,b[1]}))){
                        return;
                    }
                }
            }

            int cntK = 0;
            for (int[] temp : save) {
                int idxX = temp[0];
                int idxY = temp[1];

                cntK += graph[idxY][idxX];
            }

            if (cntK > res){
                res = cntK;
            }
            return;
        }
        for (int i = 0; i < arr.length; i++) {
            if (cnt != 0){
                if (save[cnt-1][0] > arr[i][0]){
                    continue;
                } else if (save[cnt-1][0] == arr[i][0]){
                    if (save[cnt-1][1] >= arr[i][1]){
                        continue;
                    }
                }
            }

            save[cnt] = arr[i];
            Perm(cnt+1, save);

        }
    }

    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        n = Integer.parseInt(tokens.nextToken());
        m = Integer.parseInt(tokens.nextToken());
        k = Integer.parseInt(tokens.nextToken());
        arr = new int[n*m][2];

        graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            tokens = new StringTokenizer(input.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(tokens.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[m*i+j] = new int[]{j,i};
            }
        }

        Perm(0, new int[k][2]);
        System.out.println(res);
    }
}