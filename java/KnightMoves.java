import java.util.*;

public class KnightMoves {

    static class Pair<K, V> {
        private final K key;
        private final V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }

    public static List<List<String>> board() {
        String[] cells = { "a", "b", "c", "d", "e", "f", "g", "h" };
        List<List<String>> board = new ArrayList<>();
        for (int i = 0; i < 8; i++) {
            List<String> row = new ArrayList<>();
            for (String cell : cells) {
                row.add(cell + (i + 1));
            }
            board.add(row);
        }
        return board;
    }

    public static List<String> validMoves(String pos) {
        List<String> moves = new ArrayList<>();
        int col = pos.charAt(0) - 'a';
        int row = Character.getNumericValue(pos.charAt(1)) - 1;
        int[][] deltas = {
                { 2, 1 },
                { 1, 2 },
                { -1, 2 },
                { -2, 1 },
                { -2, -1 },
                { -1, -2 },
                { 1, -2 },
                { 2, -1 }
        };
        for (int[] delta : deltas) {
            int new_row = row + delta[0];
            int new_col = col + delta[1];
            if (new_row >= 0 && new_row < 8 && new_col >= 0 && new_col < 8) {
                moves.add((char) ('a' + new_col) + "" + (new_row + 1));
            }
        }
        return moves;
    }

    public static int knight(String p1, String p2) {
        List<List<String>> board = board();
        Queue<Pair<String, Integer>> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.add(new Pair<>(p1, 0));
        visited.add(p1);

        while (!queue.isEmpty()) {
            Pair<String, Integer> pair = queue.poll();
            String pos = pair.getKey();
            int distance = pair.getValue();
            if (pos.equals(p2)) {
                return distance;
            }
            for (String move : validMoves(pos)) {
                if (!visited.contains(move)) {
                    queue.add(new Pair<>(move, distance + 1));
                    visited.add(move);
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String p1 = "a1";
        String p2 = "b3";
        System.out.println("Minimum number of moves: " + knight(p1, p2));
    }
}
