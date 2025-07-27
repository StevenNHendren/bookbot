def count_words(s):
    allwords = s.split()
    return len(allwords)

def count_characters(s):
    chars = set()
    char_counts_dict = {}
    for c in s:
        c = c.lower()
        if c in chars:
            char_counts_dict[c] += 1
        else:
            chars.add(c)
            char_counts_dict[c] = 1
    return char_counts_dict    

def sort_on(mycharacters):
    return mycharacters['count']

def sort_char_dict(c_c_dict):
    
    sorted_dictionary = list()
    for letter, count in c_c_dict.items():
        if letter.isalpha():
            char_dict_entry ={"character": letter, "count": int(count)} 
            sorted_dictionary.append(char_dict_entry)
    sorted_dictionary.sort(reverse=True, key=sort_on)
    return sorted_dictionary