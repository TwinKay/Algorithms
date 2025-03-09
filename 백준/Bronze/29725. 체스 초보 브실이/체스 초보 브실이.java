import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException {
        Map<Character,Integer> map = new HashMap<>();
        map.put('.',0);
        map.put('K',0);
        map.put('k',0);
        map.put('P',1);
        map.put('p',-1);
        map.put('N',3);
        map.put('n',-3);
        map.put('B',3);
        map.put('b',-3);
        map.put('R',5);
        map.put('r',-5);
        map.put('Q',9);
        map.put('q',-9);

        int res = 0;
        for (int i = 0; i < 8; i++) {
            String s = input.readLine();
            for (char c : s.toCharArray()) {
                res += map.get(c);
            }
        }
        System.out.println(res);
    }
}