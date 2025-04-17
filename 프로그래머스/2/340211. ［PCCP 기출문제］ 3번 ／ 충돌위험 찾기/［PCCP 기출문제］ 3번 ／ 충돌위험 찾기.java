import java.util.*;

public class Solution {
    public int solution(int[][] points, int[][] routes) {
        int numRobots = routes.length;            // 로봇 수
        int pathLength = routes[0].length;        // 각 로봇의 경로 길이
        int numPoints = points.length;            // 총 포인트 수

        // 1-indexed로 포인트 좌표 저장
        int[] pointRow = new int[numPoints + 1];
        int[] pointCol = new int[numPoints + 1];
        for (int i = 0; i < numPoints; i++) {
            pointRow[i + 1] = points[i][0];
            pointCol[i + 1] = points[i][1];
        }

        // 로봇별 시간에 따른 위치 이력 저장
        List<List<int[]>> robotPositions = new ArrayList<>();
        for (int robotIdx = 0; robotIdx < numRobots; robotIdx++) {
            List<int[]> positionHistory = new ArrayList<>();

            // 시작 위치
            int currentRow = pointRow[routes[robotIdx][0]];
            int currentCol = pointCol[routes[robotIdx][0]];
            positionHistory.add(new int[]{currentRow, currentCol});

            // 각 구간마다 한 칸씩 이동 (행 먼저, 이후 열 이동)
            for (int step = 1; step < pathLength; step++) {
                int nextPoint = routes[robotIdx][step];
                int targetRow = pointRow[nextPoint];
                int targetCol = pointCol[nextPoint];

                while (currentRow != targetRow || currentCol != targetCol) {
                    if (currentRow != targetRow) {
                        currentRow += (targetRow > currentRow ? 1 : -1);
                    } else {
                        currentCol += (targetCol > currentCol ? 1 : -1);
                    }
                    positionHistory.add(new int[]{currentRow, currentCol});
                }
            }

            robotPositions.add(positionHistory);
        }

        // 전체 시뮬레이션 시간(최대 스텝) 계산
        int maxTimeStep = 0;
        for (List<int[]> history : robotPositions) {
            maxTimeStep = Math.max(maxTimeStep, history.size() - 1);
        }

        int dangerCount = 0;
        // 시간 0부터 maxTimeStep까지 순회
        for (int time = 0; time <= maxTimeStep; time++) {
            Map<String, Integer> occupancyMap = new HashMap<>();

            // 각 로봇의 위치 카운트
            for (int robotIdx = 0; robotIdx < numRobots; robotIdx++) {
                List<int[]> history = robotPositions.get(robotIdx);
                if (time < history.size()) {
                    int[] pos = history.get(time);
                    String positionKey = pos[0] + "," + pos[1];
                    occupancyMap.put(positionKey, occupancyMap.getOrDefault(positionKey, 0) + 1);
                }
            }

            // 같은 좌표에 2대 이상 있으면 위험 횟수 증가
            for (int count : occupancyMap.values()) {
                if (count >= 2) {
                    dangerCount++;
                }
            }
        }

        return dangerCount;
    }
}
