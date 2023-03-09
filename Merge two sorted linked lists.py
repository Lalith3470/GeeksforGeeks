def sortedMerge(head1, head2):
    # code here
    lst=[]
    while head1:
        lst.append(head1.data)
        head1=head1.next
    while head2:
        lst.append(head2.data)
        head2=head2.next
    lst.sort()
    a=Node(0)
    tmp=a
    for i in lst:
        tmp.next=Node(i)
        tmp=tmp.next
    return a.next

