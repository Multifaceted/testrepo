import torch

print("number of gpu:", torch.cuda.device_count())

text_file = open("data.txt", "w")

text_file.write("number of gpu:" + str(torch.cuda.device_count()))

text_file.close()