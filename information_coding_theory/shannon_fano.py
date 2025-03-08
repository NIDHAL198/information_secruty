def shannon_fano(symbols, probabilities):

   pairs = sorted(zip(probabilities, symbols), reverse=True)
   sorted_probs, sorted_symbols = zip(*pairs)
   
   total_prob = sum(sorted_probs)
   
   cumulative = 0
   for i, p in enumerate(sorted_probs):
      cumulative += p
      if cumulative >= total_prob / 2:
            break

   left_symbols = sorted_symbols[:i+1]
   left_probs = sorted_probs[:i+1]
   right_symbols = sorted_symbols[i+1:]
   right_probs = sorted_probs[i+1:]
   
   left_codes = shannon_fano(left_symbols, left_probs)
   right_codes = shannon_fano(right_symbols, right_probs)
   
   codes = {}
   for sym in left_codes:
      codes[sym] = "0" + left_codes[sym]
   for sym in right_codes:
      codes[sym] = "1" + right_codes[sym]
   
   return codes

symbols = ["A", "B", "C", "D"]
probabilities = [0.1, 0.4, 0.3, 0.2]

codes = shannon_fano(symbols, probabilities)


for sym in codes:
   print(f"{sym} : {codes[sym]}")
