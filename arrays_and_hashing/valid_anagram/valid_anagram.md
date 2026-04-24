# Valid Anagram

- Difficulty: Easy
- Topic: Hash Table, Stirng, Sorting

## Idea
今回の問題では英語，小文字であることが条件になるので，要素数26の配列を作ればデータを格納するには十分である．アナグラムかを確認するにはそれぞれの文字が同じ回数出現しているかを確認すればいい．

## Tips
- 文字を数字に変換する際にはord()を用いる．数字を文字に変換する際にはchr()を用いる．
- 文字列をソートする際にはsorted()を用いる．
- 辞書の.getを用いる際に第二引数を指定することで辞書内に値がなかった場合の初期値を与えることができる．

## Complexity
- Time: O(n+m)
- Space: O(1) since we have at most 26 different characters.