def getNthFromLast(head,n):
    #code here
    lst=[]
    while head:
        lst.append(head.data)
        head=head.next
    if len(lst)<n:
        return -1
    return lst[-n]

