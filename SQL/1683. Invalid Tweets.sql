-- LEN() - MySQL 中函数为 LENGTH():
SELECT tweet_id
FROM Tweets
WHERE length(content) > 15