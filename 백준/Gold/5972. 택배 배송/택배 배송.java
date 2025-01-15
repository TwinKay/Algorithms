import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,M;
    static int[] cost;
    static List<List<Node>> graph = new ArrayList<>();

    static class Node {
        int v;
        int cost;

        public Node(int v, int cost) {
            this.v = v;
            this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for(int i = 0; i < M; i++){
            token= new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            int c = Integer.parseInt(token.nextToken());

            graph.get(a).add(new Node(b,c));
            graph.get(b).add(new Node(a,c));
        }

        cost = new int[N+1];
        for (int i = 0; i <= N; i++) {
            cost[i] = Integer.MAX_VALUE;
        }

        dijkstra();
        System.out.println(cost[N]);
    }
    
    static void dijkstra(){
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> {
            return o1.cost - o2.cost;
        });
        pq.add(new Node(1,0));
        cost[1] = 0;
        while (!pq.isEmpty()){
            Node cur = pq.poll();

            for(Node next : graph.get(cur.v)){
                if(cost[next.v] > cost[cur.v]+next.cost){
                    cost[next.v] = cost[cur.v]+next.cost;
                    pq.add(new Node(next.v, cost[next.v]));
                }
            }
        }
    }

}