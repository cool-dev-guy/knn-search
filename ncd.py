import gzip
def ncd(string1, string2):
    Cx1 = len(gzip.compress(string1.encode()))
    Cx2 = len(gzip.compress(string2.encode()))
    combined_str = " ".join([string1, string2])
    Cx1x2 = len(gzip.compress(combined_str.encode()))

    # Calculate NCD
    ncd = (Cx1x2 - min(Cx1, Cx2)) / max(Cx1, Cx2)
    similarity = 1 - ncd
    dissimilarity = ncd
    return similarity, dissimilarity
string1 = ["miss america","Mission not impossible","Mission","Massion","Missin"]
string2 = "Mission impossible"

# RESULT ANALYSIS
# if similarity < 5.0: => different

for i in range(len(string1)):
    similarity, dissimilarity = ncd(string1[i], string2)
    print(f"Similarity between '{string1[i]}' and '{string2}': {similarity:.4f}")
    # print(f"Dissimilarity between '{string1[i]}' and '{string2}': {dissimilarity:.4f}")
