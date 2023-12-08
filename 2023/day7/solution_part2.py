import copy

class CardConvert:
    CARDCONV = {
        "A" : 13,
        "K" : 12,
        "Q" : 11,
        "J" : 10,
        "T" : 9,
        "9" : 8,
        "8" : 7,
        "7" : 6,
        "6" : 5,
        "5" : 4,
        "4" : 3,
        "3" : 2,
        "2" : 1,
        "J": 0}
    
    FIVE_OF_KIND = {"check": [5], "value": 6}
    FOUR_OF_KIND = {"check": [4,1], "value": 5}
    FULL_HOUSE = {"check": [3,2], "value": 4}
    THREE_OF_KIND= {"check": [3, 1, 1], "value": 3}
    TWO_PAIR = {"check": [2, 2, 1], "value": 2}
    ONE_PAIR = {"check": [2, 1, 1, 1], "value": 1}
    HIGH_CARD= {"check": [1, 1, 1, 1, 1], "value": 0}

    CHECK = [FIVE_OF_KIND, FOUR_OF_KIND, FULL_HOUSE, THREE_OF_KIND, TWO_PAIR, ONE_PAIR, HIGH_CARD]

class Hand():

    def __init__(self, cards:str, bid:int) -> None:
        self.cards = cards
        self.bid = bid
        self.rank()

    def display(self):
        print("cards: ", self.cards)
        print("bid: ", self.bid)
        print("rank", self.rank_)

    def rank(self):
        tmp = copy.copy(self.cards)
        remove_index = []
        index = 0
        store = []
        number_of_j = tmp.count("J")
        tmp = tmp.replace("J", "")

        if number_of_j==5:
            self.rank_ = CardConvert.FIVE_OF_KIND["value"]
            return

        while(len(tmp)):
            remove_char = tmp[0]
            num_of_char = tmp.count(tmp[0])
            store.append(num_of_char)

            if len(tmp)>1:
                #remove character
                tmp = tmp.replace(remove_char, "")
            else:
                tmp = ""

        store.sort(reverse=True)

        #add J to the output
        store[0]+=number_of_j

        for check in CardConvert.CHECK:
            if store == check["check"]:
                self.rank_ = check["value"]
                return

    def compare(self, h)->bool:
        if self.rank_> h.rank_:
            return True
        elif self.rank_ == h.rank_:
            for i in range(len(self.cards)):
                if CardConvert.CARDCONV[self.cards[i]]>CardConvert.CARDCONV[h.cards[i]]:
                    return True
                elif CardConvert.CARDCONV[self.cards[i]]==CardConvert.CARDCONV[h.cards[i]]:
                    pass
                else:
                    return False
        return False

class Solver:
    def __init__(self) -> None:
        self.hands = []

    def add(self, h:Hand):
        self.hands.append(h)

    def display(self):
        for i in self.hands:
            i.display()


    def sort(self):
        for i in range(len(self.hands)):
            tmp = None
            for j in range(0, len(self.hands)-i - 1):
                #self.hands[j].display()
                #self.hands[j+1].display()
                if self.hands[j].compare(self.hands[j+1]):
                    tmp = self.hands[j]
                    self.hands[j] = self.hands[j+1]
                    self.hands[j+1] = tmp
    
    def calulcate_result(self):
        ret = 0
        index = 1
        for i in self.hands:
            ret += index*i.bid
            index+=1
        return ret

    def parse(self, file_path):
        with open(file_path) as file:
            lines = file.readlines()

        times = []
        distances = []

        for line in lines:
            tmp = line.split(" ")
            if line == "\n":
                continue
            h = Hand(tmp[0], int(tmp[1].strip()))
            self.add(h)

        self.sort()
        self.display()

        print("Final result: ", self.calulcate_result())

def solve(file_path):
    s = Solver()
    s.parse(file_path)

solve("test_input.txt")