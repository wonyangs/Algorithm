import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int[] arr = new int[n];
            int hap = 0;
            for (int j = 0; j < n; ++j) {
                arr[j] = Integer.parseInt(st.nextToken());
                hap += arr[j];
            }
            double avg = (double) hap/n;
            int count = 0;
            for (int j = 0; j < n; ++j) {
                if (arr[j] > avg) {
                    count++;
                }
            }
            System.out.printf("%.3f", ((double)count/n*100));
            System.out.println("%");
        }

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}