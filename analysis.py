import csv


def convert(csv_path, txt_path):
    with open(csv_path, 'r') as c:
        csv_reader = csv.reader(c)
        data = [','.join(row) for row in csv_reader]
    with open(txt_path, 'w') as t:
        t.write('\n'.join(data))
        
if __name__ == "__main__":
    csv_path = "\Users\sanvi\Downloads\keystrokes_log (37).csv"
    txt_path = "\Users\sanvi\SURF_Parkinsons_Disease-9"
    convert(csv_path, txt_path)
    