package mypackage;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.*;  

import mypackage.Node;

class Solution1 {

    String filePath;
    String instruction;
    boolean readInstruction;
    List<Node> nodeList;
    String startNodeValue;

    public Solution1(){
        filePath = "test_input.txt";
        instruction = "";
        readInstruction = true;
        nodeList = new ArrayList<Node>();
        startNodeValue="";
    }

    public void solve() {
        System.out.println("Hello, hello!"); 
        
        parse();

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
        int count = 0;
        Node node = searchNode("AAA");//searchNode(startNodeValue);
        System.out.println(instruction);
        int cycleCount = 0;
        while(true){
            System.out.println(cycleCount);
            cycleCount++;
            for (int i = 0 ; i != instruction.length() ; i++) {
                
                char c = instruction.charAt(i);
                if(c == 'L'){
                    node = node.left;
                    count++;
                }
                if(c=='R'){
                    node = node.right;
                    count++;
                }

                if(node.value.equals("ZZZ")){
                    System.out.println("Final result: "+count);
                    return;
                }
            }
        }
        //System.out.println("Final result: "+count);
    }
    
}

