count = 1
i = ''
with open("wordlist.txt", "r") as list_file:
  
   for word in list_file.read():
      count = count +1
      i = word
      if word == "better":
        
         break
   print( f'I have found {i} on  number {count}')

 
 



    

