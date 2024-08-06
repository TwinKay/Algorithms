import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());
        int[][] graph = new int[n][n];

        int idxSharkX = 0;
        int idxSharkY = 0;
        int size = 2;
        int ateFish = 0;
        int res = 0;

        for (int i=0; i<n; i++){
            tokens = new StringTokenizer(input.readLine());
            for (int j=0; j<n; j++){
                int temp = Integer.parseInt(tokens.nextToken());
                graph[i][j] = temp;
                // 아기상어 위치 저장
                if (temp==9){
                    idxSharkX = j;
                    idxSharkY = i;
                }
            }
        }
        boolean flag = false; // 더이상 먹을 것이 없을 때

        int[] deltaX = {0,0,-1,1};
        int[] deltaY = {1,-1,0,0};

        // 없을 때 까지 계속 (flag)
        while (flag==false){

            // 진화
            if (ateFish == size){
                ateFish = 0;
                size ++;
            }

            // 첫 시작
            Queue que = new LinkedList();
            int[] firstNode = {idxSharkX, idxSharkY, 0};
            que.add(firstNode);
            graph[idxSharkY][idxSharkX] = 0;

            // visited
            boolean[][] visited = new boolean[n][n];
            visited[idxSharkY][idxSharkX] = true;

            // 동일 거리 후보
            List<int[]> cand = new ArrayList<>();
            int cnt = 0;

            while (que.isEmpty()!= true) {
                int[] item = (int[]) que.poll();
                int x = item[0];
                int y = item[1];
                cnt = item[2];
                for (int i=0; i<4; i++){
                    if (x+deltaX[i]>=0 && x+deltaX[i]<n && y+deltaY[i]>=0 && y+deltaY[i]<n && graph[y+deltaY[i]][x+deltaX[i]]<=size && visited[y+deltaY[i]][x+deltaX[i]]==false){
                        if (graph[y+deltaY[i]][x+deltaX[i]]>0 && graph[y+deltaY[i]][x+deltaX[i]]<size){
                            // 먹을 수 있는 경우
                            if (cand.isEmpty()==true){
                                int[] temp = {x+deltaX[i],y+deltaY[i],cnt+1};
                                que.add(temp);
                                cand.add(temp);
                                visited[y+deltaY[i]][x+deltaX[i]] = true;
                            } else{
                                int[] temp = (int[]) cand.get(0);
                                if (temp[2]==cnt+1){
                                    int[] temp2 = {x+deltaX[i],y+deltaY[i],cnt+1};
                                    que.add(temp2);
//                                    System.out.println(cand.size());
                                    cand.add(temp2);
                                    visited[y+deltaY[i]][x+deltaX[i]] = true;
                                }else{
//                                    que.clear(); // 할 필요가 있나..?
//                                    break;
                                    int[] temp2 = {x+deltaX[i],y+deltaY[i],cnt+1};
                                    que.add(temp2);
                                    visited[y+deltaY[i]][x+deltaX[i]] = true;
                                }
                            }
                        } else {
                            int[] temp = {x+deltaX[i], y+deltaY[i], cnt+1};
                            que.add(temp);
                            visited[y+deltaY[i]][x+deltaX[i]] = true;
                        }
                    }
                }
            }
            if (cand.isEmpty()==false){
                Collections.sort(cand, new Comparator<int[]>() {
                    @Override
                    public int compare(int[] o1, int[] o2) {
                        return o1[1]!=o2[1] ? o1[1]-o2[1] : o1[0]-o2[0];
                    }
                });
//                que.clear(); // ?
                ateFish ++;
                graph[cand.get(0)[1]][cand.get(0)[0]] = 0;
//                System.out.println("cnt = " + cnt);
//                cnt ++;

                cnt = cand.get(0)[2];
                res += cnt;
                idxSharkX = cand.get(0)[0];
                idxSharkY = cand.get(0)[1];
            } else{
                flag = true;
            }
        }
        System.out.println(res);
    }
}