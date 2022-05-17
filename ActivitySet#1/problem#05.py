# Functions

def computepay(h, r):
    if(h<=40): p = h*r
    else: p=(h-40)*(r*1.5)+(40*r)
    return p            
hrs = float(input("Enter Hours:"))
rate= float(input("Enter rate:"))
p = computepay(hrs,rate)
print("Pay", p)