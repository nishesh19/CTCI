from collections import Counter


def find_word_concatenation(str, words):

    words_count = Counter(words)
    window = sum(map(lambda x: len(x), words))
    word_len = len(words[0])

    start, w_start = 0, 0
    matched = 0
    result_indices = []

    for end in range(word_len-1, len(str)):
        curr_word = str[w_start:end+1]
        if curr_word in words_count:
            words_count[curr_word] -= 1

            if words_count[curr_word] == 0:
                matched += 1
                

            if matched == len(words_count):
                result_indices.append(start)
                prev_word = str[start:start+word_len]
                words_count[prev_word] += 1
                matched -= 1
            
            w_start = end + 1

        if end-w_start+1 == word_len:
            w_start += 1

        if end-start+1 == window:
            start += 1

    # TODO: Write your code here
    return result_indices


if __name__ == "__main__":
    print(find_word_concatenation('catfoxcat', ['cat', 'fox']))
