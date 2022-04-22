import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        List<char[]> graph = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            graph.add(br.readLine().toCharArray());
        }

        boolean[][] visited = new boolean[n][m];
        int count = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (visited[i][j] == false) {
                    dfs(i, j, graph, visited, graph.get(i)[j]);
                    count++;
                }
            }
        }
        System.out.println(count);
    }

    public static void dfs(int x, int y, List<char[]> graph, boolean[][] visited, char key) {
        if (x >= graph.size() || y >= graph.get(x).length) {
            return;
        }

        if (graph.get(x)[y] == key) {
            visited[x][y] = true;
            if (key == '-') {
                dfs(x, y+1, graph, visited, key);
            } else {
                dfs(x+1, y, graph, visited, key);
            }
        } 
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}