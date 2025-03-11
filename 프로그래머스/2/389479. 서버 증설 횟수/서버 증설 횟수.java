import java.util.*;
class Solution {
    public int solution(int[] players, int m, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1,o2) -> o1[0] - o2[0]);
        int serverNum = 0; int cnt = 0; 
        
        for(int i = 0; i < 24; i++){
            while(!pq.isEmpty() && pq.peek()[0] == i){
                serverNum -= pq.poll()[1];
            }
            
            int plusNum = players[i] / m - serverNum; 
            if(plusNum >= 0){
                serverNum  += plusNum;
                cnt += plusNum;
                pq.add(new int []{i+k, plusNum});
            }
        }
        return cnt;
    }
}