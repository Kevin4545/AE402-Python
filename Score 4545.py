Math=input("請輸入數學成績")
Math=int(Math)
English=input("請輸入成績")
English=int(English)
if (Math >= 90 and English >= 90):
    print("get reaward")
 elif (Math>=60 and English>=60):
     print("get punish")
else (Math<=60 and English<=60):
    print("study more")