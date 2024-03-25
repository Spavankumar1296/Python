def Anagram(s1,s2):
    l1=list(s1);
    l1.sort();
    l2=list(s2)
    l2.sort()
    if(l1==l2):
        print("string are anagram")
    else:
        print("the strings are not anagram")
Anagram(input("enter the string-1 : "),input("enter the string-2 : "))