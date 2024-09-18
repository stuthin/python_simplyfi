    def convert_to_indian_currency(value):
      if value < 0:
        return "Negative values are not supported"
    
    value_str = str(value)
  
    if '.' in value_str:
        whole_part, decimal_part = value_str.split('.')
    else:
        whole_part = value_str
        decimal_part = ''
    
    if len(whole_part) > 3:
        last_three = whole_part[-3:]
        other_numbers = whole_part[:-3]

            formatted_whole_part = ','.join([other_numbers[i:i + 2] for i in range(0, len(other_numbers), 2)]) + ',' + last_three
        else:
            formatted_whole_part = last_three
    else:
        formatted_whole_part = whole_part
    

    if decimal_part:
        formatted_decimal_part = '.' + decimal_part
    else:
        formatted_decimal_part = ''
    

    formatted_value = formatted_whole_part + formatted_decimal_part
    
    return f"₹ {formatted_value}"
