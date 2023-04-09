def removeDuplicates(head):
    #code here
    if(head==None and head.next==None):return 
    a=head
    while a.next:
        if a.data==a.next.data:
            a.next=a.next.next
        else:
            a=a.next
    return 
        
