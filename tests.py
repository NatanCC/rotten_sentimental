from app import analyze_file



results = analyze_file("tests/input.txt")

with open("tests/classified.txt", 'r') as input:
        classified = input.read().splitlines()
    
   
   
#TODO
#Comparar e fazer matriz de confusao     
print results
print classified


            