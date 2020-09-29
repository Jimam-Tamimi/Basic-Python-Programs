# Program to fine a word from a given path of a file
try:
    file_path = input("Enter the file path: ")
    word = input("Enter a word to find: ")
    with open(file_path, 'r') as f:
        data = f.read()

    if word in data:
        print(f'{word} is available.')

    else:
        print(f'{word} is not available.')
except Exception as e:
    print(e)

