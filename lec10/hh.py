#Q>write a funtion to print the length and print the longest word of the given sentence.

s="First Programe for even coder is Hello World Language"

clean_s=s.strip()

def max_len_str(str1):
    max_len=0
    slist=str1.split()
    for i in range(len(slist)):
        if len(slist[i])>max_len:
            max_len=len(slist[i])
    return max_len

print(max_len_str(clean_s))

#q>write a function to calculate the no. of 1.vowels 2.consonants 3. digits 4. special characters 5.spaces.++=