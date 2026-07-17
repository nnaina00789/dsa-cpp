# s=input("ENTER A STRING: ")
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.swapcase())
# .........................................................................
# def swap_case(s):
#     result=""
#     for ch in s:
#         if ch.islower():
#             result+=ch.upper()
#         elif ch.isupper():
#             result+=ch.lower()
#         else:
#             result+=ch
#     return result
# print(swap_case("Hello World! 132"))
# ........................................................
# def swap_case(s):
#     result=""
#     for ch in s:
#         if 'a'<=ch<='z':
#             result+=chr(ord(ch)-32)
#         elif 'A'<=ch<='Z':
#             result+=chr(ord(ch)+32)
#         else:
#             result+=ch
#     return result
# print(swap_case("Hello World! 132"))
# ........................................................

# import string
# s='Hello World!@#$%% 132'
# print(string.punctuation)
# print("..................")
# result=""
# for ch in s:
#     if ch not in string.punctuation:
#         result+=ch
# print(result)

#..........................................................
# import string 
# s="Hello, World! How are you? Fine."
# result="".join(ch for ch in s if ch not in string.punctuation)
# print(result)
#.........................................................
# s="naina khushi sona"
# words=s.split(" ",4)
# print(words)
#..................................................
# lst=[1,2,3,4,6,3,1,2,3]
# print(list(dict.fromkeys(lst)))
# print(list(set(lst)))
# ................................................


