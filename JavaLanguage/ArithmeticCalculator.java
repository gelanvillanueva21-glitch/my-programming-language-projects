import javax.swing.*;
import javax.swing.border.*;
import java.awt.*;

public class ArithmeticCalculator extends JFrame {

    private JTextField firstNumberField;
    private JTextField secondNumberField;
    private JTextField sumField;
    private JTextField differenceField;
    private JTextField productField;
    private JTextField floatQuotientField;
    private JTextField intQuotientField;
    private JTextField remainderField;

    private static final Color ORANGE_BG      = new Color(0xE8783A);
    private static final Color INPUT_PINK     = new Color(0xFFCCCC);
    private static final Color OUTPUT_YELLOW  = new Color(0xEEF0B0);
    private static final Color LABEL_DARK     = new Color(0x3A1A00);
    private static final Font  LABEL_FONT     = new Font("Serif", Font.BOLD, 13);
    private static final Font  FIELD_FONT     = new Font("SansSerif", Font.PLAIN, 13);

    public ArithmeticCalculator() {
        setTitle("kdshdfsdfsdf");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);

        JPanel mainPanel = new JPanel(new GridBagLayout());
        mainPanel.setBackground(ORANGE_BG);
        mainPanel.setBorder(new EmptyBorder(20, 20, 20, 20));

        GridBagConstraints gc = new GridBagConstraints();
        gc.insets = new Insets(5, 8, 5, 8);
        gc.fill = GridBagConstraints.HORIZONTAL;

        // ── Input fields ──────────────────────────────────────────────
        firstNumberField  = makeInputField(INPUT_PINK);
        secondNumberField = makeInputField(INPUT_PINK);

        addRow(mainPanel, gc, 0, "First Number",  firstNumberField);
        addRow(mainPanel, gc, 1, "Second Number", secondNumberField);

        // ── Output fields ─────────────────────────────────────────────
        sumField          = makeOutputField();
        differenceField   = makeOutputField();
        productField      = makeOutputField();
        floatQuotientField= makeOutputField();
        intQuotientField  = makeOutputField();
        remainderField    = makeOutputField();

        addRow(mainPanel, gc, 2, "Sum",                    sumField);
        addRow(mainPanel, gc, 3, "Difference",             differenceField);
        addRow(mainPanel, gc, 4, "Product",                productField);
        addRow(mainPanel, gc, 5, "Floating-Point Quotient",floatQuotientField);
        addRow(mainPanel, gc, 6, "Integer Quotient",       intQuotientField);
        addRow(mainPanel, gc, 7, "Remainder",              remainderField);

        // ── Buttons ───────────────────────────────────────────────────
        JButton computeBtn = makeButton("Compute", new Color(0xF5F0E8), LABEL_DARK, false);
        JButton clearBtn   = makeButton("Clear",   new Color(0xD4E8A0), new Color(0x386000), false);
        JButton quitBtn    = makeButton("Quit",    new Color(0xF5F0E8), LABEL_DARK, true);

        computeBtn.addActionListener(e -> compute());
        clearBtn.addActionListener(e -> clearAll());
        quitBtn.addActionListener(e -> {
            int choice = JOptionPane.showConfirmDialog(
                    this, "Are you sure you want to quit?", "Confirm Quit",
                    JOptionPane.YES_NO_OPTION);
            if (choice == JOptionPane.YES_OPTION) System.exit(0);
        });

        JPanel btnPanel = new JPanel(new FlowLayout(FlowLayout.LEFT, 10, 0));
        btnPanel.setBackground(ORANGE_BG);
        btnPanel.add(computeBtn);
        btnPanel.add(clearBtn);
        btnPanel.add(quitBtn);

        gc.gridx = 0; gc.gridy = 8; gc.gridwidth = 2;
        gc.insets = new Insets(15, 8, 5, 8);
        mainPanel.add(btnPanel, gc);

        add(mainPanel);
        pack();
        setLocationRelativeTo(null);
    }

    // ── Helpers ───────────────────────────────────────────────────────────────

    private void addRow(JPanel panel, GridBagConstraints gc,
                        int row, String labelText, JTextField field) {
        JLabel label = new JLabel(labelText.toUpperCase());
        label.setFont(LABEL_FONT);
        label.setForeground(LABEL_DARK);

        gc.gridx = 0; gc.gridy = row; gc.gridwidth = 1;
        gc.anchor = GridBagConstraints.EAST;
        gc.insets = new Insets(5, 8, 5, 4);
        panel.add(label, gc);

        gc.gridx = 1; gc.anchor = GridBagConstraints.WEST;
        gc.insets = new Insets(5, 4, 5, 8);
        gc.ipadx = 80;
        panel.add(field, gc);
        gc.ipadx = 0;
    }

    private JTextField makeInputField(Color bg) {
        JTextField f = new JTextField(12);
        f.setFont(FIELD_FONT);
        f.setBackground(bg);
        f.setHorizontalAlignment(JTextField.RIGHT);
        f.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(0xCC8855), 1),
                BorderFactory.createEmptyBorder(2, 4, 2, 4)));
        return f;
    }

    private JTextField makeOutputField() {
        JTextField f = new JTextField(12);
        f.setFont(FIELD_FONT);
        f.setBackground(OUTPUT_YELLOW);
        f.setEditable(false);
        f.setHorizontalAlignment(JTextField.RIGHT);
        f.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(0xAAAA66), 1),
                BorderFactory.createEmptyBorder(2, 4, 2, 4)));
        return f;
    }

    private JButton makeButton(String text, Color bg, Color fg, boolean bold) {
        JButton b = new JButton(text.toUpperCase());
        b.setFont(new Font("Serif", bold ? Font.BOLD : Font.PLAIN, 13));
        b.setBackground(bg);
        b.setForeground(fg);
        b.setFocusPainted(false);
        b.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(0xAA7744), 1),
                BorderFactory.createEmptyBorder(4, 12, 4, 12)));
        b.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        return b;
    }

    // ── Logic ─────────────────────────────────────────────────────────────────

    private void compute() {
        try {
            double a = Double.parseDouble(firstNumberField.getText().trim());
            double b = Double.parseDouble(secondNumberField.getText().trim());

            sumField.setText(String.format("%.2f", a + b));
            differenceField.setText(String.format("%.2f", a - b));
            productField.setText(String.format("%.2f", a * b));

            if (b == 0) {
                floatQuotientField.setText("Undefined");
                intQuotientField.setText("Undefined");
                remainderField.setText("Undefined");
            } else {
                floatQuotientField.setText(String.format("%.2f", a / b));
                intQuotientField.setText(String.format("%.2f", (double)((long)(a / b))));
                remainderField.setText(String.format("%d", (long)(a % b)));
            }
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this,
                    "Please enter valid numbers in both fields.",
                    "Input Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void clearAll() {
        firstNumberField.setText("");
        secondNumberField.setText("");
        sumField.setText("");
        differenceField.setText("");
        productField.setText("");
        floatQuotientField.setText("");
        intQuotientField.setText("");
        remainderField.setText("");
        firstNumberField.requestFocus();
    }

    // ── Main ──────────────────────────────────────────────────────────────────

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            try {
                UIManager.setLookAndFeel(UIManager.getCrossPlatformLookAndFeelClassName());
            } catch (Exception ignored) {}
            new ArithmeticCalculator().setVisible(true);
        });
    }
}
