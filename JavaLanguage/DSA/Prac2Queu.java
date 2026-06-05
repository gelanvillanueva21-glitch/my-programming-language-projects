package DSA;

import java.util.LinkedList;
import java.util.Queue;

public class Prac2Queu {
    public static void main(String[] args) {
        Queue<String> namQueue = new LinkedList<String>();

        namQueue.offer("Gelan");
        namQueue.offer("Arron");
        namQueue.offer("Arnie");
        namQueue.offer("Dean");
        namQueue.offer("Neo");

        namQueue.poll();
        System.out.println(namQueue);
        //System.out.println(namQueue.isEmpty());
        //System.out.println(namQueue.size());
        
        if (namQueue.contains("Neo") == true) {
            System.out.println("Yes!");
        } else {
            System.out.println("No!");
        }
        /*
        Queue<String> queue = new LinkedList<>();
        queue.add("Alice");    // joins the back
        queue.add("Bob");
        queue.add("Charlie");

        queue.peek();          // Alice — just look at front
        queue.poll();          // Alice — removed from front (served first!)
        queue.poll();          // Bob
        queue.poll();          // Charlie
        */
    }
}
