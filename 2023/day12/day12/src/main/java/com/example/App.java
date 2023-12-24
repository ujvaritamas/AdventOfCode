package com.example;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.List;

/**
 * Hello world!
 *
 */
public class App 
{


    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        FileHandler fh = new FileHandler();
        List<String> lines = fh.readFile();
        System.out.println("-------------");

        int final_result = 0;

        for(String line: lines){
            System.out.println(line);
            ISolution s = fh.parseLine(line, new Solution());
            s.display();
            final_result += s.solve();
        }
        System.out.println("final result: " + final_result);
    }
}
