import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder output = new StringBuilder();
	private static StringTokenizer tokens;
	
	static int T;
	static Member[] members;
	static String str;
	
	
	public static void main(String[] args) throws IOException {
		T = Integer.parseInt(input.readLine());
		members = new Member[T];
		for(int n=0; n<T; n++) {
			tokens = new StringTokenizer(input.readLine());
			members[n] = new Member(n, Integer.parseInt(tokens.nextToken()),tokens.nextToken());
		}
		
		Arrays.sort(members);
		
		for (int t=0; t<T; t++) {
			Member member = members[t];
			System.out.println(member.age+" "+member.name);
		}
	}
	
	static class Member implements Comparable<Member>{
		int order, age;
		String name;
		
		public Member(int order, int age, String name) {
			this.order = order;
			this.age = age;
			this.name = name;
		}

		@Override
		public int compareTo(Member o) {
			if(this.age==o.age) {
				return Integer.compare(this.order,  o.order);
			}else {
				return Integer.compare(this.age, o.age);
			}
		}
	}
}