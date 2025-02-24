from math import pi

def area(flag, d1, d2):
    if flag == "c":
        return pi * d1 * d1
    elif flag == "r":
        return d1 * d2 
    elif flag == "t":
        return (d1 * d2) / 2 
    else:
        return "Invalid shape flag!"

def main():
    data = input("Enter data in this format (shape flag, dimension1, dimension2): ")
    data = [x.strip().lower() for x in data.split(",")]  
    if len(data) < 2:
        print("[!] Invalid input. Please provide at least a shape and one dimension.")
        return
    
    flag = data[0]
    
    try:
        d1 = float(data[1])
        d2 = float(data[2]) if len(data) > 2 else 0  
        print(f"Ans: {area(flag, d1, d2)}")
    except ValueError:
        print("[!] Invalid number format. Please enter numeric values for dimensions.")

main()
