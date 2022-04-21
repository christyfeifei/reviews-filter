data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))  # 每讀一筆留言，印出數字

print('檔案讀取完了, 總共有', len(data), '筆資料')  # 印出總共幾筆留言

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print('留言平均長度為', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆, 長度小於100的資料')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆資料有提到good')
print(good[0])
