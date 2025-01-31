import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        Set<Integer> set = new HashSet<>();
        StringTokenizer token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            set.add(Integer.parseInt(token.nextToken()));
        }
        Object[] lst = set.toArray();
        Arrays.sort(lst);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < lst.length; i++) {
            sb.append(lst[i].toString()).append("\n");
        }
        System.out.println(sb);
    }
}