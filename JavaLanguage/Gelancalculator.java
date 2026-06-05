import java.text.DecimalFormat;
import java.awt.*;
import javax.swing.JOptionPane;
import java.util.logging.Logger;

public class Gelancalculator extends javax.swing.JFrame {

    private static final Logger logger = Logger.getLogger(Gelancalculator.class.getName());

    // ── Colors ────────────────────────────────────────────────────────────────
    private static final Color ORANGE_BG     = new Color(0xE8783A);
    private static final Color INPUT_PINK    = new Color(255, 204, 204);
    private static final Color OUTPUT_YELLOW = new Color(238, 240, 176);
    private static final Color BTN_COMPUTE   = new Color(255, 51, 102);
    private static final Color BTN_CLEAR     = new Color(212, 232, 160);
    private static final Color BTN_QUIT      = new Color(255, 204, 153);
    private static final Color LABEL_DARK    = new Color(0x3A1A00);
    private static final Font  LABEL_FONT    = new Font("Serif", Font.BOLD, 13);

    public Gelancalculator() {
        initComponents();
    }

    private void initComponents() {

        firstnumfield  = new javax.swing.JTextField();
        secondnumfield = new javax.swing.JTextField();
        sumresult      = new javax.swing.JTextField();
        diffres        = new javax.swing.JTextField();
        productres     = new javax.swing.JTextField();
        fpqres         = new javax.swing.JTextField();
        intqres        = new javax.swing.JTextField();
        remres         = new javax.swing.JTextField();

        computebutton  = new javax.swing.JButton();
        clearbutton    = new javax.swing.JButton();
        quitbutton     = new javax.swing.JButton();

        firstnumlabel  = new javax.swing.JLabel();
        secondnumlabel = new javax.swing.JLabel();
        sum            = new javax.swing.JLabel();
        diff           = new javax.swing.JLabel();
        product        = new javax.swing.JLabel();
        fqo            = new javax.swing.JLabel();
        intq           = new javax.swing.JLabel();
        remainder      = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        // ── Orange content pane ───────────────────────────────────────────────
        getContentPane().setBackground(ORANGE_BG);

        // ── Input fields ──────────────────────────────────────────────────────
        styleInputField(firstnumfield);
        styleInputField(secondnumfield);
        firstnumfield.addActionListener(this::firstnumfieldActionPerformed);

        // ── Output fields ─────────────────────────────────────────────────────
        styleOutputField(sumresult);
        styleOutputField(diffres);
        styleOutputField(productres);
        styleOutputField(fpqres);
        styleOutputField(intqres);
        styleOutputField(remres);

        sumresult.addActionListener(this::sumresultActionPerformed);
        diffres.addActionListener(this::diffresActionPerformed);
        productres.addActionListener(this::productresActionPerformed);
        fpqres.addActionListener(this::fpqresActionPerformed);
        intqres.addActionListener(this::intqresActionPerformed);
        remres.addActionListener(this::remresActionPerformed);

        // ── Buttons ───────────────────────────────────────────────────────────
        styleButton(computebutton, "COMPUTE", BTN_COMPUTE, Color.WHITE);
        styleButton(clearbutton,   "CLEAR",   BTN_CLEAR,   LABEL_DARK);
        styleButton(quitbutton,    "QUIT",    BTN_QUIT,    LABEL_DARK);

        computebutton.addActionListener(this::computebuttonActionPerformed);
        clearbutton.addActionListener(this::clearbuttonActionPerformed);
        quitbutton.addActionListener(this::quitbuttonActionPerformed);

        // ── Labels ────────────────────────────────────────────────────────────
        styleLabel(firstnumlabel,  "First Number:");
        styleLabel(secondnumlabel, "Second Number:");
        styleLabel(sum,       "SUM:");
        styleLabel(diff,      "DIFFERENCE:");
        styleLabel(product,   "PRODUCT:");
        styleLabel(fqo,       "FLOATING POINT QUOTIENT:");
        styleLabel(intq,      "INTEGER QUOTIENT:");
        styleLabel(remainder, "REMAINDER:");

        sum.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        diff.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        product.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        fqo.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        intq.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);
        remainder.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);

        // ── Layout (same GroupLayout structure as original) ───────────────────
        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);

        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(16, 16, 16)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(sum)
                            .addComponent(diff)
                            .addComponent(product)
                            .addComponent(intq)
                            .addComponent(remainder)
                            .addComponent(fqo)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(firstnumlabel)
                                    .addComponent(secondnumlabel))
                                .addGap(83, 83, 83)))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED,
                            javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(0, 47, Short.MAX_VALUE)
                        .addComponent(computebutton)
                        .addGap(48, 48, 48)
                        .addComponent(clearbutton)
                        .addGap(2, 2, 2)))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING,
                        layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(sumresult,   javax.swing.GroupLayout.Alignment.TRAILING,
                                javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(diffres,     javax.swing.GroupLayout.Alignment.TRAILING,
                                javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(productres,  javax.swing.GroupLayout.Alignment.TRAILING,
                                javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(fpqres,      javax.swing.GroupLayout.Alignment.TRAILING,
                                javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(intqres,     javax.swing.GroupLayout.Alignment.TRAILING,
                                javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(remres,      javax.swing.GroupLayout.Alignment.TRAILING,
                                javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addComponent(quitbutton))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING,
                        layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                        .addComponent(secondnumfield, javax.swing.GroupLayout.Alignment.TRAILING,
                            javax.swing.GroupLayout.DEFAULT_SIZE, 131, Short.MAX_VALUE)
                        .addComponent(firstnumfield,  javax.swing.GroupLayout.Alignment.TRAILING)))
                .addGap(21, 21, 21))
        );

        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(25, 25, 25)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(firstnumfield,  javax.swing.GroupLayout.PREFERRED_SIZE,
                        javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(firstnumlabel))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(secondnumfield, javax.swing.GroupLayout.PREFERRED_SIZE,
                        javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(secondnumlabel))
                .addGap(41, 41, 41)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(sumresult, javax.swing.GroupLayout.PREFERRED_SIZE,
                        javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(sum))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(diffres, javax.swing.GroupLayout.PREFERRED_SIZE,
                        javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(diff))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(productres, javax.swing.GroupLayout.PREFERRED_SIZE,
                        javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(product))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(fpqres, javax.swing.GroupLayout.PREFERRED_SIZE,
                        javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(fqo))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(intqres, javax.swing.GroupLayout.PREFERRED_SIZE,
                        javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(intq))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(remres, javax.swing.GroupLayout.PREFERRED_SIZE,
                        javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(remainder))
                .addGap(34, 34, 34)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(computebutton)
                    .addComponent(clearbutton)
                    .addComponent(quitbutton))
                .addContainerGap(20, Short.MAX_VALUE))
        );

        pack();
    }

    // ── Style helpers ─────────────────────────────────────────────────────────

    private void styleInputField(javax.swing.JTextField f) {
        f.setBackground(INPUT_PINK);
        f.setFont(new Font("SansSerif", Font.PLAIN, 13));
        f.setHorizontalAlignment(javax.swing.JTextField.RIGHT);
        f.setBorder(javax.swing.BorderFactory.createCompoundBorder(
            javax.swing.BorderFactory.createLineBorder(new Color(0xCC8855), 1),
            javax.swing.BorderFactory.createEmptyBorder(2, 4, 2, 4)));
    }

    private void styleOutputField(javax.swing.JTextField f) {
        f.setBackground(OUTPUT_YELLOW);
        f.setEditable(false);
        f.setFont(new Font("SansSerif", Font.PLAIN, 13));
        f.setHorizontalAlignment(javax.swing.JTextField.RIGHT);
        f.setBorder(javax.swing.BorderFactory.createCompoundBorder(
            javax.swing.BorderFactory.createLineBorder(new Color(0xAAAA66), 1),
            javax.swing.BorderFactory.createEmptyBorder(2, 4, 2, 4)));
    }

    private void styleButton(javax.swing.JButton b, String text, Color bg, Color fg) {
        b.setText(text);
        b.setBackground(bg);
        b.setForeground(fg);
        b.setFont(new Font("Serif", Font.BOLD, 13));
        b.setFocusPainted(false);
        b.setBorder(javax.swing.BorderFactory.createCompoundBorder(
            javax.swing.BorderFactory.createLineBorder(new Color(0xAA7744), 1),
            javax.swing.BorderFactory.createEmptyBorder(4, 12, 4, 12)));
        b.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
    }

    private void styleLabel(javax.swing.JLabel l, String text) {
        l.setText(text);
        l.setFont(LABEL_FONT);
        l.setForeground(LABEL_DARK);
        l.setOpaque(false);
    }

    // ── Action handlers (Kyla's original logic, unchanged) ────────────────────

    private void firstnumfieldActionPerformed(java.awt.event.ActionEvent evt) { }
    private void sumresultActionPerformed(java.awt.event.ActionEvent evt)     { }
    private void diffresActionPerformed(java.awt.event.ActionEvent evt)       { }
    private void productresActionPerformed(java.awt.event.ActionEvent evt)    { }
    private void fpqresActionPerformed(java.awt.event.ActionEvent evt)        { }
    private void intqresActionPerformed(java.awt.event.ActionEvent evt)       { }
    private void remresActionPerformed(java.awt.event.ActionEvent evt)        { }

    private void quitbuttonActionPerformed(java.awt.event.ActionEvent evt) {
        int choice = JOptionPane.showConfirmDialog(null, "Are you sure?", "Confirm",
                JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
        switch (choice) {
            case JOptionPane.YES_OPTION -> System.exit(0);
            case JOptionPane.NO_OPTION  -> JOptionPane.showMessageDialog(null, "You decided to not to close ...");
            default                     -> JOptionPane.showMessageDialog(null, "Unexpected choice ...");
        }
    }

    private void clearbuttonActionPerformed(java.awt.event.ActionEvent evt) {
        firstnumfield.setText("");
        secondnumfield.setText("");
        sumresult.setText("");
        diffres.setText("");
        productres.setText("");
        fpqres.setText("");
        intqres.setText("");
        remres.setText("");
    }

    private void computebuttonActionPerformed(java.awt.event.ActionEvent evt) {
        double sumVal, diffVal, prod, quotient, intQuotient, num1, num2;
        long rem;
        num1 = Double.parseDouble(firstnumfield.getText().trim());
        num2 = Double.parseDouble(secondnumfield.getText().trim());
        DecimalFormat df = new DecimalFormat("#,##0.00");
        sumVal      = num1 + num2;
        diffVal     = num1 - num2;
        prod        = num1 * num2;
        quotient    = num1 / num2;
        intQuotient = Math.round(num1) / Math.round(num2);
        rem         = Math.round(num1) % Math.round(num2);
        sumresult.setText(df.format(sumVal));
        diffres.setText(df.format(diffVal));
        productres.setText(df.format(prod));
        fpqres.setText(df.format(quotient));
        intqres.setText(df.format(intQuotient));
        remres.setText(String.valueOf(rem));
    }

    // ── Main ──────────────────────────────────────────────────────────────────

    public static void main(String args[]) {
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info :
                    javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ReflectiveOperationException | javax.swing.UnsupportedLookAndFeelException ex) {
            logger.log(java.util.logging.Level.SEVERE, null, ex);
        }

        String nameMo = JOptionPane.showInputDialog(null, "Your name Please ...",
                "Let Me Know You", JOptionPane.QUESTION_MESSAGE);

        Gelancalculator frame = new Gelancalculator();
        frame.setLocationRelativeTo(null);
        frame.setTitle(nameMo);
        frame.setVisible(true);
    }

    // ── Variables declaration ─────────────────────────────────────────────────
    private javax.swing.JButton    clearbutton;
    private javax.swing.JButton    computebutton;
    private javax.swing.JLabel     diff;
    private javax.swing.JTextField diffres;
    private javax.swing.JTextField firstnumfield;
    private javax.swing.JLabel     firstnumlabel;
    private javax.swing.JTextField fpqres;
    private javax.swing.JLabel     fqo;
    private javax.swing.JLabel     intq;
    private javax.swing.JTextField intqres;
    private javax.swing.JLabel     product;
    private javax.swing.JTextField productres;
    private javax.swing.JButton    quitbutton;
    private javax.swing.JLabel     remainder;
    private javax.swing.JTextField remres;
    private javax.swing.JTextField secondnumfield;
    private javax.swing.JLabel     secondnumlabel;
    private javax.swing.JLabel     sum;
    private javax.swing.JTextField sumresult;
}