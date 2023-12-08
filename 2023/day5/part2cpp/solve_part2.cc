#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <limits>
#include <thread>
#include <mutex>


#include <chrono>


using namespace std;

#define NUM_OF_CATEGORY 7

class Converter{

    public:
    Converter();
    void parse(string filePath);
    void print();
    void printVector(vector<unsigned long long>);
    unsigned long long convert(unsigned long long& inputData);
    vector<unsigned long long>& getInp();

    mutex retMutex;

    private:
    void parseData(string line, vector<unsigned long long>& v);


    bool readSeed = true;
    vector<unsigned long long> inp;
    vector<vector<unsigned long long>> converterRanges;
    int convertIndex = 0;
    const string SEED_TO_SOIL = "seed-to-soil map:";
    const string SOIL_TO_FERT = "soil-to-fertilizer map:";
    const string FERT_TO_WATER = "fertilizer-to-water map:";
    const string WATER_TO_LIGHT = "water-to-light map:";
    const string LIGHT_TO_TEMP = "light-to-temperature map:";
    const string TEMP_TO_HUM = "temperature-to-humidity map:";
    const string HUM_TO_LOC = "humidity-to-location map:";
    const string LEADING_LINES[NUM_OF_CATEGORY] = {SEED_TO_SOIL, SOIL_TO_FERT, FERT_TO_WATER, WATER_TO_LIGHT, LIGHT_TO_TEMP, TEMP_TO_HUM, HUM_TO_LOC};
     // Mutex a ret változó védelmére
};

Converter::Converter(){
    for(auto i =0; i<NUM_OF_CATEGORY; i++){
        vector<unsigned long long> temp;
        converterRanges.push_back(temp);
    }
}

void Converter::print(){
    cout<<"----------------Print converter start:----------------"<<endl;
    cout<<"inp: ";
    this->printVector(inp);

    for(auto i =0 ; i<NUM_OF_CATEGORY; i++){
        this->printVector(converterRanges[i]);
    }

    cout<<"----------------Print converter end:----------------"<<endl;

}

void Converter::printVector(vector<unsigned long long> v){
    cout <<" Vector: ";
    for(auto i: v){
        cout << i<< " ";
    }
    cout<<endl;
}

void Converter::parse(string filePath){
    fstream new_file;
    new_file.open(filePath, ios::in);

    if (new_file.is_open()) {
        string line;
        while (getline(new_file, line)) {

            //cout<<" the string is: "<<line<<endl;

            if(line==""){
                //skip empty line
                continue;
            }

            if (line  == LEADING_LINES[convertIndex])
            {
                this->readSeed = false;
                this->convertIndex++;
                continue;
            }

            if(this->readSeed){
                this->parseData(line, this->inp);
            }
            else{
                //-1 is needed (forward testing)
                this->parseData(line, this->converterRanges[convertIndex-1]);
            }

        }
        new_file.close();
    }
    //this->print();
}

void Converter::parseData(string line, vector<unsigned long long>& v){
    unsigned long long number = 0;
    bool conversionStarted = false;
    for(auto c: line){
        if(isdigit(c)){
            conversionStarted = true;
            int x = c - '0';  // The (int) cast is not necessary.
            number = number*10 + x;
        }
        else{
            if(conversionStarted){
                v.push_back(number);
                number = 0;
                conversionStarted = false;
            }
        }
    }
    if(conversionStarted){
        v.push_back(number);
    }
}


unsigned long long Converter::convert(unsigned long long& inputData){
    //cout<<"Convert value: "<<inputData<< " ->";
    unsigned long long ret = inputData;
    unsigned long long prev = ret;
    bool isConverted = false;
    for(auto i =0 ; i<NUM_OF_CATEGORY; i++){
        for(auto j = 0; j<converterRanges[i].size(); j=j+3){
            if(ret>=converterRanges[i][j+1] &&
            (ret< (converterRanges[i][j+1]+converterRanges[i][j+2]))){
                long long dist_from_start = ret - converterRanges[i][j+1];
                prev =ret;
                ret = converterRanges[i][j] + dist_from_start;
                //cout<<"["<<converterRanges[i][j]<<" "<<converterRanges[i][j+1]<<" "<<converterRanges[i][j+2]<<"]";
                break;
                //return ret;
                
            }
        }
        //cout<<ret<<"-> ";
    }
    //cout<<endl;
    //if(ret == 79004095){
    //    cout<<"ttttt:"<<prev<<endl;
    //    cout<<"tt: "<<inputData<<endl;
    //}
    return ret;
}

vector<unsigned long long>& Converter::getInp(){
    return inp;
}


void solve(string fileName){
    Converter c;
    c.parse(fileName);
    unsigned long long ret = (unsigned long long) -1;

    vector<unsigned long long> inp = c.getInp();

    for(int i = 0; i<inp.size(); i= i+2){
        cout<<i<<"/"<<inp.size()<<endl;
        for(unsigned long long j = inp[i]; j<inp[i]+inp[i+1]; j++){
            unsigned long long temp = c.convert(j);
            if(temp<ret){
                ret = temp;
            }
        }
    }


    cout<<"The result: "<<endl;
    cout<<ret;

}


void parallelProcess(Converter& c, unsigned long long start, unsigned long long end, unsigned long long& ret) {
    for (unsigned long long j = start; j < end; j++) {
        unsigned long long temp = c.convert(j);
        lock_guard<mutex> lock(c.retMutex);  // Automatikus lock és unlock a mutex-szal
        if (temp < ret) {
            ret = temp;
        }
    }
}

void solveParallel(string fileName) {
    Converter c;
    c.parse(fileName);
    unsigned long long ret = numeric_limits<unsigned long long>::max();

    vector<unsigned long long> inp = c.getInp();

    vector<thread> threads;
    const int numThreads = 100;  // Adjust the number of threads as needed

    for (int i = 0; i < inp.size(); i += 2) {
        cout << i << "/" << inp.size() << endl;
        for (int t = 0; t < numThreads; ++t) {
            unsigned long long start = inp[i] + (t * (inp[i + 1] / numThreads));
            unsigned long long end = inp[i] + ((t + 1) * (inp[i + 1] / numThreads));
            threads.emplace_back(parallelProcess, ref(c), start, end, ref(ret));
            //cout << "thread started: "<<t<<endl;
        }

        for (auto& thread : threads) {
            thread.join();
        }
        threads.clear();
    }

    cout << "The result: " << endl;
    cout << ret;
}

int main(){
    auto start = std::chrono::high_resolution_clock::now();
    //solve("test_input.txt");
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    std::cout << "Execution time: " << duration.count() << " seconds." << std::endl;


    start = std::chrono::high_resolution_clock::now();
    solveParallel("test_input.txt");
    end = std::chrono::high_resolution_clock::now();
    duration = end - start;
    std::cout << "Execution time: " << duration.count() << " seconds." << std::endl;
}


//79004095, original
//566984172, 1138901055, 540622614, 79004095
//seeds: 2302307275 10