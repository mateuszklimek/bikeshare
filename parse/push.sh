curl -X POST \
-H "X-Parse-Application-Id: wZ6DmhBoPqcnsld6D0n2k8ZViPxa38vzLm3L4YyT" \
-H "X-Parse-REST-API-Key: BaOyq0sG3qtXXcoDExW82U8qnL9VN12aYuUdcyct" \
-H "Content-Type: application/json" \
-d '{ "channel": "ipad_news",
"data": { "alert": "The new iPad has been released!" } }' \
https://api.parse.com/1/push