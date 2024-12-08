import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int testCase;
    static int[] arr;
    static boolean[] visited;
    static int[][] overalls;
    static int bestScore;

    public static void main(String[] args) throws IOException {
        testCase = Integer.parseInt(input.readLine());
        for (int c = 0; c < testCase; c++) {
            arr = new int[11];
            visited = new boolean[12];
            overalls = new int[11][11];
            for (int i = 0; i < 11; i++) {
                token = new StringTokenizer(input.readLine());
                for (int j = 0; j < 11; j++) {
                    overalls[i][j] = Integer.parseInt(token.nextToken());
                }
            }
            bestScore = 0;
            permutation(0);
            sb.append(bestScore).append("\n");
        }
        System.out.println(sb);
    }
    private static void permutation(int cnt) {
        if (cnt == 11) {
            int sumScore = 0;
            for (int i = 0; i < 11; i++) {
                sumScore += overalls[i][arr[i]];
            }
            bestScore = Math.max(bestScore, sumScore);
            return;
        }
        for (int i = 0; i < 11; i++) {
            if (!visited[i] && overalls[cnt][i] > 0) {
                visited[i] = true;
                arr[cnt] = i;
                permutation(cnt+1);
                visited[i] = false;
            }
        }
    }
}