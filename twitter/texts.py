import csv
import json

texts = []
output_len = 2500

with open('user_timeline.json', encoding='utf-8') as f:
    statuses = json.load(f)
    for status in statuses:
        entities = status['entities']
        for entity in entities.values():
            if entity:
                break
        else:
            text = status['text']
            if '@' not in text:
                texts.append(text)

with open('texts.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(list(reversed(texts))[:output_len])
