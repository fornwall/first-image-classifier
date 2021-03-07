IMAGE_NAME = fredrikfornwall/first-image-classifier

docker_image:
	cd flask_web && docker build -t $(IMAGE_NAME):latest .

push_docker_image:
	docker push --all-tags $(IMAGE_NAME)

run_docker:
	docker run -p 5000:5000 $(IMAGE_NAME)

.PHONY:
	docker_image
