import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];

        double res = 0.0;
        
        for (int i = 0; i < N; ++i) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int max = Arrays.stream(arr).max().getAsInt();

        for (int n : arr) {
            res += (double)n/max * 100;
        }
        System.out.println(res/N);

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}