package com.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import java.nio.charset.StandardCharsets;


public class FileHandler {

    public FileHandler(){
    }

    public List<String> readFile(){

            List<String> ret = new ArrayList<>();
            InputStream myObj = this.getClass().getResourceAsStream("/test_input.txt");
            System.out.println(myObj);
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

    public List<List<String>> parse(List<String> lines){
        List<List<String>> ret = new ArrayList<>();

        List<String> temp = new ArrayList<>();
        for(String lineString : lines){
            if(lineString.equals("")){
                System.out.println("new line found");
                ret.add(temp);
                temp = new ArrayList<>();
                continue;
            }
            temp.add(lineString);

            //temp.add(lineString);

        }
        ret.add(temp);

        return ret;
    }
}
