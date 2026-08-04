#1.	Python Program to Append Data to Existing File and Display the Entire File
#Step 1: Define the file name using a variable.
#Step 2: Take input from the user to append to the file.
#Step 3: Open the file in append mode ('a') so existing content is preserved and new content is added.
#Step 4: After writing, open the file in read mode ('r') to display its full content.

#Python Code:
# Step 1: Define file name
file_name = "example.txt"

# Step 2: Take input from user to append
data_to_append = input("Enter text to append to the file: ")

# Step 3: Open file in append mode and write the data
with open(file_name, "a") as file:
    file.write(data_to_append + "\n")

# Step 4: Read and display the entire file content
print("\nContents of the file after appending:")
with open(file_name, "r") as file:
    content = file.read()
    print(content)
