package File;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class BufferReader {
    public static void main(String[] args) {
        try (BufferedWriter read = new BufferedWriter(new FileWriter("Helloworld.txt", true))) {
            read.write("\nYes this is all facts");
            System.out.println("Succesfull Write");
        } catch (IOException e) {
            System.out.println("An Error Occur To A File");
        }
    }
}