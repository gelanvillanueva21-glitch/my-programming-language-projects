package DSA;
import java.util.*;

public class Prac17Matrix {

    public static void main(String[] args) {
        Graph graph = new Graph(5);

        graph.addNode(new Node('A'));
        graph.addNode(new Node('B'));
        graph.addNode(new Node('C'));
        graph.addNode(new Node('D'));
        graph.addNode(new Node('E'));

        graph.addEdge(0, 1);
        graph.addEdge(1, 2);
        graph.addEdge(1, 4);
        graph.addEdge(2, 3);
        graph.addEdge(2, 4);
        graph.addEdge(4, 0);
        graph.addEdge(4, 2);


        //graph.print();

        //graph.depthFirstSearch(4);
        graph.breadthFirstSearch(1);

        System.out.println(graph.checkEdge(4, 3));

    }
} class Graph {
    
    ArrayList<Node> nodes;
    int[][] matrix;

    Graph(int size) {
        nodes = new ArrayList<>();
        matrix = new int[size][size];
    }

    public void addNode(Node node) {
        nodes.add(node);
    }

    public void addEdge(int src, int dst) {
        matrix[src][dst] = 1;
    }

    public boolean checkEdge(int src, int dst) {
        
        if (matrix[src][dst] == 1) {
            return true;
        } else {
            return false;
        }
    }

    public void print() {

        System.out.print("  ");
        for(Node node : nodes) {
            System.out.print(node.data + " ");
        }
        System.out.println();

        for (int i = 0; i < matrix.length; i++) {
            System.out.print(nodes.get(i).data + " ");
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
        System.out.println();
        }
    }

    public void depthFirstSearch(int src) {

        boolean[] visited = new boolean[matrix.length];
        dFSHelper(src, visited);

    }

    public void dFSHelper(int src, boolean[] visited) {

        if(visited[src]) {
            return;
        } else {
            visited[src] = true;
            System.out.println(nodes.get(src).data + " = Visited");
        }

        for (int i = 0; i < matrix.length; i++) {
            if (matrix[src][i] == 1) {
                dFSHelper(i, visited);
            }
        }
        return;
    }

    public void breadthFirstSearch(int src) {

        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[matrix.length];

        queue.add(src);
        visited[src] = true;

        while (queue.size() != 0) {
            
            src = queue.poll();
            System.out.println(nodes.get(src).data + " = Visited");

            for (int index = 0; index < matrix.length; index++) {
                if (matrix[src][index] == 1 && !visited[index]) {
                    queue.add(index);
                    visited[index] = true;
                }
            }
        }
    }
} class Node {

    char data;
    boolean visited;

    Node(char data) {
        this.data = data;
    }
}