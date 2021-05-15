# This function:
# check if the new record fullname has a similar name in the order_receipt 
# if a similar name exist, rather than just adding a new record to the receipt just update it

def update_string_field(order_receipt, order_receipt_fullname, updated_count):
    string_empty =''
    checking_state = False
    
    #convert order_receipt to list with split()
    receipt_list = order_receipt.split(',')

    for x in range(len(receipt_list)):
        #check if new record contains a name already in order_receipt 
        if order_receipt_fullname in receipt_list[x]:

            #since record exist only increase order count by 1
            updated_count = 1

            #get index number for duplicate name
            receipt_list_index = x

            #get duplicate record from list
            receipt_duplicate_exit = receipt_list[x]

            #split the receipt_duplicate_exit record
            duplicate_split=receipt_duplicate_exit.split(':')

            #get the name(full_name of the record)
            receipt_duplicate_name = duplicate_split[0]

            #get the record order count
            receipt_duplicate_order_count= duplicate_split[1]

            #update the order record count, strip is used to remove any trailing space 
            # both right and left
            receipt_duplicate_order_count = receipt_duplicate_order_count.strip()
            update_duplicate_order_count= float(receipt_duplicate_order_count) + updated_count

            # #merge the name(full_name of the record) with the updates count
            merge_update_together=  receipt_duplicate_name+': '+str(update_duplicate_order_count)

            #replicate the updated record in the list
            receipt_list[receipt_list_index] = merge_update_together

            #convert the list to a string
            for list_str in range(len(receipt_list)):
                string_empty += receipt_list[list_str]+', '

            #change the status to true
            checking_state = True

    if checking_state:

        #remove last commas in string(not inter comma), usually at the end of the string
        return string_empty[:-4]
    else:

        #check if the order receipt is empty
        if order_receipt == '':

            order_receipt = order_receipt +' %s : %s, ' %(order_receipt_fullname, updated_count)
        else:
            # check if the order receipts ends with 
            # an empty string in a list format
            len_receipt = len(receipt_list) #length of order receipt list

            if receipt_list[len_receipt - 1 ] == ' ':

                # if there is a trailing ' ' in the list
                # add only an ending ,
                order_receipt = order_receipt +' %s : %s, ' %(order_receipt_fullname, updated_count)
            else:

                # else add both prefix and suffix  ,
                order_receipt = order_receipt +', %s : %s, ' %(order_receipt_fullname, updated_count)
                
        #remove last commas in string(not inter comma), usually at the end of the string
        return order_receipt[:-2]
