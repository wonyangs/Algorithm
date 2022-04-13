import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
		Integer N = Integer.parseInt(br.readLine());
        
        int[] arr = new int[N];
        boolean[] visited = new boolean[N+1];

        dfs(arr, 0, N, sb, visited);
        bw.write(sb.toString());
        bw.flush();
        br.close();
        bw.close();
    }

    public static void dfs(int[] arr, int depth, int N, StringBuilder sb, boolean[] visited) {
        if (depth == N) {
            print(arr, sb);
            return;
        }

        for (int i = 1; i < N+1; ++i) {
            if (visited[i] == false) {
                visited[i] = true;
                arr[depth] = i;
                dfs(arr, depth+1, N, sb, visited);
                visited[i] = false;
            }
        }
    }

    public static void print(int[] arr, StringBuilder sb) {
        for (int n : arr) {
            sb.append(n).append(' ');
        }
        sb.append("\n");
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();        
    }
}