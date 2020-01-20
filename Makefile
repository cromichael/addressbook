PROJECT_ADDR=address_book

.PHONY: all
all: install
### @ means make will not echo the command
	@echo "Welcome to project address_book!"

# This will create an image based on the Dockerfile 
.PHONY: install
install:
	docker build --tag address_book .

# This will remove address_book image
.PHONY: clean
clean:
	docker rmi address_book:latest
	rm -fr __pycache__
