import os
import pandas as pd

def courses_list_get_files():
    """
    Retrieve all text files from the 'Courses' directory that match the naming convention.
    File format: YYYY-MM-DD--HH-MM.txt (e.g., 2021-01-01--12-00.txt)

    Returns:
        list: A list of filenames ending with '.txt' in the 'Courses' directory.
    """
    files = []
    # Iterate over all files in the 'Courses' directory
    for file in os.listdir("../../Courses"):
        # Check if the file has a '.txt' extension
        if file.endswith(".txt"):  # Good enough...
            files.append(file)
    return files

def courses_list_load_files(files):
    """
    Read and aggregate data from the provided list of files.

    Args:
        files (list): A list of filenames to read from the 'Courses' directory.

    Returns:
        list: A list containing all lines from the files.
    """
    data = []
    # Process each file in the list
    for file in files:
        # Open the file with UTF-8 encoding to handle special characters
        with open(f"../../Courses/{file}", "r", encoding='utf-8') as f:
            lines = f.readlines()
            # Append each line to the data list
            for line in lines:
                data.append(line)
    return data

def courses_list_process_data(data):
    """
    Process raw data to extract course names and URLs, and set enrollment status.

    Args:
        data (list): A list of strings containing course information.

    Returns:
        list: A list of dictionaries with course details.
    """
    courses = []
    # Process each line in the data
    for line in data:
        # Split the line into course name and URL
        course = line.strip().split(" - ")
        # Create a dictionary for the course and add it to the list
        courses.append({
            "name": course[0],
            "url": course[1],
            "status": "Not Enrolled"
        })
    return courses

def format_courses_list(courses):
    """
    Convert the list of courses into a pandas DataFrame for better formatting.

    Args:
        courses (list): A list of dictionaries containing course details.

    Returns:
        DataFrame: A pandas DataFrame of the courses.
    """
    df = pd.DataFrame(courses)
    return df

def export_file(df):
    """
    Export the DataFrame to a CSV file with a timestamped filename.

    Args:
        df (DataFrame): The DataFrame to export.
    """
    # Get the current timestamp formatted for the filename
    timestamp = pd.Timestamp.now().strftime("%Y-%m-%d--%H-%M")
    # Save the DataFrame as a CSV file in the 'Extras/CourseLists' directory
    df.to_csv(f"../../Extras/CourseLists/CourseList-{timestamp}.csv", index=False, sep="|")

def main():
    """
    Main function to orchestrate the loading, processing, and exporting of course data.
    """
    # Get the list of course files
    files = courses_list_get_files()
    # Load data from the files
    data = courses_list_load_files(files)
    # Process the data into structured course information
    courses = courses_list_process_data(data)
    # Format the courses into a DataFrame
    df = format_courses_list(courses)
    # Ensure the output directories exist
    if not os.path.exists("../../Extras"):
        os.makedirs("../../Extras")
    if not os.path.exists("../../Extras/CourseLists"):
        os.makedirs("../../Extras/CourseLists")
    # Export the DataFrame to a CSV file
    export_file(df)

if __name__ == "__main__":
    main()