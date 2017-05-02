import cv2
import numpy as np 

def convolve(img, mask):
	rows, cols = img.shape
	row_mask, col_mask = mask.shape
	conv_img = np.zeros((rows,cols),np.float32)

	assert ((row_mask == col_mask) and (row_mask%2 !=0)), "mask input is incorrect"
	for i in range(rows):
		for j in range(cols):
			itr_row = i - row_mask/2
			itr_col = j - col_mask/2

			temp = 0
			while itr_row <= i + row_mask/2:
				while itr_col <= j + col_mask/2:
					if itr_row >=0 and itr_col >=0 and itr_row<rows and itr_col<cols:
						temp += img[itr_row, itr_col]*mask[itr_row-i+row_mask/2, itr_col-j+col_mask/2]
					itr_col = itr_col+1
				conv_img[i,j] = temp
				itr_row = itr_row+1
	return conv_img

