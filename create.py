# -*- coding: utf-8 -*-
import pandas as pd

original_data = pd.read_csv('second.csv')
prefix = 'second-'
total = 10000 # 정답지 파일 갯수(csv 맨 마지막 행)
uncorrect = [total - 4650, total - 7000, total - 3780, total - 5700, total- 10000]
filename = ['-1.csv', '-2.csv', '-3.csv', '-4.csv', '-5.csv']

def reverseValue(num):
	if num is 0:
		return 1
	else:
		return 0

# 정답지 not 연산
# 0->1, 1->0
def create_part_reverse_y(uncorrect, save_path):
	data = original_data.copy()
	_hash = data.hash
	_y = data.y
	
	for idx, value in enumerate(_y[:uncorrect]):
		y = reverseValue(value)
		_y[idx] = y	
		
	filename = prefix + save_path
	new_data = pd.DataFrame({'file':_hash, 'mal/ben(1/0)':_y})
	new_data.to_csv(filename, index=False)

#해시 변경(000추가)
#abc.vir -> 000abc.vir
def create_part_change_filename(uncorrect, save_path):
	data = original_data.copy()
	_hash = data.hash
	_y = data.y
	
	for idx, value in enumerate(_hash[:uncorrect]):
		hash = '000' + value
		_hash[idx] = hash
		
	filename = prefix + save_path
	new_data = pd.DataFrame({'file':_hash, 'mal/ben(1/0)':_y})
	new_data.to_csv(filename, index=False)

#해시 삭제
#*주의 : 테스트할 데이터 갯수가 적어짐
def create_part_delete_hash(uncorrect, save_path):
	data = original_data.copy()
	_hash = data.hash
	_y = data.y
	
	filename = prefix + save_path
	new_data = pd.DataFrame({'file':_hash[:uncorrect], 'mal/ben(1/0)':_y[:uncorrect]})
	new_data.to_csv(filename, index=False)

# #add new hash and y
# def create_part5():
# 	add_data = original_data[:n5].copy()
	
# 	for idx, row in add_data.iterrows():
# 		hash = "000" + row['hash']
# 		y = row['y']
# 		add_data.loc[idx, 'hash'] = hash
		
# 	filename = prefix + '5.csv'	
# 	new_data = original_data.append(add_data)
# 	new_data.to_csv(filename, index=False)	


for idx in range(0, len(uncorrect)):
	if idx%2 == 0:
		create_part_reverse_y(uncorrect[idx], filename[idx])
	else:
		create_part_change_filename(uncorrect[idx], filename[idx])
