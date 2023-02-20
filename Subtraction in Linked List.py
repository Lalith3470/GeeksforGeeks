def subLinkedList(l1, l2): 
    # Code here
    # return head of difference list
    s1=""
    s2=""
    while l1:
        s1+=str(l1.data)
        l1=l1.next
    while l2:
        s2+=str(l2.data)
        l2=l2.next
    val=""
    if int(s1)>=int(s2):
        val=str(int(s1)-int(s2))
    else:
        val=str(int(s2)-int(s1))
    a=Node(0)
    tmp=a
    for i in val:
        i=int(i)
        tmp.next=Node(i)
        tmp=tmp.next
    return a.next
