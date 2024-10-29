import cv2
import zxingcpp

img = cv2.imread('test.png')
s=zxingcpp.read_barcodes(img)

for r in s:
    dlstring = r.text

    dlstringarray = dlstring.split('<LF>')
    dlstringarray = dlstringarray[2:]
    dlstringarray = [line.strip() for line in dlstringarray]

    for field in dlstringarray:

        fieldID = field[0:3]
        fieldValue = field[3:]

        if fieldID == 'DAC':
            print("First Name: ")
            print(fieldValue + "\n")
        elif fieldID == 'DAD':
            print('Middle Name: ')
            print(fieldValue + "\n")
        elif fieldID == 'DCS':
            print('Last Name:')
            print(fieldValue + "\n")
        # elif fieldID == 'DCD':
        #     print('Jurisdiction specific endorsement codes: ')
        # elif fieldID == 'DBA':
        #     print('Document Expiration date: ')
        # elif fieldID == 'DCS':
        #     print('Customer Family Name: ')
        # elif fieldID == 'DCT':
        #     print('Customer Given Name: ')
        # elif fieldID == 'DBD':
        #     print('Document Issue Date: ')
        # elif fieldID == 'DBB':
        #     print('Date of Birth: ')
        # elif fieldID == 'DBC':
        #     print('Sex: ')  # 1 for male, 2 for female
        # elif fieldID == 'DAY':
        #     print('Eye Color: ')
        # elif fieldID == 'DAU':
        #     print('Height: ')
        # elif fieldID == 'DAG':
        #     print('Address Line 1: ')
        # elif fieldID == 'DAI':
        #     print('City: ')
        # elif fieldID == 'DAJ':
        #     print('State: ')
        # elif fieldID == 'DAK':
        #     print('Postal Code: ')
        # elif fieldID == 'DAQ':
        #     print('Customer ID Number: ')
        # elif fieldID == 'DCF':
        #     print('Document Discriminator: ')
        # elif fieldID == 'DCG':
        #     print('Country Identification: ')
        # elif fieldID == 'DCK':
        #     print('Inventory control number: ')