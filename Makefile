NAME := src
APP_NAME := stocktracker
VERSION := $(shell cat $(NAME)/VERSION)

VENV := .venv
PYTHON_VERSION := 3.8
BINS := $(VENV)/bin
PYTHON := $(BINS)/python
PIP := $(BINS)/pip
PEX := $(BINS)/pex
DIST := dist
PLATFORM := py3-none-any

SOURCES := $(wildcard $(APP_NAME)/**)

SRC := $(APP_NAME)-$(VERSION).tar.gz
DIST_SRC := $(DIST)/$(SRC)

WHEEL := $(APP_NAME)-$(VERSION)-$(PLATFORM).whl
DIST_WHEEL := $(DIST)/$(WHEEL)

PEXBIN := $(APP_NAME)-$(VERSION).pex
DIST_PEX := $(DIST)/$(PEXBIN)

#######################################

.PHONEY: all
all: test build run

.PHONEY: test
test: $(VENV)
	$(PYTHON) -m pylint $(NAME)
	$(PYTHON) -m mypy $(NAME)
	$(PYTHON) -m pytest 

.PHONEY: build
build: $(DIST_SRC) $(DIST_WHEEL) $(DIST_PEX)

$(DIST_SRC): $(VENV) $(NAME) $(SOURCES)
	echo "building src $(DIST_SRC)"
	$(PYTHON) $(NAME)/setup.py build sdist

$(DIST_WHEEL): $(VENV) $(NAME)/$(SORUCES)
	echo "building wheel $(DIST_WHEEL)"
	$(PYTHON) $(NAME)/setup.py build bdist_wheel

$(DIST_PEX): $(VENV) $(DIST_WHEEL) $(PEX) $(SOURCES)
	$(PEX) $(DIST_WHEEL) -c $(NAME) -o $(DIST_PEX)

.PHONEY: run
run:$(PYTHON) $(DIST_PEX)
	$(PYTHON) ./$(DIST_PEX)
#######################################
$(VENV):
	python$(PYTHON_VERSION) -m venv $(VENV)
	$(PIP) install --upgrade  pip wheel
	$(PIP) install -e "$(NAME)[dev]"

$(PYTHON): $(VENV)

$(PIP) : $(VENT)

$(PEX) : $(PIP)
	$(PIP) install --upgrade pex

.PHONEY: clean
clean:
	rm -rf $(VENV)
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info
