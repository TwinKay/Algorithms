import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(tokens.nextToken());
        int m = Integer.parseInt(tokens.nextToken());
        int redX = -1;
        int redY = -1;
        int blueX = -1;
        int blueY = -1;
        char[][] graph = new char[n][m];
        for (int i=0; i<n; i++){
            String temp = input.readLine();
            for (int j=0; j<m; j++){
                char a = temp.charAt(j);
                if (a=='R'){
                    redX = j;
                    redY = i;
                    a = '.';
                }
                if (a=='B'){
                    blueX = j;
                    blueY = i;
                    a = '.';
                }
                graph[i][j] = a;
            }
        }
        // visited에는 red blue idx로 기록
        Deque<int[]> deq = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        deq.add(new int[]{redX,redY,blueX,blueY,0});
        visited.add(redX + "," + redY + "," + blueX + "," + blueY);

        int res = -1;
        while (!deq.isEmpty()){

            char[][] newGraph;
            int[] temp = deq.pop();

            // 좌표는 각 case에서 초기화 필요
            int rX;
            int rY;
            int bX;
            int bY;
            int cnt = temp[4];

            if (cnt > 9){
                break;
            }

            // 오른쪽
            // 오른쪽에 위치한 거 먼저
            // 그 다음 것은 먼 저 간 것도 고려
            rX = temp[0];
            rY = temp[1];
            bX = temp[2];
            bY = temp[3];
            boolean rFlag = false; boolean bFlag = false;
            newGraph = new char[n][m];
            for (int i = 0; i < n; i++) {
                newGraph[i] = Arrays.copyOf(graph[i], m); // 깊은 복사
            }
            // r이 오른쪽에 위치할 때
            if (rX >= bX){
                // r 이동
                while (true) {
                    if (newGraph[rY][rX+1] == '#'){
                        break;
                    } else if (newGraph[rY][rX+1] == 'O'){
                        rFlag = true;
                        break;
                    } else if (newGraph[rY][rX+1] == '.'){
                        rX += 1;
                    }
                }
                if (!rFlag){
                    newGraph[rY][rX]='R';
                }
                // b 이동
                while (true) {
                    if (newGraph[bY][bX+1] == '#' || newGraph[bY][bX+1] == 'R'){
                        break;
                    } else if (newGraph[bY][bX+1] == 'O'){
                        bFlag = true;
                        break;
                    } else if (newGraph[bY][bX+1] == '.'){
                        bX += 1;
                    }
                }
            } else { // b가 오른쪽 위치
                // b 이동
                while (true) {
                    if (newGraph[bY][bX+1] == '#'){
                        break;
                    } else if (newGraph[bY][bX+1] == 'O'){
                        bFlag = true;
                        break;
                    } else if (newGraph[bY][bX+1] == '.'){
                        bX += 1;
                    }
                }
                if (!bFlag){
                    newGraph[bY][bX]='B';
                }
                // r 이동
                while (true) {
                    if (newGraph[rY][rX+1] == '#' || newGraph[rY][rX+1] == 'B'){
                        break;
                    } else if (newGraph[rY][rX+1] == 'O'){
                        rFlag = true;
                        break;
                    } else if (newGraph[rY][rX+1] == '.'){
                        rX += 1;
                    }
                }
            }
            if (rFlag && !bFlag){
                res = cnt+1;
                break;
            } else if (!rFlag && !bFlag){
                String vstTest = rX+","+rY+","+bX+","+bY;
                if (!visited.contains(vstTest)){
                    deq.add(new int[]{rX,rY,bX,bY,cnt+1});
                    visited.add(vstTest);
                }
            }

            // 왼쪽
            // 왼에 위치한 거 먼저
            // 그 다음 것은 먼저 간 것도 고려
            rX = temp[0];
            rY = temp[1];
            bX = temp[2];
            bY = temp[3];
            rFlag = false; bFlag = false;
            newGraph = new char[n][m];
            for (int i = 0; i < n; i++) {
                newGraph[i] = Arrays.copyOf(graph[i], m); // 깊은 복사
            }
            // r이 왼에 위치할 때
            if (rX <= bX){
                // r 이동
                while (true) {
                    if (newGraph[rY][rX-1] == '#'){
                        break;
                    } else if (newGraph[rY][rX-1] == 'O'){
                        rFlag = true;
                        break;
                    } else if (newGraph[rY][rX-1] == '.'){
                        rX -= 1;
                    }
                }
                if (!rFlag){
                    newGraph[rY][rX]='R';
                }
                // b 이동
                while (true) {
                    if (newGraph[bY][bX-1] == '#' || newGraph[bY][bX-1] == 'R'){
                        break;
                    } else if (newGraph[bY][bX-1] == 'O'){
                        bFlag = true;
                        break;
                    } else if (newGraph[bY][bX-1] == '.'){
                        bX -= 1;
                    }
                }
            } else { // b가 왼쪽 위치
                // b 이동
                while (true) {
                    if (newGraph[bY][bX-1] == '#'){
                        break;
                    } else if (newGraph[bY][bX-1] == 'O'){
                        bFlag = true;
                        break;
                    } else if (newGraph[bY][bX-1] == '.'){
                        bX -= 1;
                    }
                }
                if (!bFlag){
                    newGraph[bY][bX]='B';
                }
                // r 이동
                while (true) {
                    if (newGraph[rY][rX-1] == '#' || newGraph[rY][rX-1] == 'B'){
                        break;
                    } else if (newGraph[rY][rX-1] == 'O'){
                        rFlag = true;
                        break;
                    } else if (newGraph[rY][rX-1] == '.'){
                        rX -= 1;
                    }
                }
            }
            if (rFlag && !bFlag){
                res = cnt+1;
                break;
            } else if (!rFlag && !bFlag){
                String vstTest = rX+","+rY+","+bX+","+bY;
                if (!visited.contains(vstTest)){
                    deq.add(new int[]{rX,rY,bX,bY,cnt+1});
                    visited.add(vstTest);
                }
            }

            // 위
            // 위에 위치한 거 먼저
            // 그 다음 것은 먼저 간 것도 고려
            rX = temp[0];
            rY = temp[1];
            bX = temp[2];
            bY = temp[3];
            rFlag = false; bFlag = false;
            newGraph = new char[n][m];
            for (int i = 0; i < n; i++) {
                newGraph[i] = Arrays.copyOf(graph[i], m); // 깊은 복사
            }
            // r이 위에 위치할 때
            if (rY >= bY){
                // r 이동
                while (true) {
                    if (newGraph[rY+1][rX] == '#'){
                        break;
                    } else if (newGraph[rY+1][rX] == 'O'){
                        rFlag = true;
                        break;
                    } else if (newGraph[rY+1][rX] == '.'){
                        rY += 1;
                    }
                }
                if (!rFlag){
                    newGraph[rY][rX]='R';
                }
                // b 이동
                while (true) {
                    if (newGraph[bY+1][bX] == '#' || newGraph[bY+1][bX] == 'R'){
                        break;
                    } else if (newGraph[bY+1][bX] == 'O'){
                        bFlag = true;
                        break;
                    } else if (newGraph[bY+1][bX] == '.'){
                        bY += 1;
                    }
                }
            } else { // b가 위에 위치
                // b 이동
                while (true) {
                    if (newGraph[bY+1][bX] == '#'){
                        break;
                    } else if (newGraph[bY+1][bX] == 'O'){
                        bFlag = true;
                        break;
                    } else if (newGraph[bY+1][bX] == '.'){
                        bY += 1;
                    }
                }
                if (!bFlag){
                    newGraph[bY][bX]='B';
                }
                // r 이동
                while (true) {
                    if (newGraph[rY+1][rX] == '#' || newGraph[rY+1][rX] == 'B'){
                        break;
                    } else if (newGraph[rY+1][rX] == 'O'){
                        rFlag = true;
                        break;
                    } else if (newGraph[rY+1][rX] == '.'){
                        rY += 1;
                    }
                }
            }
            if (rFlag && !bFlag){
                res = cnt+1;
                break;
            } else if (!rFlag && !bFlag){
                String vstTest = rX+","+rY+","+bX+","+bY;
                if (!visited.contains(vstTest)){
                    deq.add(new int[]{rX,rY,bX,bY,cnt+1});
                    visited.add(vstTest);
                }
            }

            // 아래
            // 아래에 위치한 거 먼저
            // 그 다음 것은 먼저 간 것도 고려
            rX = temp[0];
            rY = temp[1];
            bX = temp[2];
            bY = temp[3];
            rFlag = false; bFlag = false;
            newGraph = new char[n][m];
            for (int i = 0; i < n; i++) {
                newGraph[i] = Arrays.copyOf(graph[i], m); // 깊은 복사
            }
            // r이 아래에 위치할 때
            if (rY <= bY){
                // r 이동
                while (true) {
                    if (newGraph[rY-1][rX] == '#'){
                        break;
                    } else if (newGraph[rY-1][rX] == 'O'){
                        rFlag = true;
                        break;
                    } else if (newGraph[rY-1][rX] == '.'){
                        rY -= 1;
                    }
                }
                if (!rFlag){
                    newGraph[rY][rX]='R';
                }
                // b 이동
                while (true) {
                    if (newGraph[bY-1][bX] == '#' || newGraph[bY-1][bX] == 'R'){
                        break;
                    } else if (newGraph[bY-1][bX] == 'O'){
                        bFlag = true;
                        break;
                    } else if (newGraph[bY-1][bX] == '.'){
                        bY -= 1;
                    }
                }
            } else { // b가 아래에 위치
                // b 이동
                while (true) {
                    if (newGraph[bY-1][bX] == '#'){
                        break;
                    } else if (newGraph[bY-1][bX] == 'O'){
                        bFlag = true;
                        break;
                    } else if (newGraph[bY-1][bX] == '.'){
                        bY -= 1;
                    }
                }
                if (!bFlag){
                    newGraph[bY][bX]='B';
                }
                // r 이동
                while (true) {
                    if (newGraph[rY-1][rX] == '#' || newGraph[rY-1][rX] == 'B'){
                        break;
                    } else if (newGraph[rY-1][rX] == 'O'){
                        rFlag = true;
                        break;
                    } else if (newGraph[rY-1][rX] == '.'){
                        rY -= 1;
                    }
                }
            }
            if (rFlag && !bFlag){
                res = cnt+1;
                break;
            } else if (!rFlag && !bFlag){
                String vstTest = rX+","+rY+","+bX+","+bY;
                if (!visited.contains(vstTest)){
                    deq.add(new int[]{rX,rY,bX,bY,cnt+1});
                    visited.add(vstTest);
                }
            }
        }
        System.out.println(res);
    }
}