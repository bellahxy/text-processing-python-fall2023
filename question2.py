#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:01:28 2023

@author: Bella Huang
"""

import re
import os
import csv

# define the base directory
BASE_DIR = "/Users/bella/Documents/GitHub/homework-2-bellahxy"

def read_file(fpath):
    with open(fpath, "r") as f:
        return f.read()

# extract the table content based on start and end markers
def extract_table_content(file):
    start_index = file.find("Abilene, TX Metropolitan Statistical Area")
    end_index = file.find("Yuma Gain 0 0 0 5 0 5 0 5 4 9 76,606 0.0%") + 42
    return file[start_index:end_index]

# clean the text by removing column names, page numbers and footnotes
def clean_text(text, col_names):
    text = text.replace("\n", " ")
    for col_name in col_names:
        text = text.replace(col_name, "")
    pattern_page = "B-\d+"
    return re.sub(pattern_page, "", text)

# split the cleaned table into individual strings, each ending with a '%' sign
def split_into_strings(table_clean):
    pattern_pct = "(.*?)%"
    table_string = re.findall(pattern_pct, table_clean)
    table_string = [string.strip() for string in table_string]
    pattern_num = "[\d\s,()%.-]+"
    return [s for s in table_string if not re.fullmatch(pattern_num, s)]

# group the strings by their Metropolitan Statistical Area (MSA) designation
def group_by_msa(table_string):
    msa = ["Metropolitan Statistical Area", "Micropolitan Statistical Area", "Metropolitan Division"]
    table_msa = {}
    for string in table_string:
        if any(substring in string for substring in msa):
            current_msa = string
            table_msa[current_msa] = []
        else:
            table_msa[current_msa].append(string)
    return [f"{key}{value}" for key, value in table_msa.items()]

# convert a string with parentheses to a negative number, or a regular string to a positive number
def to_numeric(s):
    s = s.replace(",", "")
    if "(" in s and ")" in s:
        if "." in s:
            return -float(s.replace("(", "").replace(")", ""))
        else:
            return -int(s.replace("(", "").replace(")", ""))
    else:
        if "." in s:
            return float(s)
        else:
            return int(s)

# parse the list of strings to extract MSA, base, action, and numbers
def parse_strings(list):
    
    pattern_msa = "(.*? (Metropolitan Statistical Area|Micropolitan Statistical Area|Metropolitan Division))"
    pattern_base = "(.*?)(Close/Realign|Gain|Realign|Close)([\d\s,().-]+)"
  
    rows = []
    
    for string in list:
        msa_match = re.search(pattern_msa, string)
        msa = msa_match.group(1) if msa_match else None
        string = string.replace(msa_match.group(0), "")
        
        base_matches = re.findall(pattern_base, string)
        for base_match in base_matches:
            base, action, numbers = base_match
            if base.startswith("['"):
                base = base[2:]
            elif base.startswith("', '") or base.startswith("', \"") or base.startswith('",\''):
                base = base[4:]
            base = base.strip()
            number_list = [to_numeric(num) for num in numbers.split()]
            rows.append([msa, base, action] + number_list)
            
    return rows

def write_to_csv(parsed_table, filename="question2.csv"):
    csv_col_names = ["msa", "base", "action", "mil_out", "civ_out", "mil_in", "civ_in", "mil_net", "civ_net", "net_contractor", "direct", "indirect", "total", "ea_emp", "ch_as_perc"]
    
    for row in parsed_table:
        if row[-1] is not None:
            row[-1] = str(row[-1]) + "0%" 
    
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(csv_col_names)
        for row in parsed_table:
            writer.writerow(row)

# main execution
if __name__ == "__main__":
    input_file_path = os.path.join(BASE_DIR, "2005proposal.pdf.txt")
    output_file_path = os.path.join(BASE_DIR, "question2.csv")
    os.chdir(BASE_DIR)
    
    file_content = read_file(input_file_path)
    table_content = extract_table_content(file_content)
    
    col_names = ["Installation", "Economic Installation Action", "Area Changes", "Economic Area", "Economic Installation", "Out In Net Gain/(Loss) Net Mission", "Total", "Indirect","Economic Contractor", "Contractor", "Direct", "Changes", "Job", "Employment", "Economic Action", "Mil Civ", "Action",  "as Percent of", "Changes", "Economic Area Installation", "________________", "This list does not include locations where no changes in military or civilian jobs are affected.", "Military figures include student load changes."]
    cleaned_table = clean_text(table_content, col_names)
    table_strings = split_into_strings(cleaned_table)
    grouped_strings = group_by_msa(table_strings)
    parsed_data = parse_strings(grouped_strings)
    
    write_to_csv(parsed_data, output_file_path)
