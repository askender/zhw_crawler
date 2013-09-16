help:
	@echo Usage: make [\TARGET\]
	@echo
	@echo TARGET:
	@echo "    clean    清理文件"
	@echo "    docs     docs"
	@echo

.PHONY: clean docs test

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name 'proxy_list_raw' -exec rm -f {} +

docs:
	python -m SimpleHTTPServer 8004

dianping:
	@echo "starting"
	scrapy crawl dianping -s LOG_FILE=zhw_crawler/log/dianping/dianping.log

dianping_local:
	@echo "starting local"
	scrapy crawl dianping_local -o log/dianpingshops.json -t json -s LOG_FILE=zhw_crawler/log/dianping/dianping_local.log

daodao:
	@echo "starting"
	scrapy crawl daodao -s LOG_FILE=zhw_crawler/log/daodao/daodao.log

daodao_local:
	@echo "starting local"
	scrapy crawl daodao_local -o log/daodaoshops.json -t json -s LOG_FILE=zhw_crawler/log/dianping/daodao_local.log

manager:
	cd crawler_manager && python run.py

commit:
	@echo "starting commit"
	git add . && git commit -a

deploy:
	git push origin master
