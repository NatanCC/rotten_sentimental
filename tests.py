from app import analyze_file



results = analyze_file("tests/input.txt")

with open("tests/classified.txt", 'r') as input:
        classified = input.read().splitlines()
    
        
print results
print classified


            