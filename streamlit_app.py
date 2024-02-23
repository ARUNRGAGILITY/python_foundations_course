import streamlit as st
import os

def list_markdown_files(startpath):
    """
    Lists all Markdown files in the specified directory and its subdirectories, organized by directory.

    Parameters:
    - startpath: str, the root directory to start searching from.

    Returns:
    - dict, a nested dictionary where keys are directory paths and values are dictionaries mapping filenames to their full paths.
    """
    markdown_files = {}
    for root, dirs, files in os.walk(startpath):
        markdown_paths = {file: os.path.join(root, file) for file in files if file.endswith('.md')}
        if markdown_paths:
            relative_root = os.path.relpath(root, startpath)
            markdown_files[relative_root] = markdown_paths
    return markdown_files

def main():
    # Base directory for modules
    modules_dir = "Learning/Basics"
    
    # Normalize and construct absolute path
    modules_path = os.path.normpath(os.path.join(os.path.dirname(__file__), modules_dir))
    
    # List all Markdown files
    markdown_files = list_markdown_files(modules_path)
    
    # Sort directories by their prefix numbers
    sorted_dirs = sorted(markdown_files.keys(), key=lambda x: [int(part) if part.isdigit() else part for part in x.split('/')])
    
    # Sidebar - select a module directory
    selected_dir = st.sidebar.selectbox("Select a module:", options=sorted_dirs)
    
    # Sidebar - select a file within the selected directory
    if selected_dir:
        # Get filenames (keys) and sort them by their prefix numbers
        filenames = sorted(markdown_files[selected_dir].keys(), key=lambda x: [int(part) if part.isdigit() else part for part in x.split('_')])
        selected_filename = st.sidebar.selectbox("Select a file:", options=filenames)
        
        # Find the full path of the selected file
        if selected_filename:
            selected_file_path = markdown_files[selected_dir][selected_filename]
            file_content = load_markdown_file(selected_file_path)
            st.markdown(file_content, unsafe_allow_html=True)

def load_markdown_file(markdown_file_path):
    """
    Reads a Markdown file and returns the content as a string.

    Parameters:
    - markdown_file_path: str, path to the Markdown file.

    Returns:
    - str, content of the Markdown file.
    """
    with open(markdown_file_path, "r", encoding="utf-8") as file:
        return file.read()

if __name__ == "__main__":
    main()
