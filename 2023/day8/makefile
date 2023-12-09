build:
	docker build -t adventofcode_day8java .
run:
	docker run -d --name adventofcode_day8java_cont -v .:/code adventofcode_day8java

debug:
	docker exec -it adventofcode_day8java_cont /bin/bash

clean:
	docker kill adventofcode_day8java_cont
	docker image rm -f adventofcode_day8java
	docker container rm -f adventofcode_day8java_cont
	docker image prune -a; docker system prune -a --volumes;