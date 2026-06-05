package Swing;
import javax.swing.*;
import java.awt.*;
import javax.swing.border.*;

public class Practice2Label {
    public static void main(String[] args) {
        JFrame window = new JFrame();
        JLabel label = new JLabel();
        ImageIcon image = new ImageIcon("C:/Users/user/OneDrive/Desktop/Java.Language/images.jpg");
        Border border = BorderFactory.createLineBorder(Color.green, 3);

        //Labels
        label.setText("I AM STEVE");
        label.setIcon(image);
        label.setHorizontalTextPosition(JLabel.CENTER);
        label.setVerticalTextPosition(JLabel.TOP);
        label.setForeground(new Color(0x81bdcb));
        label.setFont(new Font("MV Boli", Font.BOLD, 20));
        label.setIconTextGap(20);
        label.setBackground(Color.BLACK);
        label.setOpaque(true);
        label.setBorder(border);
        label.setVerticalAlignment(JLabel.CENTER);
        label.setHorizontalAlignment(JLabel.CENTER);
        //label.setBounds(125, 100, 250, 250);


        //Frame Window
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //window.setSize(500, 500);
        //window.setLayout(null);
        window.add(label);
        window.setVisible(true);
        window.pack();
    }
}
