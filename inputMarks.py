def inputMarksFromUser():
   print("\n\n")
   print("***************************************************")
   studentName = input("Enter Student Name: ")
   
   rollno = 0
   while (rollno == 0):
      try:
         print("\n")
         rollno = int(input("Enter Student Roll No.: "))
      except ValueError:
         print("❌ Invalid Input, Please Enter A Number: ")
         print("\n")

   subjects = input("Enter List Of Subjects Seperated By Space: ").split(" ")
   print("***************************************************")
   print("Enter Marks For Each Subject: ")
   print("\n")
   marks = {}

   for sub in subjects:
      while True:
         try:
               mark = int(input(f"Enter Marks For {sub}: "))
               if 0 <= mark <= 100:
                  marks[sub] = mark
                  break
               else:
                  print("❌ Marks must be between 0 and 100. Try again.")
         except ValueError:
               print("❌ Invalid input. Please enter a number.")


   print("\n\n")
   return rollno, marks
