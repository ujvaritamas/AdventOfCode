package com.example;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");


        FileHandler fh = new FileHandler();
        List<String> lines = fh.readFile();
        List<List<String>> parsedLines =  fh.parse(lines);
        System.out.println("-------------");
        System.out.println(parsedLines);

        /* 
        Solution1 solver = new Solution1();

        long finalResult = 0;
        for(List<String> i : parsedLines){
            System.out.println(i);
            finalResult += solver.solve(i);
        }
        System.out.println("Final result: " + finalResult);
        */
        System.out.println("?????????????");
        Solution2 solver = new Solution2();
        for(List<String> i : parsedLines){
            System.out.println(i);
            solver.findSmudge(i);
            System.out.println("-------------");
        }
        
        
        
    }
}