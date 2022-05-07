import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        if (b-c >= 0) {
            System.out.println(-1);
            return;
        }
        System.out.println(a / (c-b) + 1);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}