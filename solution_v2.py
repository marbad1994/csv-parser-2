import csv


def main():
    A = 'csxobjix.csv'
    B = 'COS_object_list.csv'
    with open(B, 'rb') as f:
        b_data = list(csv.reader(f, delimiter=' ', skipinitialspace=True))
    b_data = b_data[12:]

    with open(A) as f:
        a_data = list(csv.reader(f, delimiter='	'))

    new_csv = []





    for a_row in a_data:
        new_row = a_row
        for b_row in b_data:
            if a_row[3] == b_row[0]:
                new_row = [a_row[0]] + [b_row[1]] + a_row[2:]
                break                
            elif a_row[3][:2] == "CV" and b_row[0][:2] == "PT" and a_row[3][2:] == b_row[0][2:]: 
                new_row = [a_row[0]] + [b_row[1]] + a_row[2:]
                break
            elif a_row[3][:2] == "SL" and b_row[0][:2] == "TC" and a_row[3][2:] == b_row[0][2:]: 
                new_row = [a_row[0]] + [b_row[1]] + a_row[2:]
                break

        new_csv.append(new_row)        

    with open('result.csv', 'w') as f:
        wr = csv.writer(f, delimiter="	")
        wr.writerows(new_csv)




if __name__ == "__main__":
    main()
                
