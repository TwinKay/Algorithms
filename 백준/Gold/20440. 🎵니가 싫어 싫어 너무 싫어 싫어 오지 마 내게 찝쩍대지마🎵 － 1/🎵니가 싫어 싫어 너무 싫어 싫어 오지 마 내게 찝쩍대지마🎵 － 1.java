import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    static Map<Integer,Integer> map;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        map = new HashMap<>();
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            int start = Integer.parseInt(token.nextToken());
            int end = Integer.parseInt(token.nextToken());
            map.put(start, map.getOrDefault(start, 0)+1);
            map.put(end, map.getOrDefault(end, 0)-1);
        }
        int[][] info = new int[map.size()][2];
        Object[] keys = map.keySet().toArray();
        for (int i = 0; i < info.length; i++) {
            info[i][0] = (int) keys[i];
            info[i][1] = map.get(info[i][0]);
        }

        Arrays.sort(info, (o1,o2) ->{
            return o1[0]-o2[0];
        });
        int[] imos = new int[info.length];
        imos[0] = info[0][1];
        int max = imos[0];
        for (int i = 1; i < info.length; i++) {
            imos[i] = imos[i-1] + info[i][1];
            max = Math.max(max, imos[i]);
        }
        int resStart = -1;
        int resEnd = -1;
        for (int i = 0; i < imos.length; i++) {
            if(imos[i]==max){
                if(resStart==-1){
                    resStart = i;
                }
            }else{
                if(resStart!=-1){
                    resEnd = i;
                    break;
                }
            }
        }
        sb.append(max).append("\n");
        sb.append(info[resStart][0]).append(" ").append(info[resEnd][0]);
        System.out.println(sb);
    }
}