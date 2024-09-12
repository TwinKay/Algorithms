import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    static int[] timeLine;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        timeLine = new int[1000001];
        for (int i = 1; i <= N; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            timeLine[a] += i;
            timeLine[b] -= i;
        }

        int[] seats = new int[1000001];
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 1; i <= 100000; i++) {
            pq.add(i);
        }
        int[] eachUsingNum = new int[1000001];

        int maxUsing = 0;
        int currentUsing = 0;
        for (int i = 0; i <= 1000000; i++) {
            int userIdx = timeLine[i];
            if (userIdx==0) continue;

            if (userIdx>0){
                currentUsing ++;
                maxUsing = Math.max(maxUsing, currentUsing);

                int comNum = pq.poll();
                seats[userIdx] = comNum;
                eachUsingNum[comNum]++;

            }else{
                currentUsing --;
                int comNum = seats[-userIdx];
                pq.add(comNum);
            }
        }
        sb.append(maxUsing).append("\n");
        for (int i = 1; i <= 1000000; i++) {
            int a = eachUsingNum[i];
            if (a==0) break;
            sb.append(a).append(" ");
        }
        System.out.println(sb);
    }
}