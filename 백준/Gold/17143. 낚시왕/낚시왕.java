import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int R,C,M;
    static Shark[][] graph;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        R = Integer.parseInt(token.nextToken());
        C = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        graph = new Shark[R][C];
        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(input.readLine());
            int r = Integer.parseInt(token.nextToken())-1;
            int c = Integer.parseInt(token.nextToken())-1;
            int s = Integer.parseInt(token.nextToken());
            int d = Integer.parseInt(token.nextToken())-1;
            int z = Integer.parseInt(token.nextToken());
            graph[r][c] = new Shark(s, d, z);
        }
        int res = 0;
        for (int i = 0; i < C; i++) {
            res += fishing(i);
            moving();
        }
        System.out.println(res);

    }
    private static void moving() {
        Shark[][] newGraph = new Shark[R][C];
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (graph[r][c] != null) {
                    Shark shark = graph[r][c];
                    int d = shark.direct;
                    int s = shark.speed;

                    int nr = r;
                    int nc = c;

                    if (d == 0 || d == 1) {
                        s %= (R-1)*2;
                    } else {
                        s %= (C-1)*2;
                    }

                    for (int i = 0; i < s; i++) {
                        int tr = nr + dr[d];
                        int tc = nc + dc[d];

                        if (tr < 0 || tr >= R || tc < 0 || tc >= C) {
                            if (d == 0) {
                                d = 1;
                            } else if (d == 1) {
                                d = 0;
                            } else if (d == 2) {
                                d = 3;
                            } else if (d == 3) {
                                d = 2;
                            }
                            tr = nr+dr[d];
                            tc = nc+dc[d];
                        }
                        nr = tr;
                        nc = tc;
                    }
                    shark.direct = d;

                    if (newGraph[nr][nc] == null || newGraph[nr][nc].size < shark.size) {
                        newGraph[nr][nc] = shark;
                    }
                }
            }
        }
        graph = newGraph;
    }

    public static int fishing(int col) {
        for (int i = 0; i < R; i++) {
            if (graph[i][col]!=null){
                int size = graph[i][col].size;
                graph[i][col] = null;
                return size;
            }
        }

        return 0;
    }

    public static class Shark{
        int speed;
        int direct;
        int size;
        Shark(int speed, int direct, int size){
            this.speed = speed;
            this.direct = direct;
            this.size = size;
        }

    }
}

