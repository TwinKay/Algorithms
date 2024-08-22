import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
 
public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();
 
    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            token = new StringTokenizer(input.readLine());
            int n = Integer.parseInt(token.nextToken());;
            String s = token.nextToken();
 
            int[][] graph = new int[n][n];
            for (int i = 0; i < n; i++) {
                token = new StringTokenizer(input.readLine());
                for (int j = 0; j < n; j++) {
                    graph[i][j] = Integer.parseInt(token.nextToken());
                }
            }
 
            if (s.equals("up")){
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
            } else if (s.equals("down")){
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
            } else if (s.equals("left")){
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
            }else if (s.equals("right")){
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
            sb.append("#").append(t).append("\n");
            for (int[] temp : graph){
                for (int i : temp){
                    sb.append(i).append(" ");
                }
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }
}