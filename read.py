data = []
count = 0
with open("reviews.txt","r")as f:
	for line in f:
		data.append(line)
		count += 1 #count = count +1 # 
		if count % 1000 == 0:
			print(len(data))
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print("平均留言是",sum_len/len(data))



# print("檔案讀取完了,總共有", len(data),"筆資料")