package com.example;
import java.util.ArrayList;
import java.util.List;
public class Solution {
    private List<Integer> config;
    private String data;
    private List<Integer> unknownCharPosition;

    public Solution(){
        this.config = new ArrayList<>();
        data = new String();
        unknownCharPosition = new ArrayList<>();
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

        if(numOfComb>0){
            for(int i = 0; i<Math.pow(2, numOfComb); i++){
                int[] conf = this.decToBin(i);

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

        return count;
    }

    private int[] decToBin(int n){
        int numOfComb = this.unknownCharPosition.size();
        int[] binaryNum = new int[numOfComb];
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
        List<Integer> current = new ArrayList<>();
        for(char c: d){
            if(c == '#'){
                count++;
            }
            else{
                if(count>0){
                    current.add(count);
                }
                count = 0;
            }
        }
        if(count>0){
            current.add(count);
            count = 0;
        }

        if(this.config.size() != current.size()){
            return false;
        }

        for(int i = 0; i<this.config.size(); i++){
            if(this.config.get(i) != current.get(i)){
                return false;
            }
        }

        return true;
    }
}
