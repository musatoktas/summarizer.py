from transformers import pipeline

# Transformer modelini yüklemek için pipeline oluşturma
summarizer = pipeline("summarization")

def summarize_text(text):
    # Metin özetleme işlemi
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Örnek metin
text = """
Gaza war: Israeli tank fire kills five soldiers in north Gaza, military says. Israel's military says five soldiers have been killed by Israeli tank fire in northern Gaza, in one of the deadliest incidents of its kind since the war against Hamas began in October. An initial probe found that two tanks fired at a building in Jabalia refugee camp where the troops had gathered. Troops went back into the area this week after previously pulling out, saying Hamas had regrouped there. Tens of thousands of Palestinians have fled the fighting and bombardment. Both the Israeli military and Hamas's military wing said on Wednesday that battles in Jabalia camp and the surrounding town of Jabalia were intensifying. Battles also raged around the southern city of Rafah, from where nearly 600,000 people have fled since the start of an Israeli operation 10 days ago. More than a million displaced people had been taking refuge there.
"""

# Metni özetle ve sonucu yazdır
print("Original Text: ", text)
print("Summary: ", summarize_text(text))

