'''
# Problem : Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: 
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"


'''

def spin_words(sentence):
    
    #splitting into the words
    words = sentence.split(' ')
    new_sentence = '' 
    i=0
    while i != len(words):
        #Checking the length of each word from the list
        if len(words[i]) >= 5:
            new_sentence += words[i][::-1]
        else:
            new_sentence += words[i]
        
        new_sentence +=' ' #Adding spaces as it was before splitting
        
        i += 1
    return new_sentence[:len(new_sentence)-1]

print(spin_words( "Hey fellow warriors" ))