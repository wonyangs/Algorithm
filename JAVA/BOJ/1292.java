import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        
        int count = 0, total = 0;
        int sum = 0;
        while (total < B) {
            count++;
            for (int i = 0; i < count; ++i) {
                total++;
                if (total >= A && total <= B) {
                    sum += count;
                }
            }
        }
        System.out.println(sum);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();        
    }
}