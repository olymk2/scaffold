import datetime
from default import html_form_ui

class control(html_form_ui):    
    timestamp=None
    merchantid=None
    orderid=None
    amount=None
    currency='GB'
    def javascript(self,id=None):
        js=()
        return "\n".join(js)

    def get_value(self,name,value):
        count=0
        enum_name=name
        results=[]
        #results.append(value.get(name,None))
        while enum_name in value:
            results.append(value.get(enum_name,None))
            
            enum_name=name+str(count)
            count+=1
        return results  

    def shaHash(self):
        pass
    #19
    #(
    #TIMESTAMP.MERCHANT_ID.ORDER_ID.AMOUNT.CURRENCY
    #)
    #Like so:
    #(
    #20120926112654.thestore.ORD453-11.29900.EUR
    #)
    #Get the hash of this string (SHA-1 shown below).
    #(
    #b3d51ca21db725f9c7f13f8aca9e0e2ec2f32502
    #) 

    def details(self):
        pass

    #multiple plain text or numerical data form input
    def render(self,name, dict, error=None):
        return "\n".join(('<form method="POST" action="https://epage.payandshop.com/epage.cgi">',
                '<input type="hidden" name="MERCHANT_ID" value="Majestic Mint Limited">',
                '<input type="hidden" name="ORDER_ID" value="uniqueorder-id">',
                '<input type="hidden" name="ACCOUNT" value="sub account name">',
                '<input type="hidden" name="AMOUNT" value="amount">',
                '<input type="hidden" name="CURRENCY" value="currency code">',
                '<input type="hidden" name="TIMESTAMP" value="'+datetime.datetime.now().strftime('%Y%m%d%H%M')+'">',
                '<input type="hidden" name="MD5HASH" value="32 character string">',
                '<input type="hidden" name="AUTO_SETTLE_FLAG" value="1">',
                '<input type="submit" value="Click here to Purchase">',
                '</form>'))


    def xhtmlhead(self):
        return ""

    def html5body(self,id="map",text=""):
        htm=(   "<div id=\""+id+"\" style=\"height:500px; width:800px;\"></div>",
                "<input id=\"long\" name=\"long\" />",
                "<input id=\"lat\" name=\"lat\" />")
        
        return "\n".join(htm)

    def html5head(self):
        return ""
