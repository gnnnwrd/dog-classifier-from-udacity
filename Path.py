file_path = "D:\learning_zone\Latihan Udacity_AI with Python\AIPND-revision-master\intropyproject-classify-pet-images\imagenet1000_clsid_to_human.txt"
try:
    with open(file_path, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError as e:
    print(f"Error opening file '{file_path}': {e}")
