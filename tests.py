from app import Analyzer

analyzer = Analyzer()

results = []
results = analyzer.analyze_file("tests/test_input.txt")


with open("tests/test_classified.txt", 'r') as input:
        classified = input.read().splitlines()

    


print results
print classified
print

def confusion_matrix(results, classified):
    pos_pos = 0
    pos_neu = 0
    pos_neg = 0
    neu_pos = 0
    neu_neu = 0
    neu_neg = 0
    neg_pos = 0
    neg_neu = 0
    neg_neg = 0
    
    for i in range(len(classified)):
        if classified[i] == "positivo":
            if results[i] == "positivo":
                pos_pos += 1
            elif results[i] == "neutro":
                pos_neu += 1
            else:
                pos_neg += 1
                
        elif classified[i] == "neutro":
            if results[i] == "positivo":
                neu_pos += 1
            elif results[i] == "neutro":
                neu_neu += 1
            else:
                neu_neg += 1
                
        else:
            if results[i] == "positivo":
                neg_pos += 1
            elif results[i] == "neutro":
                neg_neu += 1
            else:
                neg_neg += 1
            
    print str(pos_pos) + " " + str(pos_neu) + " " + str(pos_neg)  
    print str(neu_pos) + " " + str(neu_neu) + " " + str(neu_neg) 
    print str(neg_pos) + " " + str(neg_neu) + " " + str(neg_neg)
    
    return [pos_pos, pos_neu, pos_neg, neu_pos, neu_neu, neu_neg, neg_pos, neg_neu, neg_neg]      


confusion_matrix(results, classified)

            