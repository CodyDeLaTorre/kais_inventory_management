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
