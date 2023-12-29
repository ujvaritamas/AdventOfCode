package com.example;

import java.util.ArrayList;
import java.util.List;

public class Solution1 {

    private List<Integer> findReflectionVertical(List<String> inputSet){

        List<Integer>  ret = new ArrayList<>();

        int checkIndex0 =0;
        int checkIndex1 = 1;
        boolean reflectFound = true;
        for(int col = 0; col<inputSet.get(0).length()-1; col++){
            checkIndex0 = col;
            checkIndex1 = col+1;
            reflectFound = true;
            for(int row = 0; row<inputSet.size(); row++){
                for(int i = 0; i<checkIndex0+1; i++){

                    if(checkIndex1+i==inputSet.get(0).length()){
                    break;
                }

                    if(inputSet.get(row).charAt(checkIndex0-i) == inputSet.get(row).charAt(checkIndex1+i)){

                    }
                    else{
                        reflectFound = false;
                        break;
                    }
                }
                
            }
            if(reflectFound){
                ret.add(checkIndex0);
            }
        }

        return ret;
    }

    private List<Integer> findReflectionHorizontal(List<String> inputSet){

        List<Integer>  ret = new ArrayList<>();

        int checkIndex0 =0;
        int checkIndex1 = 1;
        boolean reflectFound = true;
        for(int i = 0; i<inputSet.size()-1; i++){
            checkIndex0 = i;
            checkIndex1 = i+1;
            reflectFound = true;

            for(int j = 0;j<checkIndex0+1; j++){

                if(checkIndex1+j==inputSet.size()){
                    break;
                }

                if(inputSet.get(checkIndex0-j).equals(inputSet.get(checkIndex1+j))){
                }
                else{
                    reflectFound = false;
                    break;
                }
            }

            if(reflectFound){
                ret.add(checkIndex0);
            }
        }

        return ret;
    }

    private long summarize(List<Integer> indexesHor, List<Integer> indexesVert){
        long sum = 0;
        if(indexesHor.size() >2){
            System.out.println("Not ok0");
            System.out.println(indexesHor);
        }

        if(indexesVert.size() >2){
            System.out.println("Not ok1");
            System.out.println(indexesVert);
        }

        int indVer = 0;
        if(indexesVert.size()>0){
            indVer = indexesVert.get(0)+1;
        }
        int indHor = 0;
        if(indexesHor.size()>0){
            indHor = indexesHor.get(0)+1;
        }

        System.out.println("--------------");
        System.out.println(indexesHor);
        System.out.println(indexesVert);
        System.out.println("--------------");
        sum = 100*(indHor)   + indVer;
        return sum;
    }

    public long solve(List<String> inputSet){
        List<Integer> indHor = findReflectionHorizontal(inputSet);
        List<Integer> indVer = findReflectionVertical(inputSet);

        return summarize(indHor, indVer);
    }
}

