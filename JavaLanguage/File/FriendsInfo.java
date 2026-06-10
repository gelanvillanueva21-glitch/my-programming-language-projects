package File;

import java.io.*;
import java.util.*;

public class FriendsInfo {
    static String choice;
    static Scanner sc = new Scanner(System.in);
    static String Filename = "FriendsInfo.bin";
    static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException, InterruptedException {
        
        do {
                System.out.flush();
                System.out.println("\n\n1. Enter Friends Info\n2. Friends List\n3. Exit");
                System.out.print("Enter: ");
                choice = sc.nextLine();
                
                switch (choice) {
                    case "1":
                        enterFriendsInfo(Filename);
                        break;
                    case "2":
                        friendsList(Filename);
                        break;
                    case "3":
                        System.out.println("Exited The Program");
                        System.out.println("God Bless You.");
                        break;
                    default:
                        System.out.println("Wrong Input");
                }

        } while(!choice.equals("3"));

    }
    static void friendsList(String Filename) throws IOException, InterruptedException {

        String name, birthdate;
        int weight, height;

        try (DataInputStream input_data = new DataInputStream(new FileInputStream(Filename))) {

            System.out.flush();
            System.out.println("ALL MY FRINED LIST HERE");
            System.out.println("Record  Name Of My Friends     Date Of Birth        Height   Weight");
            int recount = 0;
            
                while (input_data.available() > 0) {
                    name = input_data.readUTF();
                    birthdate = input_data.readUTF();
                    weight = input_data.readInt();
                    height = input_data.readInt();
                    System.out.printf("\n%3d.  %-25s %-18s  %3d     %3d",++recount, name, birthdate, weight, height);
                }

                System.out.println("\n");
                System.out.print("Press Enter To Return To The Menu.....");
                sc.nextLine();
                System.out.println("\n\n");

        } catch (IOException e) {
            System.out.println("An Error Occur In File");
        }

    }
    static void enterFriendsInfo(String Filename) throws IOException, InterruptedException {

        String name, birthdate, add_more;
        int weight, height;

        try (DataOutputStream output_data = new DataOutputStream(new FileOutputStream(Filename, true))) {
            do {
                System.out.flush();
                System.out.println("\n\n");
                System.out.print("Enter His/Her Name: ");
                name = sc.nextLine();
                System.out.print("Enter His/Her Birthdate: ");
                birthdate = sc.nextLine();
                System.out.print("Enter His/Her Weight[lbs]: ");
                weight = sc.nextInt();
                System.out.print("Enter His/Her Height[cm]: ");
                height = sc.nextInt();
                sc.nextLine();

                    output_data.writeUTF(name);
                    output_data.writeUTF(birthdate);
                    output_data.writeInt(weight);
                    output_data.writeInt(height);

                    System.out.print("Want Another Friends Info?[Y][N]: ");
                    add_more = sc.next().toLowerCase();
                    sc.nextLine();
            } while(add_more.equals("y"));
            
            System.out.println("\n");
            System.out.print("Press Enter To Return To The Menu.....");
            sc.nextLine();
            System.out.println("\n\n");

        } catch(IOException e) {
            System.out.println("An Error Occur In File");
        }

    }
}