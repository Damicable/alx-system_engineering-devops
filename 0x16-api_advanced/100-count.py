#!/usr/bin/python3
"""Module to recursively print sorted count of hot articles of subreddit"""

import requests
import sys


def word_in_sentence(word, sentence, holder):
    """This returns word count"""
    if len(sentence) == 0:
        return holder
    if word == sentence[0].lower():
        if holder.get(word):
            holder[word] = holder.get(word) + 1
        else:
            holder[word] = 1
    return word_in_sentence(word, sentence[1:], holder)


def word_in_array_of_sentences(word, arr, holder):
    """Counts the arrays"""
    if len(arr) == 0:
        return holder
    holder = word_in_sentence(word, arr[0].split(' '), holder)
    return word_in_array_of_sentences(
            word, arr[1:], holder)


def words_in_array_of_sentences(words, arr, holder):
    if len(words) == 0:
        return holder
    holder = word_in_array_of_sentences(words[0].lower(), arr, holder)
    return words_in_array_of_sentences(
            words[1:], arr, holder)


def recurse(subreddit, hot_list=[], after=""):
    """
    Return all hot article titles
    """
    req_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Switch value to prevent breaking"
    }
    params = {
        "after": after
    }
    r = requests.get(
            req_url, headers=headers, params=params, allow_redirects=False)
    if r.status_code == 200:
        bulk_resp = r.json()
        children = bulk_resp.get('data').get('children')
        new_after = bulk_resp.get('data').get('after')
        titles = list(map(lambda x: x.get('data').get('title'), children))
        hot_list.extend(titles)
        if new_after is None:
            return hot_list
        return recurse(subreddit, hot_list, new_after)
    else:
        return None


def count_words(subreddit, word_list):
    """
    Recursively count all words in hot titles
    """
    hot_titles = recurse(subreddit)
    if hot_titles is not None:
        word_occurence = words_in_array_of_sentences(
                word_list, hot_titles, {})
        sorted_dict = dict(
                sorted(
                    word_occurence.items(), key=lambda item: (
                        -item[1], item[0])))
        for key, value in sorted_dict.items():
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    count_words(sys.argv[1], sys.argv[2])
