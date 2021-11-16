class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper_count = 0
        first_is_upper = True if word[0].isupper() else False
        for i in range(len(word)):
            if word[i].isupper():
                upper_count += 1
        if upper_count == len(word) or upper_count == 0 or (upper_count == 1 and first_is_upper):
            return True
        else:
            return False