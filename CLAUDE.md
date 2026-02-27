# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

This repository ("agentcoding") is a Python project containing a CLI utility for sorting integers.

## Structure

- `sort_list.py` — CLI script and `sort_list()` function for sorting a list of integers
- `tests/test_sort_list.py` — pytest tests (unit + CLI integration)
- `.venv/` — Python 3.13 virtual environment

## Commands

- **Run tests:** `.venv/bin/pytest tests/ -v`
- **Run the script:** `python sort_list.py <int> [<int> ...]`
