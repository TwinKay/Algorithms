import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int N,M;
    static int[][] students;
    static int[] idxs;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        students = new int[N][M];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < M; j++) {
                students[i][j] = Integer.parseInt(token.nextToken());
            }
            Arrays.sort(students[i]);
        }
        idxs = new int[N];
        int min = Integer.MAX_VALUE;
        while (true) {
            int minVal = Integer.MAX_VALUE;
            int maxVal = Integer.MIN_VALUE;
            int minIdx = 0;
            for (int i = 0; i < N; i++) {
                if (students[i][idxs[i]] < minVal) {
                    minVal = students[i][idxs[i]];
                    minIdx = i;
                } 
                if (students[i][idxs[i]] > maxVal) {
                    maxVal = students[i][idxs[i]];
                }
            }
            if (maxVal-minVal < min) min = maxVal-minVal;
            idxs[minIdx] ++;
            if (idxs[minIdx] >= M) break;;
        }
        System.out.println(min);
    }
}