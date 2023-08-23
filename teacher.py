try:
    s=input().split()
    if len(s)>0:
        large=s[0]
        for i in range(len(s)):
            if len(s[i])>len(large):
                large=s[i]
        print(len(large))
    else:
        print("Invalid Input")
except EOFError:
    print("Invalid Input")





"""An English school teacher is teaching how to build sentences for kindergarten students. She starts by teaching two words in a sentence, then 3 words and so on. The next step is that she asks the students to find which word in the sentence they have made has the maximum number of alphabets. The task here is to write program to find the longest word in each input sentence(str).
Note :
The sentence can consist of uppercase, lowercase alphabets, special characters and numbers. Sentence need not end with a '.' symbol.
The output should be a positive integer number which represents the length of the longest word in the sentence.
If the input is an empty string print "Invalid Input"."""