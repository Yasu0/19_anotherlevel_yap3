import javax.swing.*;
import java.awt.event.*;

class MyFrame
{
    private JFrame frm = new JFrame();
    private JTextArea textArea = new JTextArea();
    private JMenuBar menuBar = new JMenuBar();
    private JMenu fileMenu = new JMenu("파일");
    private JMenu radio_checkMenu = new JMenu("기능메뉴");
    private JMenuItem newItem = new JMenuItem("새로 만들기");
    private JMenuItem openItem = new JMenuItem("열기");
    private JMenuItem saveItem = new JMenuItem("저장");
    
    public MyFrame() 
    {
        
        menuBar.add(fileMenu);
        menuBar.add(radio_checkMenu);
        
        
        fileMenu.add(newItem);
        fileMenu.add(openItem);
        fileMenu.add(saveItem);
        
        newItem.addActionListener(this);
        openItem.addActionListener(this);
        saveItem.addActionListener(this);
              
        fileMenu.setMnemonic(KeyEvent.VK_F);
        radio_checkMenu.setMnemonic(KeyEvent.VK_Q);
        
        
        newItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_N, KeyEvent.CTRL_MASK));
        openItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_O, KeyEvent.CTRL_MASK));
        saveItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, KeyEvent.CTRL_MASK));
        
        frm.add(textArea, BorderLayout.CENTER);
        frm.setJMenuBar(menuBar);
        frm.add(stateLabel, BorderLayout.SOUTH);
        
       
     
        frm.setVisible(true);
    }
 
   
}