#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <fstream>

using namespace std;

//vector<int> split_by_whitespace(string &substring)

class Parser{
    string* winningNumbers;
    string* numbersYouHave;
    vector<int> winningNumbersConverted;
    vector<int> yourNumbersConverted;

    void getWinning_numbers();
    void getYour_numbers();

    public:
        Parser(string& winningNumbers, string& numbersYouHave);
        void printInput();

        int solve();


};

Parser::Parser(string& winningNumbers, string& numbersYouHave){
    this->winningNumbers = &winningNumbers;
    this->numbersYouHave = &numbersYouHave;
    this->getWinning_numbers();
    this -> getYour_numbers();
}

void Parser::printInput(){
    cout<<"Winnig numbers: "<< *(this->winningNumbers)<<endl;
    cout<<"Your numbers: "<< *(this->numbersYouHave)<<endl;

    cout<<"Winning numbers converted: ";
    for(auto i: this->winningNumbersConverted){
        cout<<i<<" ";
    }
    cout<< endl;

    cout<<"Your numbers converted: ";
    for(auto i: this->yourNumbersConverted){
        cout<<i<<" ";
    }
    cout<< endl;
}


void Parser::getWinning_numbers(){
    int number = 0;
    bool numberStart = false;
    for(auto c: *(this->winningNumbers)){
        if (c != ' '){
            int x = c - '0';  // The (int) cast is not necessary.
            number = number*10 + x;
            numberStart = true;
        }
        if(c ==' ' && numberStart){
            this->winningNumbersConverted.push_back(number);
            number =0;
            numberStart = false;
        }
    }
}

void Parser::getYour_numbers(){
    int number = 0;
    bool numberStart = false;
    for(auto c: *(this->numbersYouHave)){
        if (c != ' '){
            int x = c - '0';  // The (int) cast is not necessary.
            number = number*10 + x;
            numberStart = true;
        }
        if(c ==' ' && numberStart){
            this->yourNumbersConverted.push_back(number);
            number =0;
            numberStart = false;
        }
    }
    if(numberStart){
        this->yourNumbersConverted.push_back(number);
    }
}

int Parser::solve(){
    int ret = 0;
    bool isFirst = true;
    for(auto i: this->yourNumbersConverted){

        
        if (std::count(this->winningNumbersConverted.begin(), this->winningNumbersConverted.end(), i)) {
            if(isFirst){
                ret = 1;
                isFirst = false;
            }
            else{
                ret = ret*2;
            }
        }
    }
    return ret;
}

int solveLine(string &line){
    int index = 0;
    int size = line.length();

    int winningNumberStartIndex = size;
    int winningNumberEndIndex = size;
    int numberYouHaveStartIndex = size;
    
    string winningNumbers = "";
    string yourNumbers = "";

    for(auto c: line){
        if(c == ':'){
            winningNumberStartIndex = index+2;
        }

        if(c=='|'){
            winningNumberEndIndex = index -2;
            numberYouHaveStartIndex = index +2;
        }

        if (index>=winningNumberStartIndex && index<=winningNumberEndIndex){
            winningNumbers = winningNumbers+c;
        }

        if (index>=numberYouHaveStartIndex){
            yourNumbers = yourNumbers+c;
        }

        index++;
    }

    Parser p(winningNumbers, yourNumbers);
    //p.printInput();
    cout<<"Solution: "<<p.solve()<<endl;
    return p.solve();
}

vector<int> get_numbers_you_have(string line){
    vector<int> ret;
    return ret;
}

int solve(string fileName){
    int ret = 0;
    fstream new_file;
    new_file.open("test_input.txt", ios::in);

    if (new_file.is_open()) {
        string line;
        while (getline(new_file, line)) {
            // Print the data of the string.
            cout << line << endl;
            ret = ret + solveLine(line);
        }
        new_file.close();
    }


    return ret;
}

int main(){

    int sum  = solve("test_input.txt");

    cout<<"Final solution: "<<sum<<endl;
    return 0;
}