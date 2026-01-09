import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
Text = "Hello my name is Gabriel Okom; it is really nice to meet you."

token = enc.encode(Text)

# output = [13225, 922, 1308, 382, 52073, 532, 6382, 26, 480, 382, 2715, 7403, 316, 4158, 481, 13]
print("Encoded:", token)

token2 = enc.decode([13225, 922, 1308, 382, 52073, 532, 6382, 26, 480, 382, 2715, 7403, 316, 4158, 481, 13])
print("Decoded:", token2)
