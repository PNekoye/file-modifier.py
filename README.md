# file-modifier.py
# File Modifier Program

A Python program that reads a text file, modifies its content, and writes the result to a new file with comprehensive error handling.

## Features

- Reads content from a user-specified text file
- Applies several modifications to the content:
  - Converts text to uppercase
  - Adds line numbers to each line
  - Adds header and footer sections
- Writes the modified content to a new file
- Implements robust error handling for various file operations
- Provides clear user feedback throughout the process

## Requirements

- Python 3.x

## Usage

1. Run the program:
   ```
   python file_modifier.py
   ```

2. When prompted, enter the name of the file you want to read
   - The file must exist and be readable
   - Enter 'exit' to quit the program

3. If the file is successfully read, the program will modify its content

4. Enter a name for the output file where the modified content will be saved

5. Choose whether to process another file or exit the program

## Error Handling

The program handles several types of errors:

- **FileNotFoundError**: When the specified input file doesn't exist
- **PermissionError**: When the user doesn't have permission to read the input file or write to the output file
- **IOError**: For other input/output errors that might occur during file operations

## Example Usage

```
File Modifier Program
---------------------
This program reads a text file, modifies its content, and writes the result to a new file.

Enter the name of the file to read (or 'exit' to quit): sample.txt
Successfully read file 'sample.txt' (152 characters)
Content modified (267 characters)
Enter the name for the modified file: modified_sample.txt
Successfully wrote modified content to 'modified_sample.txt'

Would you like to process another file? (y/n): n
Exiting program. Goodbye!
```

## Example of Modifications

### Original Content (sample.txt):
```
Hello, world!
This is a sample text file.
It contains multiple lines.
The program will modify this content.
```

### Modified Content (modified_sample.txt):
```
==================================================
MODIFIED FILE CONTENT
==================================================

1. HELLO, WORLD!
2. THIS IS A SAMPLE TEXT FILE.
3. IT CONTAINS MULTIPLE LINES.
4. THE PROGRAM WILL MODIFY THIS CONTENT.

==================================================
END OF MODIFIED CONTENT
==================================================
```

## Functions

### `read_file(filename)`
Reads content from a file and returns it as a string.

### `write_file(filename, content)`
Writes content to a file.

### `modify_content(content)`
Applies transformations to the content, including converting to uppercase, adding line numbers, and adding header/footer.

### `main()`
Controls the program flow, handles user interaction, and manages error handling.

## License

Free to use and modify.

## Author

[Purity Nekoye]