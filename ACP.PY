with open('Codingal.txt','w')as file:
    file.write("Harry, Age:8 Fav subject: English  Peter, Age:9 ,Fav subject:Maths  Sara, Age:8, Fav subject: Science")
    file.close()

with open('Codingal.txt','r')as file:
  data= file.readlines()
print("Words in this file are....")
for line in data:
    word= line.split()
    print(word)
    file.close()