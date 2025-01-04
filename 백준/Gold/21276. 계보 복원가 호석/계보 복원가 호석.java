import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());

        token = new StringTokenizer(input.readLine());
        String[] people = new String[N];
        for (int i = 0; i < N; i++) {
            people[i] = token.nextToken();
        }
        Arrays.sort(people);

        Map<String, Integer> nameToIndex = new HashMap<>();
        for (int i = 0; i < N; i++) {
            nameToIndex.put(people[i], i+1);
        }

        List<Integer>[] graph = new ArrayList[N+1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }
        int[] inDegree = new int[N+1];

        int M = Integer.parseInt(input.readLine());
        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(input.readLine());
            String to = token.nextToken();
            String from = token.nextToken();
            int toIndex = nameToIndex.get(to);
            int fromIndex = nameToIndex.get(from);
            graph[fromIndex].add(toIndex);
            inDegree[toIndex]++;
        }

        List<Integer> roots = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            if (inDegree[i] == 0) {
                roots.add(i);
            }
        }

        sb.append(roots.size()).append("\n");
        List<String> rootNames = new ArrayList<>();
        for (int root : roots) {
            rootNames.add(people[root-1]);
        }
        for (String rootName : rootNames) {
            sb.append(rootName).append(" ");
        }
        sb.append("\n");

        List<Integer>[] children = new ArrayList[N+1];
        for (int i = 0; i <= N; i++) {
            children[i] = new ArrayList<>();
        }

        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            if (inDegree[i] == 0) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int current = queue.poll();
            for (int child : graph[current]) {
                if (inDegree[child] == 1) {
                    children[current].add(child);
                }
                inDegree[child]--;
                if (inDegree[child] == 0) {
                    queue.add(child);
                }
            }
        }

        for (String name : people) {
            int index = nameToIndex.get(name);
            List<Integer> childList = children[index];
            Collections.sort(childList);
            sb.append(name).append(" ").append(childList.size());
            for (int child : childList) {
                sb.append(" ").append(people[child-1]);
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}