import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N=8;
    static char[][] graph;
    static boolean[][] visited;
    static boolean isFind;
    static int[] deltaX = {0,0,-1,1,1,1,-1,1,0};
    static int[] deltaY = {1,-1,0,0,1,-1,-1,1,0};

    public static void main(String[] args) throws IOException {
        graph = new char[N][N];
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            graph[i] = s.toCharArray();
        }
        graph[N-1][0] = 'P';
        isFind = false;
        while(isNotClear()){
            graph = moveP();
            if (isFind) break;
        }
        if(isFind){
            System.out.println(1);
        }else{
            System.out.println(0);
        }

    }
    public static boolean isNotClear() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(graph[i][j] != '.') {
                    return true;
                }
            }
        }
        return false;
    }
    public static char[][] moveP(){
        char[][] newGraph = new char[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                newGraph[i][j] = '.';
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j] == 'P') {
                    for (int k = 0; k < 9; k++) {
                        int dx = j+deltaX[k];
                        int dy = i+deltaY[k];
                        if (isValid(dx,dy) && graph[dy][dx] != '#'){
                            newGraph[dy][dx] = 'P';
                            if(dx==7 && dy==0){
                                isFind = true;
                                return newGraph;
                            }
                        }
                    }
                }
            }
        }

        char[][] newGraph2 = new char[N][N];
        for (int i = 0; i < N; i++) {
            newGraph2[i] = newGraph[i].clone();
        }
        List<int[]> wallIdxs = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j] == '#') {
                    wallIdxs.add(new int[]{j,i});
                    newGraph2[i][j] = '.';
                }
            }
        }
        for (int[] wallIdx : wallIdxs) {
            int dx = wallIdx[0];
            int dy = wallIdx[1]+1;
            if (isValid(dx, dy)) {
                newGraph2[dy][dx] = '#';
            }
        }

        return newGraph2;
    }
    public static char[][] moveW(){
        char[][] newGraph2 = new char[N][N];
        for (int i = 0; i < N; i++) {
            newGraph2[i] = graph[i].clone();
        }
        List<int[]> wallIdxs = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j] == '#') {
                    wallIdxs.add(new int[]{j,i});
                    newGraph2[i][j] = '.';
                }
            }
        }
        for (int[] wallIdx : wallIdxs) {
            int dx = wallIdx[0];
            int dy = wallIdx[1]+1;
            if (isValid(dx, dy)) {
                newGraph2[dy][dx] = '#';
            }
        }
        return newGraph2;
    }

    public static boolean isValid(int x, int y){
        return x>=0 && x<N && y>=0 && y<N;
    }

}