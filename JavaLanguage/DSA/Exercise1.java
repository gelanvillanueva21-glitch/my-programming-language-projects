package DSA;
import java.util.*;

public class Exercise1 {
    public static void main(String[] args) throws InputMismatchException {
        Queue<String> waiting_line = new LinkedList<String>();
        Stack<String> service_history = new Stack<String>();
        Scanner sc = new Scanner(System.in);

        try {
            System.out.println("Enter #Num Customer To Served");
            System.out.print("> ");
            int costumer_line = sc.nextInt();
            
            for (int i = 0; i < costumer_line; i++) {
                sc.nextLine();
                System.out.print("Enter Name: ");
                String name = sc.nextLine();
                service_history.push(name);
                waiting_line.offer(name);
            }
            boolean alrdy_srv = false;
            while (true) {
            System.out.println("_____TICKET_____\n1. Serve Ticket\n2. Service History\n3. Exit");
            System.out.print("> ");
            int choice = sc.nextInt();

            if (choice == 1) {
                for (int i = 0; i < costumer_line; i++) {
                    System.out.println(waiting_line.poll() + " has been served!");
                }
                alrdy_srv = true;

            } else if (choice == 2) {
                if (alrdy_srv == true) {
                System.out.println("\n_____Served History_____");
                    for (int i = 0; i < costumer_line; i++) {
                        System.out.println(service_history.pop());
                    }
                } else {
                    System.out.println("Haven't Served Anyone Yet");
                }
            } else if (choice == 3) {
                break;
            } else {
                System.out.println("Input Number " + choice + "Not Found");
            }
            }
        } catch (InputMismatchException e) {
            System.out.println("Wrong Input!!");
        }
        sc.close();
    }
}
