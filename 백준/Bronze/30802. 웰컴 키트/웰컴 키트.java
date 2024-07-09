import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.valueOf(br.readLine());
		
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		int a = Integer.valueOf(st1.nextToken());
		int b = Integer.valueOf(st1.nextToken());
		int c = Integer.valueOf(st1.nextToken());
		int d = Integer.valueOf(st1.nextToken());
		int e = Integer.valueOf(st1.nextToken());
		int f = Integer.valueOf(st1.nextToken());
		
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		int shirt = Integer.valueOf(st2.nextToken());
		int pen = Integer.valueOf(st2.nextToken());
		
		int res1 = 0;
		
		if (a%shirt == 0) {
			res1 += a/shirt;
		} else {
			res1 += a/shirt +1;
		}
		if (b%shirt == 0) {
			res1 += b/shirt;
		} else {
			res1 += b/shirt +1;
		}
		if (c%shirt == 0) {
			res1 += c/shirt;
		} else {
			res1 += c/shirt +1;
		}
		if (d%shirt == 0) {
			res1 += d/shirt;
		} else {
			res1 += d/shirt +1;
		}
		if (e%shirt == 0) {
			res1 += e/shirt;
		} else {
			res1 += e/shirt +1;
		}
		if (f%shirt == 0) {
			res1 += f/shirt;
		} else {
			res1 += f/shirt +1;
		}

		System.out.println(res1);
		
		System.out.println(num/pen + " " + num%pen);

	}

}