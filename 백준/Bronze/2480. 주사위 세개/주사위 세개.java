import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		int a = Integer.valueOf(st.nextToken());
		int b = Integer.valueOf(st.nextToken());
		int c = Integer.valueOf(st.nextToken());
		
		int res;
		if (a==b && b==c) {
			res = 10000+a*1000;
		} else if (a!=b && b!=c && a!=c) {
			int max = Math.max(a,  Math.max(b, c));
			res = max*100;
		} else {
			if(a==b || a==c) {
				res = 1000+a*100;
			}else {
				res = 1000+b*100;
			}
		}
		
		sb.append(res);
		System.out.println(sb);
	}

}