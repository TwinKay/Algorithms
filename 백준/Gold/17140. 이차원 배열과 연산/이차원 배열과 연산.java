import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int R,C,K;
    static List<List<Integer>> graph;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        R = Integer.parseInt(token.nextToken());
        C = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        graph = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            graph.add(new ArrayList<>());
            token = new StringTokenizer(input.readLine());
            graph.get(i).add(Integer.parseInt(token.nextToken()));
            graph.get(i).add(Integer.parseInt(token.nextToken()));
            graph.get(i).add(Integer.parseInt(token.nextToken()));
        }

        int time = 0;
        while (time <= 100){
            if (graph.size()>R-1 && graph.get(0).size()>C-1){
                if (graph.get(R-1).get(C-1)==K) break;
            }
            if (graph.size()>=graph.get(0).size()){
                expand();
            }else{
                rotate();
                expand();
                rotate();
            }
            time++;

        }
        if (time>100){
            System.out.println(-1);
        }else{
            System.out.println(time);
        }
    }
    private static void expand() {
        int rSize = graph.size();
        int maxSize = 0;
        for (int i = 0; i < rSize; i++) {
            List<Integer> currentR = graph.get(i);
            Map<Integer, Integer> hmap = new HashMap<>();
            for (Integer n : currentR) {
                hmap.put(n, hmap.getOrDefault(n, 0) + 1);
            }
            List<int[]> tempList = new ArrayList<>();
            for (int key : hmap.keySet()) {
                if (key!=0){
                    tempList.add(new int[]{key,hmap.get(key)});
                }
            }
            Collections.sort(tempList, (o1, o2) -> {
                if (o1[1]==o2[1]){
                    return o1[0]-o2[0];
                }
                return o1[1]-o2[1];
            });
            List<Integer> newR = new ArrayList<>();
            for (int[] temp : tempList) {
                newR.add(temp[0]);
                newR.add(temp[1]);
            }
            graph.set(i, newR);
            maxSize = Math.max(maxSize,newR.size());
        }
        for (int i = 0; i < graph.size(); i++) {
            int dif = maxSize-graph.get(i).size();
            for (int j = 0; j < dif; j++) {
                graph.get(i).add(0);
            }
        }
    }
    private static void rotate() {
        int rSize = graph.size();
        int cSize = graph.get(0).size();
        List<List<Integer>> rotatedGraph = new ArrayList<>();
        for (int i = 0; i < cSize; i++) {
            rotatedGraph.add(new ArrayList<>());
        }
        for (int i = 0; i < rSize; i++) {
            List<Integer> currentR = graph.get(i);
            for (int j = 0; j < cSize; j++) {
                rotatedGraph.get(j).add(currentR.get(j));
            }
        }
        graph = rotatedGraph;
    }

}