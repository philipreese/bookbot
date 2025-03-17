def get_num_words(text):
  return len(text.split())

def get_chars_dict(text):
  chars = {}
  for c in text:
    key = c.lower()
    chars[key] = chars.get(key, 0) + 1
  return chars

def chars_dict_to_sorted_list(num_chars_dict):
  sorted_list = []
  for ch in num_chars_dict:
    sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

def sort_on(dict):
  return dict["num"]