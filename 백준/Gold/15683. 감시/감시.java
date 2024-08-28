import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n,m, cctvNum, wallNum, min;
    static int[][] graph;
    static boolean[][] secuArea;
    static int[][] cctvInfo;
    static int[][] eachCctvCase = {{0,1,2,3},{0,1},{0,1,2,3},{0,1,2,3},{0}};
    static int[] deltaX = {0,1,0,-1};
    static int[] deltaY = {1,0,-1,0};
    
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());

        graph = new int[n][m];
        cctvNum = 0;
        wallNum = 0;
        cctvInfo = new int[8][3]; // 빈 공간 있을 수 있음
        for (int i = 0; i < n; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < m; j++) {
                int num = Integer.parseInt(token.nextToken());
                graph[i][j] = num;
                if (num > 0 && num <=5){
                    cctvInfo[cctvNum] = new int[]{num,j,i};
                    cctvNum++;
                }else if(num == 6){
                    wallNum++;
                }
            }
        }

        min = Integer.MAX_VALUE;
        Perm(0,new int[cctvNum]);
        System.out.println(min);
    }
    public static void Perm(int cnt, int[] save){
        if (cnt == cctvNum){
            secuArea = new boolean[n][m];
            for (int i = 0; i < cctvNum; i++) {
                order(cctvInfo[i][0],cctvInfo[i][1],cctvInfo[i][2],save[i]);
            }

            int res = 0;
            for (int i=0; i<n; i++){
                for (int j=0; j<m; j++){
                    if (secuArea[i][j]){
                        res++;
                    }
                }
            }

            if (n*m-res-wallNum < min){
                min = n*m-res-wallNum;
            }
            return;
        }
        for (int i = 0; i < eachCctvCase[cctvInfo[cnt][0] - 1].length; i++) {
            save[cnt] = eachCctvCase[cctvInfo[cnt][0] - 1][i];
            Perm(cnt + 1, save);
        }
    }

    public static void order(int cctvId, int x, int y, int direct) {
        switch (cctvId) {
            case 1:
                move(x, y, direct);
                break;
            case 2:
                move(x, y, direct);
                move(x, y, (direct + 2) % 4);
                break;
            case 3:
                move(x, y, direct);
                move(x, y, (direct + 1) % 4);
                break;
            case 4:
                move(x, y, direct);
                move(x, y, (direct + 1) % 4);
                move(x, y, (direct + 3) % 4);
                break;
            case 5:
                move(x, y, 0);
                move(x, y, 1);
                move(x, y, 2);
                move(x, y, 3);
                break;
        }
    }

    public static void move(int x, int y, int direct) {
        secuArea[y][x] = true;
        while (isValid(x + deltaX[direct], y + deltaY[direct]) && graph[y + deltaY[direct]][x + deltaX[direct]] != 6) {
            x += deltaX[direct];
            y += deltaY[direct];
            secuArea[y][x] = true;
        }
    }

    public static boolean isValid(int x, int y){
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}