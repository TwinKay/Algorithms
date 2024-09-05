import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int T,N,M;
    static int[] arrA, arrB;
    static HashMap<Integer,Integer> mapA;
    static HashMap<Integer,Integer> mapB;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        N = Integer.parseInt(input.readLine());
        arrA = new int[N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            arrA[i] = Integer.parseInt(token.nextToken());
        }
        M = Integer.parseInt(input.readLine());
        arrB = new int[M];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < M; i++) {
            arrB[i] = Integer.parseInt(token.nextToken());
        }
        mapA = new HashMap<>();
        for (int size=1; size <= N; size++) {
            int sum = 0;
            for (int i=0; i<size; i++) {
                sum += arrA[i];
            }
            mapA.put(sum, mapA.getOrDefault(sum, 0) + 1);
            for (int i=0; i<N-size; i++){
                sum -= arrA[i];
                sum += arrA[i+size];

                mapA.put(sum, mapA.getOrDefault(sum, 0) + 1);
            }
        }

        mapB = new HashMap<>();
        for (int size=1; size <= M; size++) {
            int sum = 0;
            for (int i=0; i<size; i++) {
                sum += arrB[i];
            }
            mapB.put(sum, mapB.getOrDefault(sum, 0) + 1);
            for (int i=0; i<M-size; i++){
                sum -= arrB[i];
                sum += arrB[i+size];
                // sum이 특정 넘으면 추가 X (수정 안 함)
                mapB.put(sum, mapB.getOrDefault(sum, 0) + 1);
            }
        }
        int[] keysA = new int[mapA.size()];
        int z = 0;
        for (int key: mapA.keySet()){
            keysA[z] = key;
            z++;
        }
        int[] keysB = new int[mapB.size()];
        z = 0;
        for (int key: mapB.keySet()){
            keysB[z] = key;
            z++;
        }
        long res = 0;
        for (int keyA: mapA.keySet()){
            int keyB = T - keyA;
            if (mapB.containsKey(keyB)) {
                res += (long) mapA.get(keyA) * mapB.get(keyB);
            }
        }

        System.out.println(res);
    }
}