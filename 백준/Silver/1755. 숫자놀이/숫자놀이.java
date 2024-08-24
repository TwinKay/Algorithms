import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer token;
	static StringBuilder sb = new StringBuilder();
	static String[] numToStr = {"zero","one","two","three","four","five",
								"six","seven","eight","nine"};
	static String[][] resArr;
	

	public static void main(String[] args) throws IOException {
		token = new StringTokenizer(input.readLine());
		int m = Integer.parseInt(token.nextToken());
		int n = Integer.parseInt(token.nextToken());
		
		resArr = new String[n-m+1][2];
		for (int i=m; i<=n; i++) {
			if (i<10) {
				resArr[i-m][0] = numToStr[i];
				resArr[i-m][1] = String.valueOf(i);
			} else {
				resArr[i-m][0] = numToStr[i/10]+numToStr[i%10];
				resArr[i-m][1] = String.valueOf(i);
			}
		}
		
		Arrays.sort(resArr, (a, b) -> a[0].compareTo(b[0]));
		
		int cnt = 0;
		for (int i=0; i<n-m+1; i++) {
			sb.append(resArr[i][1]).append(" ");
			cnt ++;
			if (cnt == 10) {
				System.out.println(sb);
				
				cnt = 0;
				sb.setLength(0);
				continue;
			}
		}
		System.out.println(sb);
	}
}