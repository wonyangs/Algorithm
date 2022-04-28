import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        if (a == b && b == c) {
            System.out.println(10000 + a * 1000);
        } else if (a == b || b == c || c == a) {
            if (a == b || b == c) {
                System.out.println(1000 + b * 100);
            } else {
                System.out.println(1000 + c * 100);
            }
        } else {
            System.out.println(max(a, b, c) * 100);
        }
    }

    private static int max(int a, int b, int c) {
        if (a >= b && a >= c) {
            return a;
        } else if (b >= a && b >= c) {
            return b;
        }
        return c;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}