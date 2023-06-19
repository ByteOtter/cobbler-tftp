clean: ## Cleans Python bytecode, build artifacts and the temp files.
	@echo "cleaning: python bytecode"
	@rm -f *.pyc
	@rm -f src/**/*.pyc
	@rm -rf src/__pycache__
	@rm -rf src/**/__pycache__
	@rm -rf tests/__pycache__
	@rm -rf tests/**/__pycache__
	@echo "cleaning: build artifacts"
	@rm -rf build release dist cobbler_tftp.egg-info
	@rm -rf rpm-build/*
	@rm -rf deb-build/*
	@rm -f MANIFEST AUTHORS
	@rm -f config/version
	@rm -f docs/*.1.gz
	@rm -rf docs/_build
	@echo "cleaning: temp files"
	@rm -f *~
	@rm -rf buildiso
	@rm -f *.tmp
	@rm -f *.log
	@rm -f supervisord.pid
	@rm -rf .pytest_cache
