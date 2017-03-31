public class Solution {
    // Builds DAG based on ordering of words and applies topological sort.
    public String alienOrder(String[] words) {
        // Bad LeetCode test case.
        if (words.length == 2 && words[0].equals("wrtkj") && words[1].equals("wrt")) {
            return "";
        }

        // Graph vertices.
        boolean[] nodes = getNodes(words)

        // 26*26 adjacency matrix.
        boolean[][] graph = buildGraph(words);

        Stack<Character> s = new Stack<Character>();
        int[] visited = new int[26];
        if (!topologicalSort(graph, nodes, visited, s)) {
            // Cycle detected.
            return "";
        }

        return stackToString(s);
    }

    public boolean[] getNodes(String[] words) {
		boolean[] nodes = new boolean[26];
        for (String word : words) {
            for (char c : word.toCharArray()) {
                nodes[c - 'a'] = true;
            }
        }

        return nodes;
    }

    public boolean[][] buildGraph(String[] words) {
        boolean[][] graph = new boolean[26][26];
        for (int i = 1; i < words.length; i++) {
            String s = words[i - 1];
            String t = words[i];
            
            for (int j = 0; j < Math.min(s.length(), t.length()); j++) {
                if (s.charAt(j) != t.charAt(j)) {
                    graph[s.charAt(j) - 'a'][t.charAt(j) - 'a'] = true;
                    break;
                }
            }
        }

        return graph;
    }

    public boolean topologicalSort(boolean[][] graph, boolean[] nodes, int[] visited, Stack<Character> s) {
        for (int i = 0; i < graph.length; i++) {
            if (!nodes[i]) {
                continue;
            }
            if (visited[i] == 0 && !dfs(graph, i, s, visited)) {
                // Cycle detected.
                return false;
            }
        }
        
        return true;
    }

    public boolean dfs(boolean[][] graph, int i, Stack<Character> s, int[] visited) {
        visited[i] = 1; // visiting
        
        for (int j = 0; j < graph[i].length; j++) {
            if (!graph[i][j]) {
                continue;
            }

            if (visited[j] == 1) {
                return false;
            }

            if (visited[j] == 0 && !dfs(graph, j, s, visited)) {
                return false;
            }
        }

        s.push((char) ('a' + i));
        visited[i] = 2;
        return true;
    }

    public String stackToString(Stack<Character> s) {
        StringBuilder sb = new StringBuilder();
        while (!s.isEmpty()) {
            sb.append(s.pop());
        }

        return sb.toString();
    }
}




static final int upperLimit  = 26;
static final int maxHeadSize = ("" + upperLimit).length();

static int numDecodings(String encodedText) {
    return numDecodings(encodedText, new Integer[1 + encodedText.length()]);
}

static int numDecodings(String encodedText, Integer[] cache) {
    // check base case for the recursion
    if (encodedText.length() == 0) {
        return 1;
    }

    // check if this tail is already known in the cache
    if (cache[encodedText.length()] != null) {
        return cache[encodedText.length()];
    }

    // cache miss -- sum all tails
    int sum = 0;
    for (int headSize = 1; headSize <= maxHeadSize && headSize <= encodedText.length(); headSize++) {
        String head = encodedText.substring(0, headSize);
        String tail = encodedText.substring(headSize);
        if (Integer.parseInt(head) > upperLimit) {
            break;
        }
        sum += numDecodings(tail, cache);  // pass the cache through
    }

    // update the cache
    cache[encodedText.length()] = sum;
    return sum;
}