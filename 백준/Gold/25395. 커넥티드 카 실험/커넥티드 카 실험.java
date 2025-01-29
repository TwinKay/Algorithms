import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();
    static int N,S;
    static boolean[] visited;
    static class Car{
        int location;
        int fuel;
        int idx;

        Car(int location, int fuel, int idx){
            this.location = location;
            this.fuel = fuel;
            this.idx = idx;
        }
    }

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        S = Integer.parseInt(token.nextToken())-1;
        int[] locArr = new int[N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            locArr[i] = Integer.parseInt(token.nextToken());
        }
        int[] fuelArr = new int[N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            fuelArr[i] = Integer.parseInt(token.nextToken());
        }
        Car[] cars = new Car[N];
        for (int i = 0; i < N; i++) {
            cars[i] = new Car(locArr[i], fuelArr[i], i);
        }
        Arrays.sort(cars, (o1,o2)->{
            return o1.location-o2.location;
        });
        visited = new boolean[N];

        Deque<Car> deq = new ArrayDeque<>();
        deq.addLast(cars[S]);
        visited[S] = true;
        while(!deq.isEmpty()){
            Car cur = deq.pollFirst();
            for (int i = cur.idx-1; i >= 0; i--) {
                if (cur.location-cars[i].location > cur.fuel){
                    break;
                }
                if (!visited[i]){
                    visited[cars[i].idx] = true;
                    deq.addLast(cars[i]);
                }
            }

            for (int i = cur.idx+1; i < N; i++) {
                if (cars[i].location-cur.location > cur.fuel){
                    break;
                }
                if (!visited[i]){
                    visited[cars[i].idx] = true;
                    deq.addLast(cars[i]);
                }
            }
        }
        for (int i = 0; i < N; i++) {
            if (visited[i]){
                sb.append(i+1).append(" ");
            }
        }
        System.out.println(sb);
    }
}