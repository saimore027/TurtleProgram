import turtle

sai=turtle.Turtle()
turtle.speed(30)
def square():
    sai.forward(100)
    sai.right(90)
    sai.forward(100)
    sai.right(90)
    sai.forward(100)
    sai.right(90)
    sai.forward(100)
    
    

for i in range(10):
    square()
print(float(2))
string="Hello"
print(string[0])
print(string.lower())
print(string.replace("Hello"))
splitting=string.split(" ",4)
print(splitting)

name=["John" ,"sai" ,"shivam" ,"aniket"]
print(name)
name.append("gary")
print(name)

name.insert(0,"gary")
print(name)

    
