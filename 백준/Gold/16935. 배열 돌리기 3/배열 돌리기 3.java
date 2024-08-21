import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int n;
    static int m;
    static int r;
    static int[][] graph;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());
        r = Integer.parseInt(token.nextToken());

        graph = new int[n][m];
        for (int i=0; i<n; i++){
            token = new StringTokenizer(input.readLine());
            for (int j=0; j<m; j++){
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        token = new StringTokenizer(input.readLine());
        int[] order = new int[r];
        for (int i=0; i<r; i++){
            order[i] = Integer.parseInt(token.nextToken());
        }

        List<Integer> orderList = new ArrayList<>();
        int z = 0;
        while (z < r) {
            if (z+3 < r) {
                if ((order[z] == 3 && order[z+1] == 3 && order[z+2] == 3 && order[z+3] == 3) ||
                        (order[z] == 4 && order[z+1] == 4 && order[z+2] == 4 && order[z+3] == 4) ||
                        (order[z] == 5 && order[z+1] == 5 && order[z+2] == 5 && order[z+3] == 5) ||
                        (order[z] == 6 && order[z+1] == 6 && order[z+2] == 6 && order[z+3] == 6)) {
                    z += 4;
                    continue;
                }
            }
            if (z+1 < r) {
                if ((order[z] == 1 && order[z+1] == 1) ||
                        (order[z] == 2 && order[z+1] == 2) ||
                        (order[z] == 3 && order[z+1] == 4) ||
                        (order[z] == 4 && order[z+1] == 3) ||
                        (order[z] == 5 && order[z+1] == 6) ||
                        (order[z] == 6 && order[z+1] == 5)) {
                    z += 2;
                    continue;
                }
            }
            orderList.add(order[z]);
            z++;
        }

        for (int i=0; i<orderList.size(); i++){
            int ord = orderList.get(i);
            if (ord == 1){
                graph = cal1();
            }else if (ord == 2){
                graph = cal2();
            }else if (ord == 3){
                graph = cal3();
            }else if (ord == 4){
                graph = cal4();
            }else if (ord == 5){
                graph = cal5();
            }else if (ord == 6){
                graph = cal6();
            }
        }
        for (int[] temp : graph){
            for (int i=0; i<temp.length; i++){
                sb.append(temp[i]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static int[][] cal1(){
        int[][] newGraph = new int[n][m];
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                newGraph[n-1-i][j] = graph[i][j];
            }
        }
        return newGraph;
    }

    public static int[][] cal2(){
        int[][] newGraph = new int[n][m];
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                newGraph[i][j] = graph[i][m-1-j];
            }
        }
        return newGraph;
    }

    public static int[][] cal3(){
        int[][] newGraph = new int[m][n];
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                newGraph[i][j] = graph[n-1-j][i];
            }
        }
        int temp = m;
        m = n;
        n = temp;

        return newGraph;
    }

    public static int[][] cal4(){
        int[][] newGraph = new int[m][n];
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                newGraph[i][j] = graph[j][m-1-i];
            }
        }
        int temp = m;
        m = n;
        n = temp;

        return newGraph;
    }

    public static int[][] cal5(){
        int[][] newGraph = new int[n][m];
        for (int i=0; i<n/2; i++){
            for (int j=0; j<m/2; j++){
                newGraph[i][j+m/2] = graph[i][j];
            }
        }
        for (int i=0; i<n/2; i++){
            for (int j=m/2; j<m; j++){
                newGraph[i+n/2][j] = graph[i][j];
            }
        }
        for (int i=n/2; i<n; i++){
            for (int j=m/2; j<m; j++){
                newGraph[i][j-m/2] = graph[i][j];
            }
        }
        for (int i=n/2; i<n; i++){
            for (int j=0; j<m/2; j++){
                newGraph[i-n/2][j] = graph[i][j];
            }
        }
        return newGraph;
    }

    public static int[][] cal6(){
        int[][] newGraph = new int[n][m];
        for (int i=0; i<n/2; i++){
            for (int j=0; j<m/2; j++){
                newGraph[i+n/2][j] = graph[i][j];
            }
        }
        for (int i=0; i<n/2; i++){
            for (int j=m/2; j<m; j++){
                newGraph[i][j-m/2] = graph[i][j];
            }
        }
        for (int i=n/2; i<n; i++){
            for (int j=m/2; j<m; j++){
                newGraph[i-n/2][j] = graph[i][j];
            }
        }
        for (int i=n/2; i<n; i++){
            for (int j=0; j<m/2; j++){
                newGraph[i][j+m/2] = graph[i][j];
            }
        }
        return newGraph;
    }
}