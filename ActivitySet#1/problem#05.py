# Functions

def computepay(h, r):
    if(rate<=40): p = r
    else: p=h/2 
    return p            
hrs = float(input("Enter Hours:"))
rate= float(input("Enter rate:"))
p = computepay(hrs,rate)
print("Pay", p)