import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer token;

	public static void main(String[] args) throws IOException {
		token = new StringTokenizer(input.readLine());
		int n = Integer.parseInt(token.nextToken());
		int x = Integer.parseInt(token.nextToken());
		int k = Integer.parseInt(token.nextToken());
		x--;

		boolean[] arr = new boolean[n];
		arr[x] = true;

		for (int i=0; i<k; i++) {
			token = new StringTokenizer(input.readLine());
			int a = Integer.parseInt(token.nextToken());
			int b = Integer.parseInt(token.nextToken());
			a--; b--;

			boolean temp = arr[a];
			arr[a] = arr[b];
			arr[b] = temp;
		}
		for (int i=0; i<n; i++) {
			if (arr[i]) {
				System.out.println(i+1);
				break;
			}
		}
	}
}
