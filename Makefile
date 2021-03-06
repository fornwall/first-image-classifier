IMAGE_NAME = fredrikfornwall/smile-detector

docker_image:
	cd flask_web && docker build -t $(IMAGE_NAME):latest .

run_docker:
	docker run -p 5000:5000 $(IMAGE_NAME)

.PHONY:
	docker_image
