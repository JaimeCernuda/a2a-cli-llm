#!/bin/bash
cd /home/jcernuda/micro_agent
uv run python -m client.main send --agent http://localhost:8000 --message "List the BP5 files in the data directory, then inspect the variables in data/data1.bp"