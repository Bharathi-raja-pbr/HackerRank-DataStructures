def postOrder(root):
    #Write your code here
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print(root.info,end=" ")
