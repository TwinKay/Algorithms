import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int n;
    static boolean[][] graph, newGraph;
    static List<int[]> cores;
    static List<boolean[]> posiDirect; // core들 idx 저장
    static int [] deltaX = {1,0,0,-1};
    static int [] deltaY = {0,1,-1,0};

    static int posiCore;
    static int junsun;
    static int T;
    static int alreadyConnected;
    static int imposiCnt;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t=1; t<=T; t++) {
            posiCore = 0;
            cores =  new ArrayList<int[]>();
            posiDirect = new ArrayList<>();
            junsun = Integer.MAX_VALUE;
            alreadyConnected = 0;
            n = Integer.parseInt(input.readLine());
            graph = new boolean[n][n];
            for (int i = 0; i < n; i++) {
                token = new StringTokenizer(input.readLine());
                for (int j = 0; j < n; j++) {
                    int temp = Integer.parseInt(token.nextToken());
                    if (temp==1){
                        graph[i][j] = true;
                        if (i==0 || j==0 || i==n-1 || j==n-1){
                            alreadyConnected++;
                        }else{
                            cores.add(new int[]{j,i});
                            posiDirect.add(possibleDirect(j,i));
                        }

                    }
                }
            }
            Perm(0, new int[cores.size()]);
            sb.append("#").append(t).append(" ").append(junsun).append("\n");
        }
        System.out.println(sb);
    }
    public static void Perm(int cnt, int[] save){
        if (cnt==cores.size()){

            newGraph = new boolean[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    newGraph[i][j] = graph[i][j];
                }
            }
            int cntCore = alreadyConnected;
            int eachJunsunSum = 0;
            imposiCnt = 0;
            for (int i = 0; i < save.length; i++) {
                int coreX = cores.get(i)[0];
                int coreY = cores.get(i)[1];
                if (isPossible(coreX,coreY,save[i])){
                    eachJunsunSum += move(coreX,coreY,save[i]);
                    cntCore++;
                }
                if (alreadyConnected+cores.size()-imposiCnt<posiCore){
                    return;
                }
            }
            if (cntCore>posiCore){
                posiCore = cntCore;
                junsun = eachJunsunSum;
            }else if (cntCore==posiCore){
                junsun = Math.min(junsun,eachJunsunSum);
            }
            return;
        }
        for (int i = 0; i < 4; i++) {
            if (!posiDirect.get(cnt)[i]) {
                continue;
            }
            save[cnt] = i;
            Perm(cnt + 1, save);
        }

    }
    public static int move(int x, int y, int direct){
        int dx = x+deltaX[direct];
        int dy = y+deltaY[direct];
        int cnt = 0;
        while (isValid(dx,dy)){
            newGraph[dy][dx] = true;
            dx += deltaX[direct];
            dy += deltaY[direct];
            cnt++;
        }
        return cnt;
    }
    public static boolean[] possibleDirect(int x, int y){
        boolean[] directs = new boolean[4];
        for (int i=0; i<4; i++){
            if(isPossibleForInit(x,y,i)){
                directs[i] = true;
            }
        }
        return directs;
    }
    public static boolean isPossibleForInit(int x, int y, int direct){
        int dx = x+deltaX[direct];
        int dy = y+deltaY[direct];
        while (isValid(dx,dy)){
            if (graph[dy][dx]){
                imposiCnt ++;
                return false;
            }
            dx += deltaX[direct];
            dy += deltaY[direct];
        }
        return true;
    }

    public static boolean isPossible(int x, int y, int direct){
        int dx = x+deltaX[direct];
        int dy = y+deltaY[direct];
        while (isValid(dx,dy)){
            if (newGraph[dy][dx]){
                imposiCnt ++;
                return false;
            }
            dx += deltaX[direct];
            dy += deltaY[direct];
        }
        return true;
    }

    public static boolean isValid(int x, int y){
        return x>=0 && x<n && y>=0 && y<n;
    }
}