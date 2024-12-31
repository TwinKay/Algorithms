import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static int[][] graph;
    static List<int[]> firstCloud;
    static int[] deltaX = {-1,-1,0,1,1,1,0,-1};
    static int[] deltaY = {0,-1,-1,-1,0,1,1,1};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        graph = new int[N][N];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }
        firstCloud = new ArrayList<>();
        firstCloud.add(new int[]{0, N-2});
        firstCloud.add(new int[]{1, N-2});
        firstCloud.add(new int[]{0, N-1});
        firstCloud.add(new int[]{1, N-1});

        while (M-->0){
            token = new StringTokenizer(input.readLine());
            int drt = Integer.parseInt(token.nextToken());
            drt--;
            int len = Integer.parseInt(token.nextToken());
            for (int i = 0; i < firstCloud.size(); i++) {
                firstCloud.get(i)[0] = moveMod(firstCloud.get(i)[0]+deltaX[drt]*len);
                firstCloud.get(i)[1] = moveMod(firstCloud.get(i)[1]+deltaY[drt]*len);
            }
            for (int[] cloudIdx : firstCloud){
                graph[cloudIdx[1]][cloudIdx[0]]++;
            }
            for (int[] cloudIdx : firstCloud){
                int cnt = countWaterBasket(cloudIdx[0],cloudIdx[1]);
                graph[cloudIdx[1]][cloudIdx[0]] += cnt;
            }
            List<int[]> newFirstCloud = new ArrayList<>();
            for (int x = 0; x < N; x++){
                for (int y = 0; y < N; y++){
                    if (graph[y][x] >= 2 && !isFirstCloud(x,y)){
                        graph[y][x] -= 2;
                        newFirstCloud.add(new int[]{x, y});
                    }
                }
            }
            firstCloud = newFirstCloud;
        }
        int res = 0;
        for (int[] g : graph){
            for (int water : g){
                res += water;
            }
        }
        System.out.println(res);
    }

    static boolean isFirstCloud(int x, int y){
        for (int[] fCloud : firstCloud){
            if (fCloud[0] == x && fCloud[1] == y){
                return true;
            }
        }
        return false;
    }

    static boolean isValid(int x, int y){
        return x>=0 && x<N && y>=0 && y<N;
    }
    
    static int countWaterBasket(int x, int y){
        int[] drts = {1,3,5,7};
        int cnt = 0;
        for (int i = 0; i < 4; i++) {
            int dx = x + deltaX[drts[i]];
            int dy = y + deltaY[drts[i]];
            if (isValid(dx,dy)){
                if (graph[dy][dx] != 0){
                    cnt++;
                }
            }
        }
        return cnt;
    }

    static int moveMod(int idx){
        int modIdx = idx%N;
        while (modIdx<0){
            modIdx+=N;
        }
        return modIdx;
    }
}