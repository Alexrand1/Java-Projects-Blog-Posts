package FTP_GUI_Interface;

import org.apache.commons.net.ftp.FTPClient;
import org.apache.commons.net.ftp.FTPClientConfig;
import org.apache.commons.net.ftp.FTPFile;

import java.io.IOException;
import java.io.InputStream;

/**
 * A simple FTP client used for uploading files to an FTP server, and retrieving byte-streams of files
 * from a remote FTP server.
 */
public class FTPClientRunner {

    private FTPClient client;
    private FTPClientConfig config;
    private String username;
    private String password;
    private String server;

    /**
     * Constructor for FTPClientRunner, takes in the FTP username, password, and server name for connection
     * @param un
     * @param pw
     * @param server
     */
    public FTPClientRunner(String un, String pw, String server) {
        this.username = un;
        this.password = pw;
        this.server = server;
        client = new FTPClient();
        config = new FTPClientConfig();
    }

    /**
     * Helper method for connecting to the FTP server
     */
    public void makeConnection() {
        try {
            String srvr = this.server;
            client.configure(config);
            client.connect(srvr);
            client.login(username, password);
            System.out.println("Connected to " + srvr);
            System.out.println(client.getReplyString());
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * method to print the current files in the FTP server's current directory.
     */
    public void printFiles() {
        try {
            FTPFile[] files = client.listFiles();
            for (FTPFile file: files) {
                System.out.println(file);
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Takes in a file from the local computer and uploads it to the connected FTP server
     * @param file
     */
    public void upload(String file){
        try {
            client.remoteStore(file);
            System.out.println("Successfully uploaded");
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Retrieves a specified file InputStream from the FTP server, reads the first 3 bytes in (char) form.
     * @param file
     */
    public void download(String file) {
        try {
            InputStream stream = client.retrieveFileStream(file);
            System.out.println("Successfully Retrieved");
            System.out.println((char)stream.read());
            System.out.println((char)stream.read());
            System.out.println((char)stream.read());
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        FTPClientRunner run = new FTPClientRunner("dlpuser@dlptest.com", "bbCKucPzfr4b9YXUY7tvsNKyh", "ftp.dlptest.com");
        run.makeConnection();
        run.upload("C:\\Users\\Alex Randall\\Documents\\test.txt");
        run.download("D18M10J2019H11M52S59C3.txt");
        run.printFiles();
    }
}


