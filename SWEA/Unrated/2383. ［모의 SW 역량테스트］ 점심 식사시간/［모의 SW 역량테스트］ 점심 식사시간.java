import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int n, T;
    static int[][] graph;
    static List<int[]> personIdx;
    static List<int[]> stairsInfo;
    static int minTime;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(input.readLine());
            graph = new int[n][n];
            personIdx = new ArrayList<>();
            stairsInfo = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                token = new StringTokenizer(input.readLine());
                for (int j = 0; j < n; j++) {
                    int temp = Integer.parseInt(token.nextToken());
                    graph[i][j] = temp;
                    if (temp == 1) {
                        personIdx.add(new int[]{i, j});
                    } else if (temp >= 2) {
                        stairsInfo.add(new int[]{i, j, temp});
                    }
                }
            }

            minTime = Integer.MAX_VALUE;
            subset(0, new boolean[personIdx.size()]);
            sb.append("#").append(t).append(" ").append(minTime).append("\n");
        }
        System.out.println(sb);
    }

    public static void subset(int cnt, boolean[] visited) {
        if (cnt == personIdx.size()) {
            List<Integer> firstStairUserTime = new ArrayList<>();
            List<Integer> secondStairUserTime = new ArrayList<>();

            for (int i = 0; i < personIdx.size(); i++) {
                int[] person = personIdx.get(i);
                if (visited[i]) {
                    int dist = Math.abs(person[0] - stairsInfo.get(0)[0])
                            + Math.abs(person[1] - stairsInfo.get(0)[1]);
                    firstStairUserTime.add(dist + 1); // 도착 후 1분 후에 계단 이용 시작
                } else {
                    int dist = Math.abs(person[0] - stairsInfo.get(1)[0])
                            + Math.abs(person[1] - stairsInfo.get(1)[1]);
                    secondStairUserTime.add(dist + 1);
                }
            }

            Collections.sort(firstStairUserTime);
            Collections.sort(secondStairUserTime);

            int time1 = calculateTime(firstStairUserTime, stairsInfo.get(0)[2]);
            int time2 = calculateTime(secondStairUserTime, stairsInfo.get(1)[2]);

            minTime = Math.min(minTime, Math.max(time1, time2));

            return;
        }
        visited[cnt] = true;
        subset(cnt + 1, visited);
        visited[cnt] = false;
        subset(cnt + 1, visited);
    }

    public static int calculateTime(List<Integer> userTimes, int stairLength) {
        PriorityQueue<Integer> stairQueue = new PriorityQueue<>();
        int currentTime = 0;

        for (int userTime : userTimes) {
            // 계단에 3명이 있는 경우, 가장 먼저 계단을 내려간 사람의 시간을 꺼내서 갱신
            if (stairQueue.size() >= 3) {
                currentTime = stairQueue.poll();
            }

            // 새로운 사용자의 시작 시간은 현재 시간과 도착 시간 중 큰 값
            currentTime = Math.max(currentTime, userTime);

            // 계단을 내려가는 시간을 계산하여 큐에 추가
            stairQueue.add(currentTime + stairLength);
        }

        // 마지막 사람이 계단을 다 내려간 시간
        while (!stairQueue.isEmpty()) {
            currentTime = stairQueue.poll();
        }

        return currentTime;
    }
}