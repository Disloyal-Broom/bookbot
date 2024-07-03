def main():
    path = "books/frankenstein.txt"
    content = open_file(path)
    words = count_words(content)
    char_list = count_chars(content)
    print_report(words,char_list,path)
    
def print_report(words, char_list, path):
    char_list = sorted(char_list, key=lambda x: x["char"])
    print(f"-- begin report of {path} --")
    print(f"There are {words} found in the document.")  
    for i in range(0, len(char_list)-1, 1):
        print(f"{char_list[i]["char"]}: {char_list[i]["num"]}")
    
def count_chars(words):
    char_dict = {}
    char_list = []
    words = words.lower()
    
    for chars in words:    
        if chars.isalpha():
            if chars not in char_dict:
                char_dict[chars] = 1
            else:
                char_dict[chars] += 1
    
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    
    return char_list
    
def open_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

main()