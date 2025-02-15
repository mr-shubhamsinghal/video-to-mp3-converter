# video-to-mp3-converter

- Initial commit

- k9s

- curl -X POST http://mp3converter.com/login -u user@example.com:password -> To get token

- curl -X POST -F 'file=@./test_video.mp4' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXJAZXhhbXBsZS5jb20iLCJleHAiOjE3Mzk2OTEyMDgsImlhdCI6MTczOTYwNDgwOCwiYWRtaW4iOnRydWV9.ihkxPG1wELeXKnTVLogfjcADQ3AHgnkj7uK-Y2kYYUc' http://mp3converter.com/upload

- brew services start mongodb/brew/mongodb-community

- brew services stop mongodb/brew/mongodb-community

- http://rabbitmq-manager.com/

- mongofiles --db=mp3s get_id --local=test.mp3 '{"$oid": "67b0976198d08ada3c2d78d0"}'