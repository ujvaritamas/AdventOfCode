package mypackage;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.*;  
import java.util.concurrent.TimeUnit;

import mypackage.Node;

class Solution2 {

    String filePath;
    String instruction;
    boolean readInstruction;
    List<Node> nodeList;
    String startNodeValue;
    List<String> checkValues;
    List<Long> mynumbers;

    public Solution2(){
        filePath = "test_input.txt";
        instruction = "";
        readInstruction = true;
        nodeList = new ArrayList<Node>();
        startNodeValue="";
        checkValues = new ArrayList<String>();
        mynumbers = new ArrayList<>();
    }

    public void solve() {
        System.out.println("Hello, hello1!"); 
        
        parse();
        collectStartNodes();

        System.out.println("here");

        solveIt();
    }

    private void addNode(String value, String l, String r){
        boolean isNodeAdded = false;
        Node current = null;
        boolean isLeftAdded = false;
        Node left= null;
        boolean isRightAdded = false;
        Node right= null;
        for(Node n:nodeList){
            if(n.value.equals(value)){
                isNodeAdded = true;
                current = n;
            }

            if(n.value.equals(l)){
                isLeftAdded = true;
                left = n;
            }

            if(n.value.equals(r)){
                isRightAdded = true;
                right = n;
            }

        }

        if(isNodeAdded == true){
            if(isLeftAdded == true){
                current.setLeft(left);
            }
            else{
                Node n = new Node(l);
                nodeList.add(n);
                current.setLeft(n);
            }
            if(isRightAdded == true){
                current.setRight(right);
            }
            else{
                if(l.equals(r)){
                    current.setRight(current.left);
                }
                else{
                    Node n = new Node(r);
                    nodeList.add(n);
                    current.setRight(n);
                }
                
            }
        }
        else{
            current = new Node(value);

            if(isLeftAdded == true){
                current.setLeft(left);
            }
            else{
                if(value.equals(l)){
                    current.setLeft(current);
                }
                else{
                    Node n = new Node(l);
                    nodeList.add(n);
                    current.setLeft(n);
                }
                
            }
            if(isRightAdded == true){
                current.setRight(right);
            }
            else{
                if(value.equals(l)){
                    current.setRight(current);
                }
                else{
                    if(l.equals(r)){
                        current.setRight(current.left);
                    }
                    else{
                        Node n = new Node(r);
                        nodeList.add(n);
                        current.setRight(n);
                    }
                }
            }
            nodeList.add(current);
        }
    }

    private void parseLine(String line){
        boolean readValue = true;
        String value = "";
        boolean readLeft = false;
        String left = "";
        boolean readRight = false;
        String right = "";
        for (int i = 0 ; i != line.length() ; i++) {
            char c = line.charAt(i);

            if(readValue){
                value = value+line.charAt(i)+line.charAt(i+1)+line.charAt(i+2);
                i=i+6;  //skip 3 char + <whitespace> + <=> + <whitespace> + <(>
                readValue = false;
                readLeft = true;
                continue;

            }
            
            if(readLeft){
                left=left+line.charAt(i)+line.charAt(i+1)+line.charAt(i+2);
                i=i+4;   //skip 3 char+<,>+<whitespace>
                readLeft = false;
                readRight = true;
                continue;
            }

            if(readRight){
                right=right+line.charAt(i)+line.charAt(i+1)+line.charAt(i+2);
                break;
            }

        }
        //System.out.println("Parse line");
        //System.out.println("Value: " + value + " left: "+ left+ " right: "+ right);
        addNode(value, left, right);
    }

    private void parse(){
        BufferedReader reader;
        boolean isFirst= true;
        try {
			reader = new BufferedReader(new FileReader(filePath));
			String line = reader.readLine();

			while (line != null) {
                if(line.length() == 0){
                    readInstruction = false;
                    // read next line
				    line = reader.readLine();
                    continue;
                }

                System.out.println(line);
                

                if(readInstruction == true){
                    instruction = instruction+line;
                }
                else{
                    if(isFirst){
                        //save the head
                        startNodeValue = startNodeValue+line.charAt(0)+line.charAt(1)+line.charAt(2);
                        isFirst=false;
                    }
                    parseLine(line);
                }
				line = reader.readLine();
			}
            System.out.println("hasNewline");
			reader.close();


		} catch (IOException e) {
			e.printStackTrace();
		}
        System.out.println(instruction);
        System.out.println("parse finished");
        print();
        
    }

