"""
A Red-Black Tree is a self-balancing binary search tree;
Each node has an additional attribute: color (red or black)

Properties:
1.Node Color: Each node is either red or black.
2.Root Property: The root of the tree is always black
3.Red Property: Red nodes cannot have red children
4.Black Property: Every path from a node to its null nodes(leaves) has the same number of black nodes
5.Leaf Property: All leaves(NIL nodes) are black
"""

#Belows are all pseudo code
#when do the left rotation of x, we assume that its right child y is not T.nil
left-rotate(T, x){
    y = x.right;
    if y.left != T.nil:
        y.left.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    else if x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y
}



#insert in the Red-Black Tree
RB-Insert(T, z):
    #move to find a right position
    y = T.nil
    x = T.root
    while x!= T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    #start to insert
    if y == T.nil:
        T.root = z
    else if z.key < y.key:
        y.left = z
    else:
        y.right = z

    z.left = T.nil
    z.right = T.nil
    z.color = red# set the color to be red
    RB-Insert-Fixup(T, z)

RB-Insert-Fixup(T, z):#z is red initially
    while z.p.color == red:#the loop continues as long as the parent of current node z is red(violation of property!)
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == red:#this violates both of the red node's children are black rule
                z.p.color = black
                y.color = black
                z.p.p.color = red
                z = z.p.p#update z, there might be further fix
            else if z== z.p.right:
                z = z.p
                left-rotate(T, z)
            else:
                z.p.color = black
                z.p.p.color = red
                right-rotate(T, z.p.p)
        else:
            same with above
T.root.color = black#finally make sure the root color is black



