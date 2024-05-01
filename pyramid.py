def Solution(symbol,num):
    if not symbol:
        raise ValueError("Pleas provide a symbol")
    if  num %2 == 0:
        raise ValueError("Please provide an odd number")
    
    pyramid = []
    width = 1
    
    for i in range(1,num+1, 2):
        row = symbol * width
        pyramid.append(row.center(num," "))
        width += 2
        
    return print_pyramid(pyramid)
    
    pass

def print_pyramid(pyramid):
    for row in pyramid:
        print(row)
    
def main(symbol,num):
    Solution(symbol=symbol, num=num)
    
if __name__ == "__main__":
    symbol = input("enter a symbol: ")
    num = int(input("enter an odd number"))
    print(Solution(symbol=symbol, num=num))