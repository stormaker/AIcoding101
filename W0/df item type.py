import pandas as pd


# Function to determine the type based on the item name
def determine_type_fixed(item_name):
    # Convert non-string types to strings to avoid TypeError
    if not isinstance(item_name, str):
        return 'Other'  # Return 'Other' if item_name is not a string (e.g., NaN or float)

    # Original function logic
    if 'Bib' in item_name:
        return 'Bib'
    elif 'Coat' in item_name:
        return 'Coat'
    elif 'Hoodie' in item_name:
        return 'Hoodie'
    elif 'Jacket' in item_name:
        return 'Jacket'
    elif 'Jersey' in item_name:
        return 'Jersey'
    elif 'Pant' in item_name:
        return 'Pant'
    elif 'Polo' in item_name:
        return 'Polo'
    elif 'Shirt' in item_name:
        return 'Shirt'
    elif 'Short' in item_name:
        return 'Short'
    elif 'Singlet' in item_name:
        return 'Singlet'
    elif 'Skort' in item_name:
        return 'Skort'
    elif 'Softshell' in item_name:
        return 'Softshell'
    elif 'Tee' in item_name:
        return 'Tee'
    elif 'Netball Dress' in item_name:
        return 'Netball Dress'
    elif 'Top' in item_name:
        return 'Top'
    elif 'A-Line Dress' in item_name:
        return 'Netball Dress'
    elif 'Guernsey' in item_name:
        return 'Singlet'
    elif 'Jkt' in item_name:
        return 'Jacket'
    elif 'Jumper' in item_name:
        return 'Singlet'
    elif 'Jumpers' in item_name:
        return 'Singlet'
    elif 'Playing Jumper' in item_name:
        return 'Singlet'
    elif 'Puffer Vest' in item_name:
        return 'Puffer Vest'
    elif 'Soft Shell' in item_name:
        return 'SoftShell'
    elif 'Sweatshirt' in item_name:
        return 'Sweatshirt'
    elif 'Trackpant' in item_name:
        return 'Pant'
    elif 'Tshirt' in item_name:
        return 'T-Shirt'
    elif 'T-shirt' in item_name:
        return 'T-shirt'
    elif 'Vest' in item_name:
        return 'Vest'
    elif 'Top' in item_name:
        return 'Top'
    elif 'POLO' in item_name:
        return 'Polo'
    else:
        return 'Other'


# Update the types in the uploaded Excel file
def update_types_in_excel(file_path):
    # Load the Excel file
    df = pd.read_excel(file_path)

    # Apply the updated function to the 'Item' column to determine the 'Type'
    df['Type'] = df['Item'].apply(determine_type_fixed)

    # Save the updated DataFrame to a new Excel file
    output_path = file_path.replace('.xlsx', '_fixed.xlsx')
    df.to_excel(output_path, index=False)

    return output_path

# Path to the input Excel file
input_file_path = 'D:\\ee.xlsx'  # Replace with your actual file path

# Updating the types and saving to a new file
updated_file_path = update_types_in_excel(input_file_path)

# Print the path to the updated Excel file
print(f'Updated Excel file saved to: {updated_file_path}')
