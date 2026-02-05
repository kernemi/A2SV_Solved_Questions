from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        charcounts = Counter(chars)
        for i in range(len(words)):
            counts = Counter(words[i])
            for ch in words[i]:
                if ch not in chars:
                    break
            else:
                for ch in words[i]:
                    if counts[ch] > charcounts[ch]:
                        break
                else:
                    total += len(words[i])
        return total
