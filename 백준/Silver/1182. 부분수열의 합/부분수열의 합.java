import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer token;
	
	static int n;
	static int s;
	static int[] arr;
	static int res = 0;

	public static void main(String[] args) throws IOException{
		token = new StringTokenizer(input.readLine());
		n = Integer.parseInt(token.nextToken());
		s = Integer.parseInt(token.nextToken());
		
		token = new StringTokenizer(input.readLine());
		arr = new int[n];
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(token.nextToken());
		}
		
		subset(0, new boolean[n]);
		System.out.println(res);
	}
	
	public static void subset (int cnt, boolean[] isSelected) {
		if (cnt==n) {
			
			if (!Arrays.equals(isSelected, new boolean[n])) {
				int sum = 0;
				for (int i=0; i<n; i++) {
					if (isSelected[i]) {
						sum += arr[i];
					}
				}
				if (sum==s) {
					res ++;
				}
			}
			return;
		}
		isSelected[cnt] = true;
		subset(cnt+1,isSelected);
		isSelected[cnt] = false;
		subset(cnt+1,isSelected);
	}
}