import re

def find_percentage_values(text):
    percentages = re.findall(r'[0-9]+\,[0-9]+(?=%)', text)
    filtered_percentages = []
    for percentage in percentages:
        if "," in percentage:
            filtered_percentages.append(percentage.replace(',', '.'))
    values = [float(percentage) for percentage in filtered_percentages]
    return values
