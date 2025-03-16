import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    
    static int N;
    static Map<Integer,Integer> map;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        map = new HashMap<>();
        map.put(1,1);
        map.put(12,2);
        map.put(123,3);
        map.put(1234,4);
        map.put(12345,5);
        map.put(123456,6);
        map.put(1234567,7);
        map.put(12345678,8);
        map.put(123456789,9);
        System.out.println(map.getOrDefault(N,-1));
    }
}