help:
	@echo Usage: make [\TARGET\]
	@echo
	@echo TARGET:
	@echo "    clean    清理临时文件"
	@echo "    test     test"
	@echo "    docs     docs"
	@echo "    start    start"
	@echo "    deploy   deploy"
	@echo

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '*.log' -exec rm -f {} +

rm:
	find . -name '*.html' -exec rm -f {} +

docs:
	python -m SimpleHTTPServer 8004

test:
	@echo "starting test"
	python hello.py -t

start:
	make test
	@echo "starting ttmian"
	python hello.py

add:
	@echo "starting add"
	git add .

ci:
	@echo "starting commit"
	autopep8 . -air
	git add . && git commit -am 'new'

deploy:
	@echo "starting deploy"
	fab deploy

# sort -n solidot_words.txt | uniq >solidot_words2.txt
