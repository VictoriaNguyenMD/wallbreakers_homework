class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        dict_words = {}
        answer = []
        combined_list = A.split(" ") + B.split(" ")
        for word in combined_list: 
            if word in dict_words:
                dict_words[word] += 1
            else:
                dict_words[word] = 1
        for key, val in dict_words.items():
            if val == 1:
                answer.append(key)
        return answer
