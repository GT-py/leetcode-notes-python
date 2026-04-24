# Two Sum

- Difficulty: Easy
- Topics: Array, Hash Table

## Idea
ハッシュテーブルを用いることで配列すべてを探索せずにO(1)で探索が終了する(格納にはO(n)かかる)

## Tips
- forループの際にenumerate()を用いると可読性が上がる．第一戻り値がindex，第二戻り値が格納された値．

## Complexity
- Time: O(n)
- Space: O(n)