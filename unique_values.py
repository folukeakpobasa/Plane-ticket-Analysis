# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes("object")
print(non_numeric)
# Loop through columns
for column in non_numeric.columns:
  
  # Print the number of unique values
  print(f"Number of unique values in \
      {column} column: ", non_numeric[column].nunique())