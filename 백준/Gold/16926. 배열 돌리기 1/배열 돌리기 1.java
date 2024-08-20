import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int[][] graph;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(token.nextToken());
        int m = Integer.parseInt(token.nextToken());
        int r = Integer.parseInt(token.nextToken());

        graph = new int[n][m];
        for (int i=0; i<n; i++){
            token = new StringTokenizer(input.readLine());
            for (int j=0; j<m; j++){
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        for(int i=0; i < Math.min(n,m)/2; i++){
            int size = 2*(n+m)-4-(8*i);
            int[] cover = new int[size];

            int idx = 0;
            // 위쪽
            for (int j=i; j<m-i; j++) {
                cover[idx++] = graph[i][j];
            }
            // 오른쪽
            for (int j=i+1; j<n-i; j++) {
                cover[idx++] = graph[j][m-i-1];
            }
            // 아래쪽
            for (int j=m-i-2; j>=i; j--) {
                cover[idx++] = graph[n-i-1][j];
            }
            // 왼쪽
            for (int j=n-i-2; j>i; j--) {
                cover[idx++] = graph[j][i];
            }

            int[] movedCover = new int[size];
            int move = r % size;

            System.arraycopy(cover, move, movedCover, 0, size - move); // 1.기존 배열 2.기존 배열 start idx 3.저장 배열 4.저장 배열 start idx 5.배열 길이
            System.arraycopy(cover, 0, movedCover, size - move, move);

            idx = 0;
            // 위쪽
            for (int j=i; j<m-i; j++) {
                graph[i][j] = movedCover[idx++];
            }
            // 오른쪽
            for (int j=i+1; j<n-i; j++) {
                graph[j][m-i-1] = movedCover[idx++];
            }
            // 아래쪽
            for (int j=m-i-2; j>=i; j--) {
                graph[n-i-1][j] = movedCover[idx++];
            }
            // 왼쪽
            for (int j=n-i-2; j>i; j--) {
                graph[j][i] = movedCover[idx++];
            }
        }

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                sb.append(graph[i][j]).append(" ");
            }
            sb.append('\n');
        }
        System.out.print(sb.toString());
    }
}