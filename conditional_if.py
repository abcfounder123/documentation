
"""

Day.7 + 8

12. if 

ချိတ်ဆက်ထားတဲ့ condition မှန်ရင် အလုပ်လုပ်သည်။

#####################################

mark = int(input("Marks = "))

if mark >= 40:
    print("Exam pass.")

#####################################


13. else

ချိတ်ဆက်ထားတဲ့ condition မှားရင် အလုပ်လုပ်သည်။

#####################################

mark = int(input("Marks = "))

if mark >= 40:
    print("Exam pass.")

else:
    print("Exam fail."
    
#####################################
    
mark = int(input("Marks = "))

c1 = mark >= 40

if c1:
    print("Exam pass.")

else:
    print("Exam fail.")
      
#####################################

14. all from all

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

if c2: print("Programmer.")

if c3: print("Engineer.")

if c4: print("Distance.")

#####################################

15. one from all

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

if not c1 and c2: print("Programmer.")

if not c1 and not c2 and c3: print("Engineer.")

if not c1 and not c2 and not c3 and c4: print("Distance.")

#####################################

16. one from all by Python ( elif ) ( else + if )

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

elif c2: print("Programmer.")

elif c3: print("Engineer.")

elif c4: print("Distance.")

#####################################

17. if + elif + else

if not c1 and not c2 and not c3 and not c4: print("Grade 12.")

#####################################

mark = int(input("Marks = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

elif c2: print("Programmer.")

elif c3: print("Engineer.")

elif c4: print("Distance.")

else: print("Grade 12.")

#####################################

"""



