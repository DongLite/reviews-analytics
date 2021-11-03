data = []
count = 0
count_sum = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完畢，總共有', len(data), '筆資料')

for d in data:
	count_sum += len(d)
print('平均每一則留言大約', count_sum / len(data), '個字')