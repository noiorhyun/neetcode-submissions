class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        window = Counter()

        left = 0
        window_size = len(s1)

        for right in range(len(s2)):
            window[s2[right]] += 1

            if right - left + 1 > window_size:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            if window == s1_count:
                return True

        return False