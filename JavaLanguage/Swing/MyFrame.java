package Swing;
import java.awt.Color;
import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class MyFrame extends Practice1Frame{
    
    MyFrame() {
        JFrame window_frame = new JFrame();
        window_frame.setTitle("Frame");
        window_frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window_frame.setResizable(false);
        window_frame.setSize(500, 500);
        window_frame.setVisible(true);

        ImageIcon image = new ImageIcon("Sigma.png");
        window_frame.setIconImage(image.getImage());
        window_frame.getContentPane().setBackground(new Color(0x131826));
    }
}
