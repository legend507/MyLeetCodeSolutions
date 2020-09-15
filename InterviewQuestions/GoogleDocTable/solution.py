# Assume text contains words with a space separating thems.

# For Q1
def CalcHeight(text, width):
  # Input check.
  if width == 0:
    return float('inf')
  if len(text) == 0:
    return 0

  height = 0
  this_line = 0

  # Process 1 word each loop.
  for word in text.split(' '):
    length = len(word)

    # Deal with very long words.
    if length > width:
      # Fill the rest of this_line with this word.
      length = length - (width - 1 - this_line)
      height += 1
      while length > width:
        length = length - width
        height += 1
      this_line = length

    # For normal words.
    else:
      # For the 1st word there is no space. We start to put a space ahead starting the 2nd word.
      length_with_space = length + 1 if this_line > 0 else length

      if this_line + length_with_space < width:
        this_line += length_with_space
      else:
        # Filled up this line, starting a new line.
        height += 1

        if this_line + length_with_space > width:
          this_line = length
        else:
          this_line = 0

  if this_line > 0:
    height += 1

  return height

# For Q2
def FindBestColumnSize(text_left, text_right, width):
  # Assume table boundaries take no spaces.
  min_width = 1
  max_width = width

  mid = (min_width + max_width) / 2

  while min_width < max_width:
    mid = (max_width + max_width) / 2

    left_height = CalcHeight(text_left, mid)
    right_height = CalcHeight(text_right, max_width - mid)

    if left_height == right_height:
      return left_height
    
    if left_height > right_height:
      min_width = mid + 1
    else:
      max_width = mid

  # Need to do something when we go out of the while without finding returning.

  return