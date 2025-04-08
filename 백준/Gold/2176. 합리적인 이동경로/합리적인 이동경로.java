import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int numNodes, numEdges;
    static ArrayList<Edge>[] graph;
    static int[] minCost;

    static class Edge implements Comparable<Edge> {
        int destination;
        int weight;

        public Edge(int destination, int weight) {
            this.destination = destination;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge other) {
            return this.weight - other.weight;
        }
    }

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        numNodes = Integer.parseInt(token.nextToken());
        numEdges = Integer.parseInt(token.nextToken());

        graph = new ArrayList[numNodes + 1];
        for (int i = 1; i <= numNodes; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < numEdges; i++) {
            token = new StringTokenizer(input.readLine());
            int start = Integer.parseInt(token.nextToken());
            int destination = Integer.parseInt(token.nextToken());
            int cost = Integer.parseInt(token.nextToken());
            graph[start].add(new Edge(destination, cost));
            graph[destination].add(new Edge(start, cost));
        }

        minCost = new int[numNodes + 1];
        Arrays.fill(minCost, Integer.MAX_VALUE);
        minCost[2] = 0;

        int[] dp = new int[numNodes + 1];
        dp[2] = 1;

        PriorityQueue<Edge> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(new Edge(2, 0));

        while (!priorityQueue.isEmpty()) {
            Edge currentEdge = priorityQueue.poll();
            int currentNode = currentEdge.destination;
            
            if (minCost[currentNode] < currentEdge.weight) {
                continue;
            }

            for (Edge neighbor : graph[currentNode]) {
                int newCost = minCost[currentNode] + neighbor.weight;

                if (minCost[neighbor.destination] > newCost) {
                    minCost[neighbor.destination] = newCost;
                    priorityQueue.add(new Edge(neighbor.destination, newCost));
                }
                if (minCost[neighbor.destination] > minCost[currentNode]) {
                    dp[neighbor.destination] += dp[currentNode];
                }
            }
        }
        System.out.println(dp[1]);
    }
}