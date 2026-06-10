package Swing;
// ================================================================
//  SWING CALCULATOR — Step by Step Guide for Beginners
//  Read every comment carefully before moving to the next line!
// ================================================================

// STEP 1: IMPORTS
// These are Java libraries we need for building GUI windows.
// javax.swing.*  = everything related to windows, buttons, text fields
// java.awt.*     = colors, layouts, fonts (older but still used with swing)
// java.awt.event.* = listening for button clicks and keyboard events
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

// ================================================================
// STEP 2: CLASS SETUP
// We implement ActionListener — this means our class can
// LISTEN and REACT to button clicks.
// Think of it like: "hey, tell me whenever a button is clicked"
// ================================================================
public class Calculator implements ActionListener {

    // ================================================================
    // STEP 3: DECLARE YOUR COMPONENTS
    // These are the building blocks of our window.
    // We declare them here so the WHOLE class can use them.
    // ================================================================

    JFrame frame;       // The main window
    JTextField screen;  // The display screen (where numbers appear)

    // These are all the buttons on the calculator
    // We use an array to hold all number/operator buttons
    JButton[] numberButtons = new JButton[10]; // 0 to 9
    JButton addButton, subButton, mulButton, divButton;
    JButton equalButton, clearButton, deleteButton, decimalButton;

    // These variables keep track of the calculator's state
    double num1, num2, result; // The numbers being calculated
    char operator;             // Which operation: +, -, *, /

