//import java.time.*;
//import java.time.format.*;
//import java.time.format.DateTimeFormatter;
//import java.time.temporal.ChronoUnit;
import java.util.*;
import java.io.*;

public class MyFriends {
    static String choice = "";
    static Scanner prompt = new Scanner(System.in);
    static String fileName = "Sample01.bin";
    static BufferedReader read = new BufferedReader(new InputStreamReader(System.in));

    static void friendsEntry(String filename) throws IOException, InterruptedException {
        // Writing binary data
        String name, birthDate, more;
        int    weight;
        try (DataOutputStream bin = new DataOutputStream(new FileOutputStream(filename, true))) {
            do {
                System.out.flush();
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
                System.out.printf("\nEntry of My Friends\n\n");
                System.out.printf("\nName of Friend : ");
                name = read.readLine();
                System.out.printf("\nDate of Birth  : ");
                birthDate = read.readLine();
                System.out.printf("\nWeight in lbs. : ");
                weight = prompt.nextInt();
                bin.writeUTF(name);
                bin.writeUTF(birthDate);
                bin.writeInt(weight);
                System.out.printf("\nAnother Friend ? [y/n] ");
                more = prompt.nextLine();
            } while (more.toLowerCase().equals("y"));
        } catch (IOException e) {
            System.out.println("Error writing binary file: " + e.getMessage());
        }

        System.out.printf("\n\n\tThis is for Friends Entry");
        System.out.printf("\n\nPress the Enter key to return to the main menu ...");
        read.readLine();
    }

    static void friendsList(String filename) throws IOException, InterruptedException {
        String name, birthDate;
        int    weight;

        // Reading binary data
        try (DataInputStream bin = new DataInputStream(new FileInputStream(filename))) {
            System.out.flush();
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            System.out.println("All My Friends Here on this Side of Heaven\n");
            System.out.println("Record    Name of Friend           Date of Birth          Weight (lbs\n");
            int recCount = 0;
            while (bin.available() > 0) { // loop until the end of file
                name      = bin.readUTF();
                birthDate = bin.readUTF();
                weight    = bin.readInt();
                System.out.printf("\n%3d       %-25s %-18s          %3d", ++recCount, name, birthDate, weight);
            }
        } catch (IOException e) {
            System.out.println("\n\nError reading binary file: " + e.getMessage());
        }

        System.out.printf("\n\n\t\t*** End of File is Reached\n\n");
        System.out.printf("Press the Enter key to return to the main menu ...");
        read.readLine();
        //Thread.sleep(3000); //suspends program execution for 3 seconds.
    }

    public static void main(String args[]) throws IOException, InterruptedException {

        do {
            System.out.flush();
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            System.out.println("My Good Friends Here on Earth\n");
            System.out.printf("\n[ E ] Enter New Friend/s");
            System.out.printf("\n[ L ] List of My Friend/s");
            System.out.printf("\n[ S ] Exit from this Program");
            System.out.printf("n\n\nType Your Choice and Press Enter [E,L,S] ");
            choice = prompt.next().toUpperCase();
            switch (choice) {
                case "E":
                    friendsEntry(fileName); break;
                case "L":
                    friendsList(fileName); break;
                case "S":
                    break;
                default:
                    System.out.printf("\n\tNot a sensible choice ...");
                    Thread.sleep(2000); //suspends program execution for a couple of seconds
            }
            //System.out.print("\n\nTry Another ?[Y|N] ");
            //isaPa = prompt.next();
        } while (!choice.equals("S"));
        System.out.println("\nTill next time.\nMay God bless you...\n");
    }
}