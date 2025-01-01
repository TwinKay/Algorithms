import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,K,rollCol,rollRow;
    static int[][] graph, rollGraph;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        graph = new int[N][N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            graph[0][i] = Integer.parseInt(token.nextToken());
        }
        int cnt = 0;
        while (true) {
            cnt ++;

            // 물고기 수가 가장 적은 어항에 물고기 넣기
            fishToMin();
            // 굴리기
            roll();
            // 물고기 수 조절
            move();
            // 평탄화
            flat();
            // 접기
            fold();
            // 물고기 수 조절
            move();
            // 평탄화
            flat();
            if (calDiff() <= K) break;
        }
        System.out.println(cnt);
    }

    static void fishToMin() {
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            min = Math.min(min, graph[0][i]);
        }
        List<Integer> mins = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            if (graph[0][i] == min){
                mins.add(i);
            }
        }
        for (int idx : mins) {
            graph[0][idx] ++;
        }
    }

    static void roll() {
        // roll 가능할 때까지
        while (isValid()){
            rollGraph = new int [rollCol][rollRow];
            // rollGraph 채우기
            int firstIdx = -1;
            for (int i = 0; i < N; i++) {
                if (graph[0][i]!=0){
                    firstIdx = i;
                    break;
                }
            }

            for (int i = 0; i < rollCol; i++) {
                for (int j = 0; j < rollRow; j++) {
                    rollGraph[i][j] = graph[i][j+firstIdx];
                    graph[i][j+firstIdx] = 0;
                }
            }

            int[][] newRollGraph = new int[rollRow][rollCol];
            for (int i = 0; i < rollCol; i++) {
                for (int j = 0; j < rollRow; j++) {
                    newRollGraph[rollRow-1-j][i] = rollGraph[i][j];
                }
            }

            for (int i = 0; i < N; i++) {
                if (graph[0][i]!=0){
                    firstIdx = i;
                    break;
                }
            }

            for (int i = 0; i < rollRow; i++) { // new에서는 col
                for (int j = 0; j < rollCol; j++) {
                    graph[i+1][j+firstIdx] = newRollGraph[i][j];
                }
            }
        }
    }

    static boolean isValid() {
        int colLen = 0;
        flag:
        for (int i = 0; i < N; i++) {
            if (graph[0][i]!=0){
                int cnt = 0;
                for (int j = 0; j < N; j++) {
                    if (graph[j][i] != 0){
                        cnt++;
                    }else{
                        colLen = cnt;
                        break flag;
                    }
                }
            }
        }
        int cntFirstBlanks = 0;
        int rowLen = N;
        boolean isFind = false;
        for (int i = 0; i < N; i++) {
            if (!isFind){
                cntFirstBlanks ++;
            }
            if (graph[1][i]!=0){
                isFind = true;
            }
            if (isFind && graph[1][i]==0){
                rowLen = N-1-i;
                break;
            }
        }
        if (isFind && rowLen==N) rowLen = 0;
        if (colLen<=(rowLen+1)){
            rollCol = colLen;
            rollRow = N-rowLen-cntFirstBlanks;
            if (rollRow<0) rollRow = 1;
            return true;
        }else{
            return false;
        }
    }

    static void move() {
        int[][] moveGraph = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j]!=0){
                    int[] deltaX = {-1,0,1,0};
                    int[] deltaY = {0,-1,0,1};
                    for (int k = 0; k < 4; k++) {
                        int x = j+deltaX[k];
                        int y = i+deltaY[k];
                        if (inRange(x,y) && graph[y][x]!=0){
                            if (graph[i][j]<graph[y][x]){
                                int diff = graph[y][x]-graph[i][j];
                                int num = diff/5;
                                if (num>0){
                                    moveGraph[i][j] += num;
                                    moveGraph[y][x] -= num;
                                }
                            }
                        }
                    }
                }
            }
        }
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                graph[i][j] += moveGraph[i][j];
            }
        }
    }

    static boolean inRange(int x, int y){
        return x>=0 && x<N && y>=0 && y<N;
    }

    static void flat(){
        int idx = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[j][i]!=0){
                    graph[0][idx] = graph[j][i];
                    if (j!=0) graph[j][i] = 0;
                    idx ++;
                }
            }
        }
    }

    static void fold(){
        // 1접
        for (int i = 0; i < N/2; i++) {
            graph[1][N-1-i] = graph[0][i];
            graph[0][i] = 0;
        }

        // 2접
        for (int i = N/2; i < N/2+N/4; i++) {
            graph[3][N-1-i+N/2] = graph[0][i];
            graph[0][i] = 0;
            graph[2][N-1-i+N/2] = graph[1][i];
            graph[1][i] = 0;
        }
    }
    
    static int calDiff() {
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            max = Math.max(max, graph[0][i]);
            min = Math.min(min, graph[0][i]);
        }
        return max - min;
    }
}