    // ================================================================
    // STEP 4: CONSTRUCTOR — This runs when we create the calculator
    // This is where we BUILD and SETUP everything
    // ================================================================
    Calculator() {

        // ------------------------------------------------------------
        // STEP 4A: CREATE THE WINDOW (JFrame)
        // JFrame is the actual window that appears on your screen
        // ------------------------------------------------------------
        frame = new JFrame("Calculator");
        frame.setSize(400, 550);                         // Width x Height in pixels
        frame.setLayout(null);                           // We will position everything manually
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Close app when X is clicked
        frame.setResizable(false);                       // Cannot resize the window
        frame.getContentPane().setBackground(new Color(30, 30, 30)); // Dark background

        // ------------------------------------------------------------
        // STEP 4B: CREATE THE SCREEN (JTextField)
        // JTextField is an input/display field — like a text box
        // We use it as our calculator screen
        // ------------------------------------------------------------
        screen = new JTextField();
        screen.setBounds(20, 30, 350, 70);               // x, y, width, height
        screen.setFont(new Font("Arial", Font.BOLD, 30)); // Font style and size
        screen.setHorizontalAlignment(JTextField.RIGHT); // Numbers align to the right
        screen.setEditable(false);                       // User cannot type directly
        screen.setBackground(new Color(20, 20, 20));     // Darker background for screen
        screen.setForeground(Color.WHITE);               // White text
        screen.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10)); // Padding

        // ------------------------------------------------------------
        // STEP 4C: CREATE NUMBER BUTTONS (0-9)
        // We use a loop to create 10 buttons at once
        // Instead of writing button0 = new JButton("0") x10 times
        // ------------------------------------------------------------
        for (int i = 0; i < 10; i++) {
            numberButtons[i] = new JButton(String.valueOf(i)); // Label is the number
            numberButtons[i].setFont(new Font("Arial", Font.BOLD, 20));
            numberButtons[i].setBackground(new Color(50, 50, 50)); // Dark gray
            numberButtons[i].setForeground(Color.WHITE);
            numberButtons[i].setFocusPainted(false);             // Remove ugly focus border
            numberButtons[i].setBorder(BorderFactory.createLineBorder(new Color(70, 70, 70)));
            numberButtons[i].addActionListener(this);            // Listen for clicks!
        }

        // ------------------------------------------------------------
        // STEP 4D: CREATE OPERATOR BUTTONS (+, -, *, /)
        // These are the math operation buttons
        // ------------------------------------------------------------
        addButton     = createOperatorButton("+");
        subButton     = createOperatorButton("-");
        mulButton     = createOperatorButton("*");
        divButton     = createOperatorButton("/");
        equalButton   = createOperatorButton("=");
        decimalButton = createOperatorButton(".");

        // Clear button (orange color to stand out)
        clearButton = new JButton("C");
        styleSpecialButton(clearButton, new Color(200, 80, 0));

        // Delete button (red color)
        deleteButton = new JButton("DEL");
        styleSpecialButton(deleteButton, new Color(180, 0, 0));

        // ------------------------------------------------------------
        // STEP 4E: POSITION ALL BUTTONS (setBounds)
        // setBounds(x, y, width, height)
        // x = distance from LEFT of window
        // y = distance from TOP of window
        // Think of it like a grid on your screen
        // ------------------------------------------------------------

        // Row 1: Clear and Delete
        clearButton.setBounds(20, 120, 165, 60);
        deleteButton.setBounds(205, 120, 165, 60);

        // Row 2: 7, 8, 9, Divide
        numberButtons[7].setBounds(20, 200, 80, 60);
        numberButtons[8].setBounds(110, 200, 80, 60);
        numberButtons[9].setBounds(200, 200, 80, 60);
        divButton.setBounds(290, 200, 80, 60);

        // Row 3: 4, 5, 6, Multiply
        numberButtons[4].setBounds(20, 270, 80, 60);
        numberButtons[5].setBounds(110, 270, 80, 60);
        numberButtons[6].setBounds(200, 270, 80, 60);
        mulButton.setBounds(290, 270, 80, 60);

        // Row 4: 1, 2, 3, Subtract
        numberButtons[1].setBounds(20, 340, 80, 60);
        numberButtons[2].setBounds(110, 340, 80, 60);
        numberButtons[3].setBounds(200, 340, 80, 60);
        subButton.setBounds(290, 340, 80, 60);

        // Row 5: Decimal, 0, Add, Equal
        decimalButton.setBounds(20, 410, 80, 60);
        numberButtons[0].setBounds(110, 410, 80, 60);
        addButton.setBounds(200, 410, 80, 60);
        equalButton.setBounds(290, 410, 80, 60);

        // ------------------------------------------------------------
        // STEP 4F: ADD EVERYTHING TO THE FRAME
        // Think of frame.add() like placing items on a table.
        // Nothing appears on screen until you ADD it to the frame!
        // ------------------------------------------------------------
        frame.add(screen);
        frame.add(clearButton);
        frame.add(deleteButton);

        for (int i = 0; i < 10; i++) {
            frame.add(numberButtons[i]);
        }

        frame.add(addButton);
        frame.add(subButton);
        frame.add(mulButton);
        frame.add(divButton);
        frame.add(equalButton);
        frame.add(decimalButton);

        // ------------------------------------------------------------
        // STEP 4G: MAKE THE WINDOW VISIBLE
        // IMPORTANT: Always do this LAST after adding everything!
        // If you do it first, the window shows up empty.
        // ------------------------------------------------------------
        frame.setVisible(true);
    }

    // ================================================================
    // STEP 5: HELPER METHODS
    // These are reusable methods to style buttons so we don't
    // repeat the same styling code over and over
    // ================================================================

    // Creates a styled operator button (+, -, *, /, =, .)
    JButton createOperatorButton(String label) {
        JButton btn = new JButton(label);
        btn.setFont(new Font("Arial", Font.BOLD, 22));
        btn.setBackground(new Color(0, 122, 204));  // Blue color
        btn.setForeground(Color.WHITE);
        btn.setFocusPainted(false);
        btn.setBorder(BorderFactory.createLineBorder(new Color(0, 100, 180)));
        btn.addActionListener(this);                // Listen for clicks!
        return btn;
    }

    // Styles the special buttons (Clear and Delete)
    void styleSpecialButton(JButton btn, Color color) {
        btn.setFont(new Font("Arial", Font.BOLD, 20));
        btn.setBackground(color);
        btn.setForeground(Color.WHITE);
        btn.setFocusPainted(false);
        btn.addActionListener(this);                // Listen for clicks!
    }

    // ================================================================
    // STEP 6: ACTION LISTENER — THE BRAIN OF THE CALCULATOR
    // This method runs AUTOMATICALLY every time any button is clicked.
    // "e.getSource()" tells us WHICH button was clicked.
    // ================================================================
    @Override
    public void actionPerformed(ActionEvent e) {

        // ------------------------------------------------------------
        // STEP 6A: NUMBER BUTTONS (0-9)
        // If a number button is clicked, append that number to screen
        // ------------------------------------------------------------
        for (int i = 0; i < 10; i++) {
            if (e.getSource() == numberButtons[i]) {
                screen.setText(screen.getText() + i);
                return; // Exit the method early, job is done
            }
        }

        // ------------------------------------------------------------
        // STEP 6B: DECIMAL BUTTON
        // Only add a decimal if there isn't one already
        // ------------------------------------------------------------
        if (e.getSource() == decimalButton) {
            if (!screen.getText().contains(".")) {
                screen.setText(screen.getText() + ".");
            }
            return;
        }

        // ------------------------------------------------------------
        // STEP 6C: CLEAR BUTTON
        // Reset everything back to empty/zero
        // ------------------------------------------------------------
        if (e.getSource() == clearButton) {
            screen.setText("");
            num1 = 0;
            num2 = 0;
            result = 0;
            operator = ' ';
            return;
        }

        // ------------------------------------------------------------
        // STEP 6D: DELETE BUTTON
        // Remove the last character from the screen
        // ------------------------------------------------------------
        if (e.getSource() == deleteButton) {
            String current = screen.getText();
            if (current.length() > 0) {
                screen.setText(current.substring(0, current.length() - 1));
            }
            return;
        }

        // ------------------------------------------------------------
        // STEP 6E: OPERATOR BUTTONS (+, -, *, /)
        // Save the first number and the operator, then clear the screen
        // so the user can type the second number
        // ------------------------------------------------------------
        if (e.getSource() == addButton || e.getSource() == subButton ||
            e.getSource() == mulButton || e.getSource() == divButton) {

            if (!screen.getText().isEmpty()) {
                num1 = Double.parseDouble(screen.getText()); // Save first number

                // Figure out which operator was pressed
                if (e.getSource() == addButton) operator = '+';
                if (e.getSource() == subButton) operator = '-';
                if (e.getSource() == mulButton) operator = '*';
                if (e.getSource() == divButton) operator = '/';

                screen.setText(""); // Clear screen for second number
            }
            return;
        }

        // ------------------------------------------------------------
        // STEP 6F: EQUAL BUTTON
        // Get the second number, perform the calculation, show result
        // ------------------------------------------------------------
        if (e.getSource() == equalButton) {
            if (!screen.getText().isEmpty()) {
                num2 = Double.parseDouble(screen.getText()); // Save second number

                // Perform the calculation based on the operator
                switch (operator) {
                    case '+': result = num1 + num2; break;
                    case '-': result = num1 - num2; break;
                    case '*': result = num1 * num2; break;
                    case '/':
                        if (num2 == 0) {
                            screen.setText("Error"); // Cannot divide by zero!
                            return;
                        }
                        result = num1 / num2;
                        break;
                }

                // Show result — if it's a whole number, show without decimal
                if (result == (long) result) {
                    screen.setText(String.valueOf((long) result));
                } else {
                    screen.setText(String.valueOf(result));
                }

                num1 = result; // Allow chaining calculations
            }
        }
    }

    // ================================================================
    // STEP 7: MAIN METHOD — Entry point of the program
    // We just create a new SwingCalculator object and everything
    // inside the constructor runs automatically!
    // ================================================================
    public static void main(String[] args) {
        new Calculator();
    }
}

// ================================================================
// QUICK RECAP — What you learned from this file:
//
//  JFrame       = The window
//  JTextField   = Text display / input box
//  JButton      = Clickable button
//  setBounds()  = Position and size of a component (x, y, w, h)
//  setVisible() = Show the window (always do this last!)
//  ActionListener = Interface that listens for button clicks
//  actionPerformed() = Runs when any button is clicked
//  e.getSource() = Tells you which button was clicked
//  frame.add()  = Add a component to the window
//
// NEXT THINGS TO EXPLORE:
//  - JPanel     = A container to group components
//  - JLabel     = Display text that is not editable
//  - JComboBox  = Dropdown menu
//  - JCheckBox  = Checkbox
//  - GridLayout = Auto-arrange buttons in a grid
// ================================================================