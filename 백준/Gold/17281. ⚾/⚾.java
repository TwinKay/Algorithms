import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int T,max;
    static int[][] rounds;
    static int[] arr = new int[9];
    static boolean[] visited = new boolean[9];

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        max = Integer.MIN_VALUE;
        rounds = new int[T][9];
        for (int i = 0; i < T; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < 9; j++) {
                rounds[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        permutation(0);
        System.out.println(max);
    }

    private static void permutation(int cnt) {
        if (cnt == 9) {
            // 게임 시작
            int score = 0;
            int point = 0;

            for (int t = 0; t < T; t++) {
                Deque<Boolean> base = new ArrayDeque<>();
                for (int i = 0; i < 3; i++) {
                    base.add(false);
                }

                int out = 0;
                while (out<3){
                    int what = rounds[t][arr[point]];
                    if (what == 0){
                        out++;
                    } else if (what == 1){
                        boolean home1 = base.pollLast();
                        base.addFirst(true);
                        if (home1) score++;
                    } else if (what == 2){
                        boolean home1 = base.pollLast();
                        boolean home2 = base.pollLast();
                        base.addFirst(true);
                        base.addFirst(false);
                        if (home1) score++;
                        if (home2) score++;
                    } else if (what == 3){
                        boolean home1 = base.pollLast();
                        boolean home2 = base.pollLast();
                        boolean home3 = base.pollLast();
                        base.addFirst(true);
                        base.addFirst(false);
                        base.addFirst(false);
                        if (home1) score++;
                        if (home2) score++;
                        if (home3) score++;
                    } else{
                        boolean home1 = base.pollLast();
                        boolean home2 = base.pollLast();
                        boolean home3 = base.pollLast();
                        base.addFirst(false);
                        base.addFirst(false);
                        base.addFirst(false);
                        if (home1) score++;
                        if (home2) score++;
                        if (home3) score++;
                        score++;
                    }
                    point++;
                    if (point == 9) point = 0;
                }
            }
            max = Math.max(max, score);
            return;
        }

        if (cnt == 3) {
            arr[3] = 0;
            if (!visited[0]) {
                visited[0] = true;
                permutation(cnt + 1);
                visited[0] = false;
            }
        } else {
            for (int player = 1; player < 9; player++) {
                if (!visited[player]) {
                    visited[player] = true;
                    arr[cnt] = player;
                    permutation(cnt + 1);
                    visited[player] = false;
                }
            }
        }
    }
}
