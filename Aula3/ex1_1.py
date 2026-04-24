'''Exercício 1
– Create a function checkPalindrome that given the
string, check if it is a palindrome.
– Example
• For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
• For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
• For inputString = "a", the output should be
checkPalindrome(inputString) = true.'''

print("Digite uma palavra")
palavra = input()

def checkPalindrome (palavra):
   if palavra == palavra[::-1]:
        print("A palavra é palíndrome")
   else:
        print("A palavra recebida não é palíndrome")

checkPalindrome(palavra)
