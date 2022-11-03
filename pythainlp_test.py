from pythainlp import word_tokenize,Tokenizer
import deepcut
text = "รู้สึกสมเพชตัวเองที่ทำอะไรออกมาได้ไม่ดีสักอย่าง อยากร้องไห้แต่ก็รู้สึกว่าไม่มีสิทธิ์แม้แต่จะร้องไห้ คนอะไรแม่งโคตรน่าสมเพช"
print("Algorithm (mewmm)")
print (word_tokenize(text, engine="newmm"))

print("Algorithm(longest)")
print (word_tokenize(text, engine="longest"))

print("Algorithm(multi_cut)")
print (word_tokenize(text, engine="multi_cut"))

print("Algorithm(Deepcut)")
print (deepcut.tokenize(text))