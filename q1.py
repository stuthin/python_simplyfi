def convert_to_indian_currency(value):
    if value < 0:
        return "Negative values are not supported"
    
    # Convert to string
    value_str = str(value)
    
    # Split into whole and decimal parts if needed
    if '.' in value_str:
        whole_part, decimal_part = value_str.split('.')
    else:
        whole_part = value_str
        decimal_part = ''
    
    # Add commas to the whole part
    if len(whole_part) > 3:
        last_three = whole_part[-3:]
        other_numbers = whole_part[:-3]
        if other_numbers:
            formatted_whole_part = ','.join([other_numbers[i:i + 2] for i in range(0, len(other_numbers), 2)]) + ',' + last_three
        else:
            formatted_whole_part = last_three
    else:
        formatted_whole_part = whole_part
    
    # Format decimal part if it exists
    if decimal_part:
        formatted_decimal_part = '.' + decimal_part
    else:
        formatted_decimal_part = ''
    
    # Combine whole and decimal parts
    formatted_value = formatted_whole_part + formatted_decimal_part
    
    return f"₹ {formatted_value}"

# Example usage:
value = 123456789
formatted_currency = convert_to_indian_currency(value)
print(formatted_currency)  # Output: ₹ 12,34,56,789
