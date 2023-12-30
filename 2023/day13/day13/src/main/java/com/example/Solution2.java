package com.example;

import java.util.ArrayList;
import java.util.List;

public class Solution2 extends Solution1{
    public void findSmudge(List<String> inputSet){

        for(int row = 0; row<inputSet.size(); row++){
            for(int col = 0; col<inputSet.get(0).length(); col++){
                String ref = inputSet.get(row);
                char[] tmp = inputSet.get(row).toCharArray();

                String strCopy = String.copyValueOf(inputSet.get(row).toCharArray());


                if(tmp[col] == '.'){
                    tmp[col] = '#';
                }
                else{
                    tmp[col] = '.';
                }
                ref = String.copyValueOf(tmp);
                List<Integer> indHor = findReflectionHorizontal(inputSet);
                //List<Integer> indVer = findReflectionVertical(inputSet);
                
                if(indHor.size() ==1){ //|| indVer.size() == 1){
                    
                    System.out.println("Smudge found!! row: " + row +" col: "+ col );
                    System.out.println(summarize(indHor, new ArrayList<>()));
                    return ;
                }
                ref = strCopy;
                
            }
        }


        List<Integer> indHor = findReflectionHorizontal(inputSet);
        List<Integer> indVer = findReflectionVertical(inputSet);

    }
}
