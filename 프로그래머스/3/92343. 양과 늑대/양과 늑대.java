import java.util.*;

class Solution {
    static int[] nodeInfo;
    static List<Integer>[] children;
    static int max = 0;
    
    public int solution(int[] info, int[][] edges) {
        nodeInfo = info;
        children = new ArrayList[info.length];
        for (int[] edge : edges) {
            int parent = edge[0];
            int child  = edge[1];
            if (children[parent] == null) {
                children[parent] = new ArrayList<>();
            }
            children[parent].add(child);
        }
        
        List<Integer> availableNodes = new ArrayList<>();
        availableNodes.add(0);
        dfs(0, 0, 0, availableNodes);
        
        return max;
    }
    
    private void dfs(int currentNode, int sheepCount, int wolfCount, List<Integer> availableNodes) {
        if (nodeInfo[currentNode] == 0) sheepCount++;
        else wolfCount++;
        
        if (sheepCount <= wolfCount) return;
        
        max = Math.max(max, sheepCount);
        
        List<Integer> nextNodes = new ArrayList<>(availableNodes);
        nextNodes.remove(Integer.valueOf(currentNode));
        if (children[currentNode] != null) {
            for (int child : children[currentNode]) {
                nextNodes.add(child);
            }
        }
        
        for (int nextNode : nextNodes) {
            dfs(nextNode, sheepCount, wolfCount, nextNodes);
        }
    }
}
