import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());

        HashMap<Character,Integer> map = new HashMap<>();
        for (int i=0; i<n; i++) {
            String s = input.readLine();
            for (int j=0; j<s.length(); j++) {
                char c = s.charAt(j);
                if (map.containsKey(c)) {
                    map.put(c, (int) (map.get(c)+Math.pow(10,s.length()-j-1)));
                } else{
                    map.put(c, (int) Math.pow(10,s.length()-j-1));
                }
            }
        }

        Alpa[] arr = new Alpa[map.size()];
        int l = 0;
        for (char key : map.keySet()) {
            arr[l] = new Alpa(key, map.get(key));
            l++;
        }
        
        Arrays.sort(arr, (a,b)->b.weight - a.weight);

        int res = 0;
        for (int i=0; i<arr.length; i++) {
            res += (9-i)*arr[i].weight;
        }
        System.out.println(res);

    }
    public static class Alpa{
        char c;
        int weight;

        public Alpa(char c, int weight){
            this.c = c;
            this.weight = weight;
        }
    }
}