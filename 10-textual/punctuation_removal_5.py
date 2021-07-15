import re

# letters only
raw_text = "The cat sat on the mat. There were now 2 cats on the mat!!"
letters_only_text = re.sub(pattern='[^a-zA-Z]', repl=' ', string=raw_text)
print(letters_only_text)

# keep numbers
letters_and_numbers_text = re.sub('[^a-zA-Z0-9]', ' ', raw_text)
print(letters_and_numbers_text)
