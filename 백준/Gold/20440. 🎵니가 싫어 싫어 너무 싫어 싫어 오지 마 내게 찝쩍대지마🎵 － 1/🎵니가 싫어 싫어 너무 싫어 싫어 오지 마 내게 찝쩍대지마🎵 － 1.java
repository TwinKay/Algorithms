import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    static Map<Integer, Integer> map;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        map = new TreeMap<>();
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            int start = Integer.parseInt(token.nextToken());
            int end = Integer.parseInt(token.nextToken());
            map.put(start, map.getOrDefault(start, 0) + 1);
            map.put(end, map.getOrDefault(end, 0) - 1);
        }

        int max = 0;
        int imos = 0;
        int resStart = -1;
        int resEnd = -1;
        boolean inMaxRange = false;

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            imos += entry.getValue();
            if (imos > max) {
                max = imos;
                resStart = entry.getKey();
                inMaxRange = true;
            } else if (inMaxRange && imos < max) {
                resEnd = entry.getKey();
                inMaxRange = false;
            }
        }

        sb.append(max).append("\n");
        sb.append(resStart).append(" ").append(resEnd);
        System.out.println(sb);
    }
}