from app import analyze_file

results = []
#results = analyze_file("tests/test_input.txt")
#results = ["positivo"] * 10

if results:
    with open("tests/test_results.txt", 'w') as f:
        for result in results:
            f.write(result + "\n")

with open("tests/test_classified.txt", 'r') as input:
        classified = input.read().splitlines()
        
with open("tests/test_results.txt", 'r') as input:
        results = input.read().splitlines()
    

   
   
#TODO
#Comparar e fazer matriz de confusao     
print results
print classified

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

            