import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int n;

    static int[] arr = {1,2,3,4};
    static int r = 5;
    static List<int[]> permList = new ArrayList<int[]>();

    public static int[][] move(int[][] graph, int m){
        if (m==1){
            for (int i = 0; i < n; i++){
                List<Integer> arr = new ArrayList<>();
                for (int j = 0; j < n; j++){
                    if (graph[j][i]!=0){
                        arr.add(graph[j][i]);
                    }
                }
                List<Integer> afterArr = new ArrayList<>();
                boolean flag = false;
                for (int k = 0; k < arr.size(); k++){
                    if (k==arr.size()-1 && !flag){
                        afterArr.add(arr.get(k));
                        break;
                    } else if (k == arr.size()-1 && flag){
                        break;
                    }

                    if (flag) {
                        flag = false;
                    } else{
                        if (arr.get(k).equals(arr.get(k+1))){
                            afterArr.add(arr.get(k)*2);
                            flag = true;
                        } else {
                            afterArr.add(arr.get(k));
                        }
                    }
                }
                for (int j = 0; j < afterArr.size(); j++){
                    graph[j][i] = afterArr.get(j);
                }
                for (int j=afterArr.size(); j<n; j++){
                    graph[j][i] = 0;
                }
            }
        } else if (m==2){
            for (int i = 0; i < n; i++){
                List<Integer> arr = new ArrayList<>();
                for (int j = n-1; j >= 0; j--){
                    if (graph[j][i]!=0){
                        arr.add(graph[j][i]);
                    }
                }
                List<Integer> afterArr = new ArrayList<>();
                boolean flag = false;
                for (int k = 0; k < arr.size(); k++){
                    if (k==arr.size()-1 && !flag){
                        afterArr.add(arr.get(k));
                        break;
                    } else if (k == arr.size()-1 && flag){
                        break;
                    }

                    if (flag) {
                        flag = false;
                    } else{
                        if (arr.get(k).equals(arr.get(k+1))){
                            afterArr.add(arr.get(k)*2);
                            flag = true;
                        } else {
                            afterArr.add(arr.get(k));
                        }
                    }
                }
                int cnt = 0;
                for (int j = n-1; j > n-1-afterArr.size(); j--){
                    graph[j][i] = afterArr.get(cnt);
                    cnt ++;
                }
                for (int j=n-1-afterArr.size(); j>=0; j--){
                    graph[j][i] = 0;
                }
            }
        } else if (m==3){
            for (int i = 0; i < n; i++){
                List<Integer> arr = new ArrayList<>();
                for (int j = 0; j < n; j++){
                    if (graph[i][j]!=0){
                        arr.add(graph[i][j]);
                    }
                }
                List<Integer> afterArr = new ArrayList<>();
                boolean flag = false;
                for (int k = 0; k < arr.size(); k++){
                    if (k==arr.size()-1 && !flag){
                        afterArr.add(arr.get(k));
                        break;
                    } else if (k == arr.size()-1 && flag){
                        break;
                    }

                    if (flag) {
                        flag = false;
                    } else{
                        if (arr.get(k).equals(arr.get(k+1))){
                            afterArr.add(arr.get(k)*2);
                            flag = true;
                        } else {
                            afterArr.add(arr.get(k));
                        }
                    }
                }
                for (int j = 0; j < afterArr.size(); j++){
                    graph[i][j] = afterArr.get(j);
                }
                for (int j=afterArr.size(); j<n; j++){
                    graph[i][j] = 0;
                }
            }
        }else if (m==4){
            for (int i = 0; i < n; i++){
                List<Integer> arr = new ArrayList<>();
                for (int j = n-1; j >= 0; j--){
                    if (graph[i][j]!=0){
                        arr.add(graph[i][j]);
                    }
                }
                List<Integer> afterArr = new ArrayList<>();
                boolean flag = false;
                for (int k = 0; k < arr.size(); k++){
                    if (k==arr.size()-1 && !flag){
                        afterArr.add(arr.get(k));
                        break;
                    } else if (k == arr.size()-1 && flag){
                        break;
                    }

                    if (flag) {
                        flag = false;
                    } else{
                        if (arr.get(k).equals(arr.get(k+1))){
                            afterArr.add(arr.get(k)*2);
                            flag = true;
                        } else {
                            afterArr.add(arr.get(k));
                        }
                    }
                }
                int cnt = 0;
                for (int j = n-1; j > n-1-afterArr.size(); j--){
                    graph[i][j] = afterArr.get(cnt);
                    cnt ++;
                }
                for (int j=n-1-afterArr.size(); j>=0; j--){
                    graph[i][j] = 0;
                }
            }
        }
        return graph;
    }
    public static void Perm(int cnt, int[] save){
        if (cnt==r){
            permList.add(save.clone());
            return;
        }
        for (int i = 0; i < arr.length; i++){
            save[cnt] = arr[i];
            Perm(cnt+1, save);
        }
    }

    public static void main(String[] args) throws IOException {
         n = Integer.parseInt(input.readLine());

        int[][] graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        Perm(0,new int[r]);

        int max = Integer.MIN_VALUE;
        for (int[] perm : permList){
            int[][] tempGraph = new int[n][n];
            for (int i = 0; i < n; i++) {
                tempGraph[i] = graph[i].clone();
            }


            for (int m : perm){
                move(tempGraph, m);
            }

            for (int[] temp : tempGraph){
                for (int t : temp){
                    max = Math.max(max, t);
                }
            }
        }
        System.out.println(max);
    }
}