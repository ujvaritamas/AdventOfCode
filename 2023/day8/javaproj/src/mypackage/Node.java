package mypackage;

class Node{
    String value;
    Node left;
    Node right;

    public Node(String val){
        this.value = val;
        left = null;
        right = null;
    }

    public void setLeft(Node l){
        left = l;
    }

    public void setRight(Node r){
        right = r;
    }

    public String getValue(){
        return value;
    }

    public void print(){
        System.out.println("--------------------------------");
        System.out.println("Node value:" + value + " ref: "+this);
        if(left!=null){
            System.out.println("Left value:" + left.value+ " ref: "+left);
        }
        else{
            System.out.println("Left value: null");
        }
        if(right != null){
            System.out.println("Right value:" + right.value+ " ref: "+right);
        }
        else{
            System.out.println("Left value: null");
        }
        //System.out.println("Node value:" + value + " Left: " + left.value + " Right: " + right.value);
        System.out.println("--------------------------------");
    }
}