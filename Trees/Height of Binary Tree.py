def height(root):
  left_height=0
  right_height=0

  if root.left:
      left_height = height(root.left) + 1
  if root.right:
      right_height = height(root.right) + 1

  if left_height  > right_height:
     return  left_height
  else:
     return right_height
