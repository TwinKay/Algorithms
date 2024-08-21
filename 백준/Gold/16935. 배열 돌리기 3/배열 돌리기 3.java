import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int n;
    static int m;
    static int[][] graph;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());
        int r = Integer.parseInt(token.nextToken());

        graph = new int[n][m];
        for (int i=0; i<n; i++){
            token = new StringTokenizer(input.readLine());
            for (int j=0; j<m; j++){
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        token = new StringTokenizer(input.readLine());
        for (int i=0; i<r; i++){
            int order =  Integer.parseInt(token.nextToken());
            if (order == 1){
                graph = cal1();
            }else if (order == 2){
                graph = cal2();
            }else if (order == 3){
                graph = cal3();
            }else if (order == 4){
                graph = cal4();
            }else if (order == 5){
                graph = cal5();
            }else if (order == 6){
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