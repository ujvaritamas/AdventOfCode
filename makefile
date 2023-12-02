build:
	docker build -t adventofcode .
run:
	docker run -d --name adventofcode_cont -v .:/code adventofcode

debug:
	docker exec -it adventofcode_cont /bin/bash

clean:
	docker kill adventofcode_cont
	docker image rm -f adventofcode
	docker container rm -f adventofcode_cont
	docker image prune -a; docker system prune -a --volumes;