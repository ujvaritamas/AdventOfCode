#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

#include <fstream>
#include <cctype>

using namespace std;

//vector<int> split_by_whitespace(string &substring)

class Card{
    string* winningNumbers;
    string* numbersYouHave;
    vector<int> winningNumbersConverted;
    vector<int> yourNumbersConverted;
    int cardNumber;
    int numberOfWinningCards = 0;

    void getWinning_numbers();
    void getYour_numbers();

    public:
        Card(string& winningNumbers, string& numbersYouHave, int& cardNumber);
        void printInput();

        int getNumberOfWinningCards();
        int getCardNumber(){
            return this->cardNumber;
        }

        int getnumberOfWinningCards(){
            return this->numberOfWinningCards;
        }

};

Card::Card(string& winningNumbers, string& numbersYouHave, int& cardNumber){
    this->winningNumbers = &winningNumbers;
    this->numbersYouHave = &numbersYouHave;
    this->cardNumber = cardNumber;
    this->getWinning_numbers();
    this -> getYour_numbers();
    this->numberOfWinningCards = this->getNumberOfWinningCards();
}

void Card::printInput(){
    cout<<"CardNUmber: "<<this->cardNumber<<endl;
    //cout<<"Winnig numbers: "<< *(this->winningNumbers)<<endl;
    //cout<<"Your numbers: "<< *(this->numbersYouHave)<<endl;

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
    cout<<"Number of winning cards: "<<this->numberOfWinningCards<<endl;
}


void Card::getWinning_numbers(){
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

void Card::getYour_numbers(){
    int number = 0;
    bool numberStart = false;
    for(auto c: *(this->numbersYouHave)){
        if (c != ' '){
            int x = c - '0';
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

int Card::getNumberOfWinningCards(){
    int ret = 0;
    for(auto i: this->yourNumbersConverted){
        if (std::count(this->winningNumbersConverted.begin(), this->winningNumbersConverted.end(), i)) {
            ret++;
        }
    }
    return ret;
}


class CardHandler{
    int actualCardNumber = 0;
    map<unsigned long long, unsigned long long> cardCopy;
    void setActialCardNumber(int actualCardNumber);
    public:
        unsigned long long game(Card& c);
};

void CardHandler::setActialCardNumber(int actualCardNumber){
    this->actualCardNumber = actualCardNumber;
}

unsigned long long CardHandler::game(Card& c){
    setActialCardNumber(c.getCardNumber());
    //copy + the current
    auto isAdded = this->cardCopy.count(this->actualCardNumber);
    unsigned long long winfactor;
    if(isAdded){
        //copy + the current
        winfactor = this->cardCopy[this->actualCardNumber] + 1;
    }
    else{
        //only the current
        winfactor = 1;
    }
    //int winfactor = this->cardCopy.count(c.getCardNumber()) + 1;
    cout<<" test: "<<cardCopy.count(c.getCardNumber())<<endl;
    

    unsigned long long numOfNewCards = c.getnumberOfWinningCards();

    while(numOfNewCards>0){
        unsigned long long index = this->actualCardNumber+numOfNewCards;
        cout<<"index: "<<index<<endl;
        if(this->cardCopy.count(index)){
            this->cardCopy[index] = this->cardCopy[index] + winfactor;
        }
        else{
            this->cardCopy[index] = winfactor;
        }
        --numOfNewCards;
    }

    if(isAdded){
        auto it = this->cardCopy.find(this->actualCardNumber);
        this->cardCopy.erase(it);
    }

    map<unsigned long long, unsigned long long>::iterator itr;
    cout<<"MAP: ";
    for(itr=cardCopy.begin();itr!=cardCopy.end();itr++)
    {
        cout<<itr->first<<" "<<itr->second<<" XX ";
    }
    cout<<endl;

    cout<<"Winfactor: "<<winfactor<<endl;
    return winfactor;
}



int solveLine(string &line, CardHandler& cardHandler){
    int index = 0;
    int size = line.length();

    int winningNumberStartIndex = size;
    int winningNumberEndIndex = size;
    int numberYouHaveStartIndex = size;

    int cardNumberStartIndex = size;
    int cardNumberEndIndex = size;
    int cardNumber = 0;
    
    string winningNumbers = "";
    string yourNumbers = "";

    for(auto c: line){
        if(cardNumberStartIndex == size && isdigit(c)){
            cardNumberStartIndex = index;
        }

        if(c == ':'){
            winningNumberStartIndex = index+2;
            cardNumberEndIndex = index -1;
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

        if(index>=cardNumberStartIndex && index<=cardNumberEndIndex){
            int x = c - '0';    //convert char to int
            cardNumber = cardNumber*10 +x;
        }

        index++;
    }

    Card p(winningNumbers, yourNumbers, cardNumber);
    p.printInput();

    //cardHandler.game(p);
    //cout<<"Solution: "<<p.solve()<<endl;
    return cardHandler.game(p);
}

vector<int> get_numbers_you_have(string line){
    vector<int> ret;
    return ret;
}

int solve(string fileName){
    int ret = 0;
    fstream new_file;
    new_file.open("test_input.txt", ios::in);

    CardHandler cardHandler;

    if (new_file.is_open()) {
        string line;
        while (getline(new_file, line)) {
            // Print the data of the string.
            cout<<"------------------------------------"<<endl;
            cout << line << endl;
            ret = ret + solveLine(line, cardHandler);
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