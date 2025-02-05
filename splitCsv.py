import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('song_lyrics.csv')

# Calculate the number of instances
num_instances = len(df)
print("num_instances:", num_instances)
num_duplicates = int(num_instances * 0.15)
num_unique = num_instances - num_duplicates
num_files = 8

# Shuffle the dataframe
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Split the dataframe into unique and duplicate sets
unique_df = df.iloc[:num_unique]
duplicate_df = df.iloc[num_unique:num_unique + num_duplicates]

# Create a list to keep track of which files each duplicate is placed in
duplicate_file_mapping = []

# Split the unique dataframe into 8 equally sized sets
unique_splits = np.array_split(unique_df, num_files)

# Add duplicates to the first 7 sets and record the files they are placed in
for i in range(num_duplicates):
    file1_index = i % (num_files - 1)
    file2_index = (file1_index + 1) % (num_files - 1)
    duplicate = duplicate_df.iloc[i]
    unique_splits[file1_index] = pd.concat([unique_splits[file1_index], duplicate.to_frame().T])
    unique_splits[file2_index] = pd.concat([unique_splits[file2_index], duplicate.to_frame().T])
    duplicate_file_mapping.append({
        'duplicate_index': duplicate['song_id'],
        'file1': f'data{file1_index + 1}.csv',
        'file2': f'data{file2_index + 1}.csv',
        'title': duplicate['title'],
        'artist': duplicate['artist']
    })

# Save the duplicate file mapping to a CSV file
duplicate_mapping_df = pd.DataFrame(duplicate_file_mapping)
duplicate_mapping_df.to_csv('duplicate_file_mapping.csv', index=False)

# Save the splits to CSV files
for i, split in enumerate(unique_splits):
    split.to_csv(f'data{i + 1}.csv', index=False)