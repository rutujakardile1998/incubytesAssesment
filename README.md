# incubytesAssesment

## Rutuja Kardile

### Current Status:
We maintain all customers in one database. There are heaps of customers with user cards to
my hospital. So, I decided to split up the customers based on the country and load them into
corresponding country tables.
To pull the customers as per Country, my developers should know what are all the places the
Customer Data is available. So, the data extracting will be done by our Source System. They
will pull the all the relevant customer data and will give us a Data file.

### In design documents, you will have:
! File Name Specification – Name String, Extension of the files
! Date and Time format of the File – YYYYMMDD, HHMMSSTT or any other format
! Header Records Layout –
|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|
State|Country|DOB|Is_Active
! Details Record Layout – |D|John|123456|20101012|20121013|MVD|Paul|NSW|AU|06031987|A
