import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        Map<String, Integer> map = new HashMap<>();
        map.put("Poblano",1500);
        map.put("Mirasol",6000);
        map.put("Serrano",15500);
        map.put("Cayenne",40000);
        map.put("Thai",75000);
        map.put("Habanero",125000);

        int total = 0;
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            total += map.getOrDefault(s, 0);
        }
        System.out.println(total);
    }
}