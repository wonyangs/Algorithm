import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int count = 0;

        boolean[] prime = new boolean[N+1];
        Arrays.fill(prime, true);

        for (int i = 2; i <= N; ++i) {
            if (prime[i] == true) {
                int t = 1;
                while (i*t <= N) {
                    if (prime[i*t] == true) {
                        prime[i*t] = false;
                        count++;
                        if (count == K) {
                            System.out.println(i*t);
                            return;
                        }
                    }
                    t++;
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();        
    }
}