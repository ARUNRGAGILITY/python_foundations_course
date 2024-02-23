import streamlit as st
import os
import time
def list_markdown_files(startpath):
    """
    Lists all Markdown files in the specified directory and its subdirectories.

    Parameters:
    - startpath: str, the root directory to start searching from.

    Returns:
    - dict, a dictionary where keys are directory paths and values are lists of Markdown file paths.
    """
    markdown_files = {}
    for root, dirs, files in os.walk(startpath):
        markdown_paths = [os.path.join(root, file) for file in files if file.endswith('.md')]
        if markdown_paths:
            relative_root = os.path.relpath(root, startpath)
            markdown_files[relative_root] = markdown_paths
    return markdown_files

def main():
    # Base directory for modules
    modules_dir = "pfs/modules"
    
    # Normalize and construct absolute path
    modules_path = os.path.normpath(os.path.join(os.path.dirname(__file__), modules_dir))
    
    # List all Markdown files
    markdown_files = list_markdown_files(modules_path)
    
    # Sidebar - select a module directory
    selected_dir = st.sidebar.selectbox("Select a module:", options=list(markdown_files.keys()))
    
    # Sidebar - select a file within the selected directory
    if selected_dir:
        selected_file = st.sidebar.selectbox("Select a file:", options=markdown_files[selected_dir])
        
        # Display the selected Markdown file content
        if selected_file:
            file_content = load_markdown_file(selected_file)
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
