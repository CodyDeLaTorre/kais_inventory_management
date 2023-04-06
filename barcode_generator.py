from io import BytesIO
import random

from barcode import EAN13
from barcode .writer import SVGWriter

inventory_amount = 25

while inventory_amount > 0:
    num = random.randint(100000000000, 100000011111)
    with open(f"testfile.svg{inventory_amount}", "wb") as f:
        EAN13(str(num), writer=SVGWriter()).write(f)
    inventory_amount = inventory_amount - 1

    
#_______BROKEN CODE______   
# from io import BytesIO
# import random
# import os.path

# from barcode import EAN13 , UPCA
# from barcode .writer import SVGWriter

# save_path = 'C:/home/n46252/dev/practice/inventory_management/barcodes/'

# inventory_amount = 25

# while inventory_amount > 0:
#     name = f"testfile.svg{inventory_amount}"
#     complete_name = os.path.join(save_path, name)
#     num = random.randint(100000000000, 100000011111)
#     with open(complete_name, "wb") as f:
#         EAN13(str(num), writer=SVGWriter()).write(f)
#     inventory_amount = inventory_amount - 1
