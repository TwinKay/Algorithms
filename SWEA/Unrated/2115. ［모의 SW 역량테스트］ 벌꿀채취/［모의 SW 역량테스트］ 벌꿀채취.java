import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static List<boolean[]> subsetCase;
    static int n,m,c,T;
    static List<Integer> arr;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            token = new StringTokenizer(input.readLine());
            n = Integer.parseInt(token.nextToken());
            m = Integer.parseInt(token.nextToken());
            c = Integer.parseInt(token.nextToken());

            arr = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                token = new StringTokenizer(input.readLine());
                for (int j = 0; j < n; j++) {
                    arr.add(Integer.parseInt(token.nextToken()));
                }
                arr.add(-1);
            }

            boolean[] visited = new boolean[arr.size()];
            List<Integer> profits = new ArrayList<>();
            List<List<Integer>> visits = new ArrayList<>();

            subsetCase = new ArrayList<>();
            generateSubset(0, new boolean[m]);

            flag:
            for (int i = 0; i < arr.size() - m; i++) {
                if (arr.get(i) == -1) continue;

                List<Integer> tempVisited = new ArrayList<>();
                for (int j = 0; j < m; j++) {
                    if (arr.get(i + j) == -1) continue flag;
                    tempVisited.add(i + j);
                }

                for (boolean[] subset : subsetCase) {
                    int totalHoney = 0;
                    int eachProfit = 0;
                    boolean valid = true;

                    for (int k = 0; k < m; k++) {
                        if (subset[k]) {
                            int honeyAmount = arr.get(i + k);
                            if (honeyAmount == -1) {
                                valid = false;
                                break;
                            }
                            totalHoney += honeyAmount;
                            eachProfit += honeyAmount * honeyAmount;
                        }
                    }

                    if (valid && totalHoney <= c) {
                        profits.add(eachProfit);
                        visits.add(new ArrayList<>(tempVisited));
                    }
                }
            }

            for (int i = 0; i < visits.size(); i++) {
                visits.get(i).add(0, profits.get(i));
            }

            Collections.sort(visits, (o1, o2) -> (int) o2.get(0) - (int) o1.get(0));

            int res = 0;
            res += visits.get(0).get(0);
            for (int i = 1; i < visits.get(0).size(); i++) {
                visited[visits.get(0).get(i)] = true;
            }

            flag:
            for (List<Integer> v : visits) {
                for (int i = 1; i < v.size(); i++) {
                    if (visited[v.get(i)]) continue flag;
                }
                res += v.get(0);
                break;
            }

            sb.append("#").append(t).append(" ").append(res).append("\n");
        }
        System.out.println(sb);
    }

    public static void generateSubset(int cnt, boolean[] selected) {
        if (cnt == m) {
            subsetCase.add(selected.clone());
            return;
        }
        selected[cnt] = true;
        generateSubset(cnt + 1, selected);
        selected[cnt] = false;
        generateSubset(cnt + 1, selected);
    }
}