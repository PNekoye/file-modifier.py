"""
File Modifier Program

This program reads a text file, modifies its content, and writes the result to a new file.
It includes comprehensive error handling for various file operations.
"""

def read_file(filename):
    """
    Reads the content of a file and returns it as a string.
    
    Args:
        filename (str): The name of the file to read
        
    Returns:
        str: The content of the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        PermissionError: If the user doesn't have permission to read the file
        IOError: For other input/output errors
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        raise PermissionError(f"Error: You don't have permission to read '{filename}'.")
    except IOError as e:
        raise IOError(f"Error reading the file '{filename}': {str(e)}")

def write_file(filename, content):
    """
    Writes content to a file.
    
    Args:
        filename (str): The name of the file to write to
        content (str): The content to write to the file
        
    Raises:
        PermissionError: If the user doesn't have permission to write to the file
        IOError: For other input/output errors
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except PermissionError:
        raise PermissionError(f"Error: You don't have permission to write to '{filename}'.")
    except IOError as e:
        raise IOError(f"Error writing to the file '{filename}': {str(e)}")

def modify_content(content):
    """
    Modifies the content by applying several transformations.
    
    Args:
        content (str): The original content
        
    Returns:
        str: The modified content
    """
    # Convert to uppercase
    modified = content.upper()
    
    # Add line numbers
    lines = modified.split('\n')
    numbered_lines = [f"{i+1}. {line}" for i, line in enumerate(lines)]
    
    # Join lines back together
    modified = '\n'.join(numbered_lines)
    
    # Add header and footer
    header = "=" * 50 + "\nMODIFIED FILE CONTENT\n" + "=" * 50 + "\n\n"
    footer = "\n\n" + "=" * 50 + "\nEND OF MODIFIED CONTENT\n" + "=" * 50
    
    return header + modified + footer

def main():
    print("File Modifier Program")
    print("---------------------")
    print("This program reads a text file, modifies its content, and writes the result to a new file.\n")
    
    while True:
        # Get input file name from user
        input_file = input("Enter the name of the file to read (or 'exit' to quit): ")
        
        if input_file.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
        
        # Try to read the file
        try:
            content = read_file(input_file)
            print(f"Successfully read file '{input_file}' ({len(content)} characters)")
            
            # Modify the content
            modified_content = modify_content(content)
            print(f"Content modified ({len(modified_content)} characters)")
            
            # Get output file name
            output_file = input("Enter the name for the modified file: ")
            
            # Write to the output file
            write_file(output_file, modified_content)
            print(f"Successfully wrote modified content to '{output_file}'")
            
            # Ask if the user wants to process another file
            another = input("\nWould you like to process another file? (y/n): ")
            if another.lower() != 'y':
                print("Exiting program. Goodbye!")
                break
                
        except (FileNotFoundError, PermissionError, IOError) as e:
            print(str(e))
            print("Please try again with a different file.\n")

if __name__ == "__main__":
    main()