    private void print(){
        System.out.println(nodeList);
        for(Node n: nodeList){

            n.print();
        }
    }

    private Node searchNode(String value){
        for(Node n : nodeList){
            if(n.value.equals(value)){
                return n;
            }
        }
        return null;
    }

    private void solveIt(){
        long count = 0;
        //Node node = searchNode("AAA");//searchNode(startNodeValue);
        System.out.println(instruction);
        int cycleCount = 0;
        System.out.println(checkValues);

        boolean found0 = false;
        boolean found1 = false;
        boolean found2 = false;
        boolean found3 = false;
        boolean found4 = false;
        boolean found5 = false;

        while(true){
            //System.out.println(cycleCount);
            cycleCount++;

            for (int ins = 0 ; ins < instruction.length() ; ins++) {
                char c = instruction.charAt(ins);
                
                for(int j = 0; j<checkValues.size();j++){
                //for(String check:checkValues){
                    Node nodetmp = searchNode(checkValues.get(j));
                    if(c == 'L'){
                        //check = ""+nodetmp.left.value;
                        checkValues.set(j, ""+nodetmp.left.value);
                    }
                    if(c=='R'){
                        //check = ""+nodetmp.right.value;
                        checkValues.set(j, ""+nodetmp.right.value);
                    }
                }
                count++;

                //start values for me: [STA, AAA, GPA, LKA, DFA, KKA]
                if(!found0)
                    if(checkValues.get(0).charAt(2)=='Z'){
                        System.out.println("Found 0: "+checkValues.get(0)+"   "+count);
                        mynumbers.add(Long.valueOf(count));
                        found0 = true;
                    }
                if(!found1)
                    if(checkValues.get(1).charAt(2)=='Z'){
                        System.out.println("Found 1: "+checkValues.get(1)+"   "+count);
                        found1 = true;
                        mynumbers.add(Long.valueOf(count));
                    }
                if(!found2)
                    if(checkValues.get(2).charAt(2)=='Z'){
                        System.out.println("Found 2: "+checkValues.get(2)+"   "+count);
                        found2 = true;
                        mynumbers.add(Long.valueOf(count));
                    }

                if(!found3)
                    if(checkValues.get(3).charAt(2)=='Z'){
                        System.out.println("Found 3: "+checkValues.get(3)+"   "+count);
                        found3 = true;
                        mynumbers.add(Long.valueOf(count));
                    }

                if(!found4)
                    if(checkValues.get(4).charAt(2)=='Z'){
                        System.out.println("Found 4: "+checkValues.get(4)+"   "+count);
                        found4 = true;
                        mynumbers.add(Long.valueOf(count));
                    }

                if(!found5)
                    if(checkValues.get(5).charAt(2)=='Z'){
                        System.out.println("Found 5: "+checkValues.get(5)+"   "+count);
                        found5 = true;
                        mynumbers.add(Long.valueOf(count));
                    }

                if(found0 & found1 & found2 & found3 & found4 & found5)
                {
                    System.out.println("Final result: "+calculateLCM());
                    return;
                }
            }
        }
        //System.out.println("Final result: "+count);
    }
    
    void collectStartNodes(){
        for(Node n : nodeList){
            if(n.value.charAt(2) == 'A'){
                String tmp = ""+ n.value;
                checkValues.add(tmp);
                //System.out.println(n.value);
            }
        }
    }


    // calculate gcd
    private long gcd(long a, long b) {
        while (b > 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // calculate LCM
    private long lcm(long a, long b) {
        return (a / gcd(a, b)) * b;
    }

    // Több szám LCM kiszámítása
    public long calculateLCM() {
        if (mynumbers.size() == 0) {
            throw new IllegalArgumentException("not valid");
        }

        long result = mynumbers.get(0);

        for (int i = 1; i < mynumbers.size(); i++) {
            result = lcm(result, mynumbers.get(i));
        }

        return result;
    }

}

