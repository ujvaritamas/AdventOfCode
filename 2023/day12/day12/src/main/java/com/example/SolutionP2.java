package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class SolutionP2 implements ISolution{
    private List<Integer> config;
    private String data;
    private List<Integer> unknownCharPosition;

    public HashMap<String, String> cache;



    public SolutionP2(){
        this.config = new ArrayList<>();
        data = new String();
        unknownCharPosition = new ArrayList<>();
        cache = new HashMap<String, String>();
    }

    public void setData(String data){
        this.data = data;
    }

    public String getData(){
        return this.data;
    }

    public void setConfig(List<Integer> l){
        this.config = l;
    }

    public List<Integer> getConfig(){
        return this.config;
    }

    public void addConfigNumber(int n){
        this.config.add(n);
    }

    public void display(){
        System.out.println("Data: "+this.data);
        System.out.println("Config: "+this.config);
        System.out.println("unknownCharPosition: "+this.unknownCharPosition);
    }

    public void addUnknownCharPosition(int pos){
        this.unknownCharPosition.add(pos);
    }

    public int solve(){
        //00, 01, 10, 11
        //000, 001, 010, 011, 100, 101, 110, 111
        char[] generated = this.data.toCharArray();
        int numOfComb = this.unknownCharPosition.size();

        int count = 0;

            System.out.println(Math.pow(2, numOfComb));
        if(numOfComb>0){
            for(long i = 0; i<Math.pow(2, numOfComb); i++){
                long[] conf = this.decToBin(i);
                

                for(int j = 0; j<numOfComb;j++){
                    if(conf[j] == 1){
                        generated[this.unknownCharPosition.get(j)] = '#';
                    }
                    else{
                        generated[this.unknownCharPosition.get(j)] = '.';
                    }
                }
                if(this.validate(generated)){
                    count++;
                }
                //reset
                generated = this.data.toCharArray();

            }
        }
        else{
            if(this.validate(generated)){
                return 1;
            }
        }

        //System.out.println(cache);
        return count;
    }

    private long[] decToBin(long n){
        int numOfComb = this.unknownCharPosition.size();
        long[] binaryNum = new long[numOfComb];
        int i = 0;
        while (n > 0)
        {
            // storing remainder in binary array
            binaryNum[i] = n % 2;
            n = n / 2;
            i++;
        }

        return binaryNum;
    }

    public boolean validate(char[] d){
        int count = 0;
        int checkIndex = 0;
        String substring_hash = "";
        String conf_hash = "";
        for(char c: d){
            substring_hash += c;

            if(cache.containsKey(substring_hash+conf_hash)){
                return false;
            }

            if(c == '.'){
                if(count>0){
                    if(checkIndex>this.config.size()-1){
                        cache.put(substring_hash+conf_hash, "dummy");
                        return false;
                    }
                    conf_hash += this.config.get(checkIndex);

                    if(this.config.get(checkIndex) == count){
                        checkIndex++;
                    }
                    else{
                        cache.put(substring_hash+conf_hash, "dummy");
                        return false;
                    }
                }
                count = 0;

            }
            else{
                count++;
            }
        }

        if(count>0){
            if(checkIndex>this.config.size()-1){
                cache.put(substring_hash+conf_hash, "dummy");
                return false;
            }
            conf_hash += this.config.get(checkIndex);

            if(this.config.get(checkIndex) == count){
                checkIndex++;
            }
            else{
                cache.put(substring_hash+conf_hash, "dummy");
                return false;
            }
        }

        if(checkIndex<=this.config.size()-1){
            cache.put(substring_hash+conf_hash, "dummy");
            return false;
        }
        //System.out.println(d);
        //System.out.println(this.config);
        return true;
    }


    // solution2
    public String manipulateLine(String line){
        String ret = new String();

        String[] words = line.split(" ");

        for(int i = 0; i<5;i++){
            ret += words[0];
            if(i == 4){
                break;
            }
            ret += "?";
        }

        ret += " ";

        for(int i = 0; i<5;i++){
            ret += words[1];
            if(i == 4){
                break;
            }
            ret += ",";
        }

        return ret;
    }
}
