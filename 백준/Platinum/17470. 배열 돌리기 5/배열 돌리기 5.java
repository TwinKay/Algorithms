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
    static int[][] graph;
    static int[][] innerGraph;
    static int[][] outerGraph;

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

        innerGraph = new int[][]{{1, 2}, {4, 3}};
        outerGraph = new int[][]{{1, 2}, {4, 3}};

        token = new StringTokenizer(input.readLine());
        for (int z=0; z<r; z++){
            int ord = Integer.parseInt(token.nextToken());
            if (ord == 1){
                innerGraph = innerOrd1();
                outerGraph = outerOrd1();
            } else if (ord == 2){
                innerGraph = innerOrd2();
                outerGraph = outerOrd2();
            }else if (ord == 3){
                innerGraph = innerOrd3();
                outerGraph = outerOrd3();
            }else if (ord == 4){
                innerGraph = innerOrd4();
                outerGraph = outerOrd4();
            }else if (ord == 5){
                outerGraph = outerOrd5();
            }else if (ord == 6){
                outerGraph = outerOrd6();
            }
        }
        boolean innerHoriFlip = false;
        int innerRotateRight = 0;

        for (int i=0; i<4; i++){
            if (Arrays.equals(innerGraph[0],new int[]{1,2})){
                break;
            }else {
                int[][] tempGraph = new int[2][2];
                tempGraph[0][1] = innerGraph[0][0];
                tempGraph[1][1] = innerGraph[0][1];
                tempGraph[0][0] = innerGraph[1][0];
                tempGraph[1][0] = innerGraph[1][1];
                innerGraph = tempGraph;
                innerRotateRight++;
            }
        }
        if (innerRotateRight==4){
            innerRotateRight=0;
            innerHoriFlip=true;
            for (int i=0; i<4; i++){
                if (Arrays.equals(innerGraph[0],new int[]{2,1})){
                    break;
                }else {
                    int[][] tempGraph = new int[2][2];
                    tempGraph[0][1] = innerGraph[0][0];
                    tempGraph[1][1] = innerGraph[0][1];
                    tempGraph[0][0] = innerGraph[1][0];
                    tempGraph[1][0] = innerGraph[1][1];
                    innerGraph = tempGraph;
                    innerRotateRight++;
                }
            }
        }
        if (!innerHoriFlip){
            if (innerRotateRight%2==1){
                innerRotateRight += 2;
            }
        }



        int[][] inner1 = new int[n/2][m/2];
        for (int i=0; i<n/2; i++){
            for (int j=0; j<m/2; j++){
                inner1[i][j] = graph[i][j];
            }
        }
        int[][] inner2 = new int[n/2][m/2];
        for (int i=0; i<n/2; i++){
            for (int j=0; j<m/2; j++){
                inner2[i][j] = graph[i][j+m/2];
            }
        }
        int[][] inner3 = new int[n/2][m/2];
        for (int i=0; i<n/2; i++){
            for (int j=0; j<m/2; j++){
                inner3[i][j] = graph[i+n/2][j+m/2];
            }
        }
        int[][] inner4 = new int[n/2][m/2];
        for (int i=0; i<n/2; i++){
            for (int j=0; j<m/2; j++){
                inner4[i][j] = graph[i+n/2][j];
            }
        }
        for (int i=0; i<innerRotateRight; i++){
            inner1 = rotateInner(inner1);
            inner2 = rotateInner(inner2);
            inner3 = rotateInner(inner3);
            inner4 = rotateInner(inner4);
        }

        if (innerHoriFlip){
            inner1 = hFlip(inner1);
            inner2 = hFlip(inner2);
            inner3 = hFlip(inner3);
            inner4 = hFlip(inner4);
        }

        int[][] resGraph;
        if (innerRotateRight%2==0){
            resGraph = new int[n][m];
        }else{
            resGraph = new int[m][n];
            int temp = n;
            n = m;
            m = temp;
        }

        for (int i=0; i<2; i++){
            for (int j=0; j<2; j++){
                if (outerGraph[i][j] == 1){
                    for (int k=0; k<n/2; k++){
                        for (int l=0; l<m/2; l++){
                            resGraph[k+(i*n/2)][l+(j*m/2)] = inner1[k][l];
                        }
                    }
                }else if (outerGraph[i][j] == 2){
                    for (int k=0; k<n/2; k++){
                        for (int l=0; l<m/2; l++){
                            resGraph[k+(i*n/2)][l+(j*m/2)] = inner2[k][l];
                        }
                    }
                }else if (outerGraph[i][j] == 3){
                    for (int k=0; k<n/2; k++){
                        for (int l=0; l<m/2; l++){
                            resGraph[k+(i*n/2)][l+(j*m/2)] = inner3[k][l];
                        }
                    }
                }else if (outerGraph[i][j] == 4){
                    for (int k=0; k<n/2; k++){
                        for (int l=0; l<m/2; l++){
                            resGraph[k+(i*n/2)][l+(j*m/2)] = inner4[k][l];
                        }
                    }
                }
            }
        }

        for (int[] g : resGraph){
            for (int n : g){
                sb.append(n).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);


    }
    public static int[][] innerOrd1(){
        int[][] tempGraph = new int[2][2];
        tempGraph[1][0] = innerGraph[0][0];
        tempGraph[1][1] = innerGraph[0][1];
        tempGraph[0][0] = innerGraph[1][0];
        tempGraph[0][1] = innerGraph[1][1];
        return tempGraph;
    }
    public static int[][] outerOrd1(){
        int[][] tempGraph = new int[2][2];
        tempGraph[1][0] = outerGraph[0][0];
        tempGraph[1][1] = outerGraph[0][1];
        tempGraph[0][0] = outerGraph[1][0];
        tempGraph[0][1] = outerGraph[1][1];
        return tempGraph;
    }
    public static int[][] innerOrd2(){
        int[][] tempGraph = new int[2][2];
        tempGraph[0][1] = innerGraph[0][0];
        tempGraph[0][0] = innerGraph[0][1];
        tempGraph[1][1] = innerGraph[1][0];
        tempGraph[1][0] = innerGraph[1][1];
        return tempGraph;
    }
    public static int[][] outerOrd2(){
        int[][] tempGraph = new int[2][2];
        tempGraph[0][1] = outerGraph[0][0];
        tempGraph[0][0] = outerGraph[0][1];
        tempGraph[1][1] = outerGraph[1][0];
        tempGraph[1][0] = outerGraph[1][1];
        return tempGraph;
    }
    public static int[][] innerOrd3(){
        int[][] tempGraph = new int[2][2];
        tempGraph[0][1] = innerGraph[0][0];
        tempGraph[1][1] = innerGraph[0][1];
        tempGraph[0][0] = innerGraph[1][0];
        tempGraph[1][0] = innerGraph[1][1];
        return tempGraph;
    }
    public static int[][] outerOrd3(){
        int[][] tempGraph = new int[2][2];
        tempGraph[0][1] = outerGraph[0][0];
        tempGraph[1][1] = outerGraph[0][1];
        tempGraph[0][0] = outerGraph[1][0];
        tempGraph[1][0] = outerGraph[1][1];
        return tempGraph;
    }
    public static int[][] innerOrd4(){
        int[][] tempGraph = new int[2][2];
        tempGraph[1][0] = innerGraph[0][0];
        tempGraph[0][0] = innerGraph[0][1];
        tempGraph[1][1] = innerGraph[1][0];
        tempGraph[0][1] = innerGraph[1][1];
        return tempGraph;
    }
    public static int[][] outerOrd4(){
        int[][] tempGraph = new int[2][2];
        tempGraph[1][0] = outerGraph[0][0];
        tempGraph[0][0] = outerGraph[0][1];
        tempGraph[1][1] = outerGraph[1][0];
        tempGraph[0][1] = outerGraph[1][1];
        return tempGraph;
    }
    public static int[][] outerOrd5(){
        int[][] tempGraph = new int[2][2];
        tempGraph[0][1] = outerGraph[0][0];
        tempGraph[1][1] = outerGraph[0][1];
        tempGraph[0][0] = outerGraph[1][0];
        tempGraph[1][0] = outerGraph[1][1];
        return tempGraph;
    }
    public static int[][] outerOrd6(){
        int[][] tempGraph = new int[2][2];
        tempGraph[1][0] = outerGraph[0][0];
        tempGraph[0][0] = outerGraph[0][1];
        tempGraph[1][1] = outerGraph[1][0];
        tempGraph[0][1] = outerGraph[1][1];
        return tempGraph;
    }
    public static int[][] rotateInner(int[][] graph){
        int width = graph[0].length;
        int height = graph.length;
        int[][] newGraph = new int[width][height];
        for (int i=0; i<width; i++){
            for (int j=0; j<height; j++){
                newGraph[i][j] = graph[height-1-j][i];
            }
        }
        return newGraph;
    }
    public static int[][] hFlip(int[][] graph){
        int width = graph[0].length;
        int height = graph.length;
        int[][] newGraph = new int[height][width];
        for (int i=0; i<height; i++){
            for (int j=0; j<width; j++){
                newGraph[i][j] = graph[i][width-1-j];
            }
        }
        return newGraph;
    }
//    public static int[][] vFlip(int[][] graph){
//        int width = graph[0].length;
//        int height = graph.length;
//        int[][] newGraph = new int[height][width];
//        for (int i=0; i<height; i++){
//            for (int j=0; j<width; j++){
//                newGraph[height-1-i][j] = graph[i][j];
//            }
//        }
//        return newGraph;
//    }
}