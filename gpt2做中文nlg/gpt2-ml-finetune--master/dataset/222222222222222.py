import re
pattern2=r'.*?[。！？]'
t='''白锦无纹香烂漫，玉树琼苞堆雪。静夜沉沉，浮光霭霭，冷浸溶溶月。人间天上，烂银霞照通彻。浑似姑射真人，天姿灵秀，意气殊高洁。万蕊参差谁信道，不与群芳同列。浩气清英，仙才卓荦，下土难分别。瑶台归去，洞天方看清绝。dsfasdfasd dsfasd。
'''
tmp=re.findall(pattern2,t)
print(tmp)