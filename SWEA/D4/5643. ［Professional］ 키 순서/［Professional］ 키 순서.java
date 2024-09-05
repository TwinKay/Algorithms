import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static int[][] dist, distReversed;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            N = Integer.parseInt(input.readLine());
            M = Integer.parseInt(input.readLine());

            dist = new int[N+1][N+1];
            distReversed = new int[N+1][N+1];
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (i == j) {
                        dist[i][j] = 0;
                        distReversed[i][j] = 0;
                    } else {
                        dist[i][j] = Integer.MAX_VALUE;
                        distReversed[i][j] = Integer.MAX_VALUE;
                    }
                }
            }

            for (int i = 0; i < M; i++) {
                token = new StringTokenizer(input.readLine());
                int a = Integer.parseInt(token.nextToken());
                int b = Integer.parseInt(token.nextToken());
                dist[a][b] = 1;
                distReversed[b][a] = 1;
            }

            for (int k = 1; k <= N; k++) {
                for (int i = 1; i <= N; i++) {
                    for (int j = 1; j <= N; j++) {
                        if (dist[i][k] != Integer.MAX_VALUE && dist[k][j] != Integer.MAX_VALUE) {
                            dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                        }
                        if (distReversed[i][k] != Integer.MAX_VALUE && distReversed[k][j] != Integer.MAX_VALUE) {
                            distReversed[i][j] = Math.min(distReversed[i][j], distReversed[i][k] + distReversed[k][j]);
                        }
                    }
                }
            }

            int res = 0;
            for (int i = 1; i <= N; i++) {
                int cnt = 0;
                for (int j = 1; j <= N; j++) {
                    if (!(dist[i][j] == Integer.MAX_VALUE)) {
                        cnt++;
                    }
                    if (!(distReversed[i][j] == Integer.MAX_VALUE)) {
                        cnt++;
                    }
                }
                if (cnt==N+1){ // 본인은 두 번 뽑히기 때문
                    res++;
                }
            }
            sb.append("#").append(t).append(" ").append(res).append("\n");
        }
        System.out.println(sb);
    }
}