from pyscript import document, display

def placeOrder(e): # just variable-ing

    prod1 = document.getElementById("LMXM4")
    prod2 = document.getElementById("LMXM3S")
    prod3 = document.getElementById("RBV3")
    prod4 = document.getElementById("CA5400")
    prod5 = document.getElementById("TV380")
    prod6 = document.getElementById("FDT")

    items = "" # checks if checkbox is checked and adds the item to list
    if prod1.checked: items += "Logitech MX Master 4<br>"
    if prod2.checked: items += "Logitech MX Master 3S<br>"
    if prod3.checked: items += "Razer Basilisk V3<br>"
    if prod4.checked: items += "Corsair Air 5400<br>"
    if prod5.checked: items += "Thermaltake View 380<br>"
    if prod6.checked: items += "Fractal Design Terra<br>"

    subtotal = ( # its just adding stuff if the product is checked

    (float(prod1.value) if prod1.checked else 0.0) + 
    (float(prod2.value) if prod2.checked else 0.0) + 
    (float(prod3.value) if prod3.checked else 0.0) + 
    (float(prod4.value) if prod4.checked else 0.0) + 
    (float(prod5.value) if prod5.checked else 0.0) + 
    (float(prod6.value) if prod6.checked else 0.0)

    )

    # this took WAAYYY too long for how simple it is
    # this is just an fstring with some extra stuff like html stuff which i was able to call by setting the textOut heading tag with the id textOut to the variable

    vat = subtotal * 0.12
    total = subtotal + vat
    
    textOut = f""" 
    <div class="container roundbord">
    <br>
    -------- reciept --------<br>
    {items if items else "no items selected<br>"}
    -------------------------<br>
    subtotal: ₱{subtotal:,.2f}<br>
    vat: {vat:,.2f}<br>
    -------------------------<br>
    total: ₱{total:,.2f}
    <br>
    <br>
    </div>
    """
    
    document.getElementById("textOut").innerHTML = textOut

def genSKU(e):
    document.getElementById('displaySKU').innerHTML = "" # clear div
    prodCategory = document.getElementById('prodCat').value
    prodName = document.getElementById('prodNm').value.strip()
    prodQty = document.getElementById('prodStock').value.strip()
    SKUname = (prodCategory.upper() + "XXX")[:3] + "-" + (prodName.upper() + "XXXX")[:4] + "-" + (prodQty.zfill(4)[:4] if prodQty else 0.0)
    # okay so  get first 3 letters of category,  | add "-" then get first 4 letters       |    add "-" then put quantity and add zeroes
    # (triple x is the fallback in case its not  |         (XXXX is the fallback here)    |            before to make sure its four
    # three letters for any reason)              |                                        |            digits

    display("generated sku: ", SKUname, target='displaySKU')