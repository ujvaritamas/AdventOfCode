package com.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import java.nio.charset.StandardCharsets;


public class FileHandler {

    ISolution solver;

    public FileHandler(){
    }

    public List<String> readFile(){

            List<String> ret = new ArrayList<>();
            InputStream myObj = this.getClass().getResourceAsStream("/test_input.txt");
            InputStreamReader streamReader = new InputStreamReader(myObj, StandardCharsets.UTF_8);

            BufferedReader reader = new BufferedReader(streamReader);
            try {
                ret = reader.lines().toList();

                reader.close();
            }
            catch (IOException e){
                e.printStackTrace();
            }
            return ret;
    }

    public ISolution parseLine(String line, ISolution solver){

        boolean readDigit = false;
        boolean readData = true;

        String data = "";
        int num = 0;


        for(int i= 0; i<line.length(); i++){
        //for(char c:line.toCharArray()){
            char c = line.charAt(i);
            if(c==' '){
                readData = false;
                readDigit = true;
                solver.setData(data);
                continue;
            }

            if(readData){
                if(c == '?'){
                    solver.addUnknownCharPosition(i);
                }
                data += c;
            }

            if(readDigit){
                if(Character.isDigit(c)){
                    num = num*10+ Character.getNumericValue(c);
                }
                else{
                    solver.addConfigNumber(num);
                    num = 0;
                }
            }

        }

        //add the last number
        solver.addConfigNumber(num);

        return solver;
    }
}
