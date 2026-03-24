import csv
import json

csv_file_path = 'data.csv'
js_file_path = 'tw_vocab.js'

vocab_list = []
seen_ids = set() 

with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # 精準抓取終端機印出來的欄位
        word_id = row.get('詞目id', '').strip()
        raw_word = row.get('詞目', '').strip()
        meaning = row.get('解說', '').strip()
        
        if word_id and raw_word and (word_id not in seen_ids):
            seen_ids.add(word_id)
            
            # 從中間空白切開
            parts = raw_word.split(' ', 1)
            word = parts[0]
            pinyin = parts[1] if len(parts) > 1 else ""
            
            vocab_list.append({
                'w': word,
                'p': pinyin,
                'c': meaning,
                'lv': 1, 
                'audio': word_id
            })

with open(js_file_path, mode='w', encoding='utf-8') as file:
    # ⚠️ 這裡把 const twVocab 改成 window.twVocab
    file.write("window.twVocab = ") 
    json.dump(vocab_list, file, ensure_ascii=False, indent=4)
    file.write(";\n")

print(f"🎉 破解成功！自動切分漢字與拼音，共收錄 {len(vocab_list)} 題，請查看 {js_file_path}。")
