package com.example;

public interface ISolution {
    public void display();
    public void setData(String data);
    public void addConfigNumber(int n);
    public void addUnknownCharPosition(int pos);
    public int solve();
    public String manipulateLine(String line);
}
