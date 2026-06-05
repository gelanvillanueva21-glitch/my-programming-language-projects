package DSA;
import java.util.*;

public class Prac1Stacks {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<String>();

        stack.push("Gelan");
        stack.push("Chanzine");
        stack.push("Arron");
        stack.push("Neo");
        stack.push("Arnie");
        stack.push("Myra");
        stack.push("Dean");

        System.out.println(stack.peek()); //peek is to peek the last value
        System.out.println(stack.search("Gelan")); //search is to find and returning an int
        System.out.println(stack.pop()); //pop is to delete the last value
        System.out.println(stack);

        /*
        Stack<Integer> stack = new Stack<>();
        stack.push(10);   // add 10 → bottom
        stack.push(20);   // add 20 → middle
        stack.push(30);   // add 30 → top

        stack.peek();     // 30 — just look, don't remove
        stack.pop();      // 30 — removes from top
        stack.pop();      // 20
        stack.pop();      // 10
// */
    }
}