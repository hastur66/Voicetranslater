from google_trans_new import google_translator 

translator = google_translator()  

#translate_text = translator.translate('สวัสดีจีน', lang_tgt='en')  
translate_text = translator.translate('யார் நீ', lang_src='ta', lang_tgt='si')

print(translate_text)