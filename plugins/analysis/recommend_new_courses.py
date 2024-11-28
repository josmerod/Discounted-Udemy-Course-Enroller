import pandas as pd
import re
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process  

# Load the CSV file and Markdown file paths
csv_file_path = '../../Extras/CourseLists/CourseList-2024-11-28--03-00.csv'
markdown_file_path = '../../Extras/AuxFiles/Udemy.md'

# Read the CSV file with the list of courses
course_df = pd.read_csv(csv_file_path)

# Read the Markdown file to extract the categories
with open(markdown_file_path, 'r', encoding='utf-8') as f:
    markdown_content = f.readlines()

# Extract categories from the Markdown file
def extract_categories(markdown_lines):
    categories = []
    for line in markdown_lines:
        if line.startswith('##### '):
            category = line.strip().replace('##### ', '')
            categories.append(category)
        elif line.startswith('#### '):
            category = line.strip().replace('#### ', '')
            categories.append(category)
    return categories

categories = extract_categories(markdown_content)

# Use fuzzy matching to find similar courses
filtered_courses = {}
threshold = 50  # Set a higher threshold for more precise fuzzy matching
for category in categories:
    matches = course_df['name'].apply(lambda x: fuzz.partial_ratio(category.lower(), x.lower()))
    filtered_courses[category] = course_df[matches >= threshold]

# Display filtered courses for each category
for category, df in filtered_courses.items():
    if not df.empty:
        print(f"\nRecommended courses for category: {category}")
        print(df[['name', 'url']])

# Create a DataFrame to store the filtered courses by category for export
export_data = []

# Collect all filtered courses with their categories
for category, df in filtered_courses.items():
    if not df.empty:
        export_data.extend([[category, row['name'], row['url']] for _, row in df.iterrows()])

# Create a DataFrame for export
export_df = pd.DataFrame(export_data, columns=['Category', 'Course Name', 'URL'])

# Remove any duplicates from the export DataFrame (same course in multiple categories, via same url or name)
export_df.drop_duplicates(subset=['Course Name', 'URL'], inplace=True)

# Check if the folder exists, if not, create it
folder_path = "../../Extras/CourseRecommendations"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Get the current timestamp for the export filename, formatted as 'YYYY-MM-DD--HH-MM'
currentTime = pd.Timestamp.now().strftime("%Y-%m-%d--%H-%M")

# Save the recommendations to a CSV file
export_file_path = folder_path + "/course_recommendations_filtered" + currentTime + ".csv"
export_df.to_csv(export_file_path, index=False)

print(f"Recommendations exported to: {export_file_path}")
