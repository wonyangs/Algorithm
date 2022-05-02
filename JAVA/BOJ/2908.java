import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = reverse(Integer.parseInt(st.nextToken()));
        int b = reverse(Integer.parseInt(st.nextToken()));

        System.out.println(a>b ? a : b);
    }

    public static int reverse(int n) {
        int res = 0;
        for (int i = 0; i < 3; ++i) {
            res *= 10;
            res += n % 10;
            n /= 10;
        }
        return res;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}