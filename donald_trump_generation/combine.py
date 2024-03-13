import glob
import random
import re
phrase_length_min = 3
phrase_length_max = 4
with open("dt_input.txt", "w", encoding="utf8") as out_file:
    for file in glob.glob("*.txt"):
        with open(file, "r", encoding="utf8") as in_file:
            if "dt_input" in file:
                continue
            print(file)
            lines = in_file.readlines()
            for line in lines:
                in_quote = False
                start = 0
                puntucation_count = 0
                phrase_length = random.randint(phrase_length_min, phrase_length_max)
                for idx, char in enumerate(line):
                    if char == "." or char == "?":
                        puntucation_count +=1
                        if puntucation_count == phrase_length:
                            new_line = line[start:idx + 1]
                            new_line= new_line.replace("\"","").strip() + "\n"
                            out_file.write(new_line)
                            puntucation_count = 0
                            start  = idx + 1
                            phrase_length = random.randint(phrase_length_min, phrase_length_max)

                # start = 0
                # split_lines = re.split(r"[.?]", line)
                # while start < len(split_lines):
                #     phrase_length = random.randint(phrase_length_min, phrase_length_max)
                #     new_lines = [l.replace("\"","").strip() +" " for l in split_lines[start:start+phrase_length]]
                #     out_file.writelines(new_lines)
                #     out_file.write("\n")
                #     start += phrase_length
                
                
                # for l in split_lines:
                #     out_file.write(l.strip().replace("\"","") + "\n")
                #     # out_file.write("\n")