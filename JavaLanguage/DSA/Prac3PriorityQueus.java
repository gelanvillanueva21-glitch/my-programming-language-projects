package DSA;

import java.util.*;

public class Prac3PriorityQueus {
    public static void main(String[] args) {
        
        Queue<String> queue = new PriorityQueue<>(Collections.reverseOrder());

        queue.offer("Gelan");
        queue.add("Alias");
        queue.add("Chanzine");
        queue.offer("Arron");
        queue.offer("Neo");
        queue.offer("Arnie");

        while (!queue.isEmpty()) {
            System.out.println(queue.poll());
        }
        /*
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(5);   // minor
        pq.add(1);   // critical
        pq.add(3);   // moderate

        pq.poll();   // 1 — smallest = highest priority, served FIRST
        pq.poll();   // 3
        pq.poll();   // 5 — served LAST
        */
    }
}
