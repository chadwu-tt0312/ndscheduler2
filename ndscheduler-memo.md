
## setup (origin)

1. uv venv --python=3.9
2. export NDSCHEDULER_SETTINGS_MODULE=simple_scheduler.settings
3. fix makefile
4. simple_scheduler/requirements.txt fix (mark git)
5. simple_scheduler/scheduler.py fix (Fix for Tornado+asyncio on Windows)
6. add requirements.txt
   - tornado>=6.4.2
   - SQLAlchemy>=2.0.39
   - apscheduler>=3.11.0
   - future>=0.18.3
   - python-dateutil>=2.8.2
   - pytz>=2025.2
7. uv pip install -r requirements.txt
8. (X)uv pip install setuptools
9. (X)uv run setup.py install
10. make simple
11. uv pip install -e .
12. uv run simple_scheduler/scheduler.py

## setup (palto42)

1. uv venv --python=3.11
2. export NDSCHEDULER_SETTINGS_MODULE=simple_scheduler.settings
3. uv pip install setuptools
4. uv pip install ldap/python_ldap-3.4.4-cp311-cp311-win_amd64.whl
5. fix makefile/setup.cfg/setup.py
6. add test_requirements.txt
   - pytz>=2025.2
7. uv pip install -r test_requirements.txt
8. make install
9. make test
10. del build/dist/doc/ndscheduler.egg-info path
11. uv pip install -e .
12. uv run simple_scheduler/scheduler.py

## update to python 3.11 (origin)

1. Tornado 相關更新
    - ...
2. SQLAlchemy 相關更新
    - ...
3. APScheduler 相關更新
    - n/a
4. del .venv/
    - close IDE and open cmd to run
5. uv venv --python=3.11
6. .venv/Scripts/activate
7. uv pip install -r requirements.txt
8. fix setup.py
9. uv pip install -e .

## RUN (origin)

1. export NDSCHEDULER_SETTINGS_MODULE=simple_scheduler.settings
2. uv run simple_scheduler/scheduler.py

## Memo (origin)

1. DB tablename
   - DEFAULT_JOBS_TABLENAME = 'scheduler_jobs'
   - DEFAULT_EXECUTIONS_TABLENAME = 'scheduler_execution'
   - DEFAULT_AUDIT_LOGS_TABLENAME = 'scheduler_jobauditlog'
2. AUDIT_LOGS 只儲存 job 變更紀錄，EXECUTIONS 只儲存 job 執行紀錄。
3. DEFAULT_TIMEZONE = 'UTC'
4. NDSCHEDULER_SETTINGS_MODULE=simple_scheduler.settings 用來決定要載入哪個設定檔。當這個環境變數沒有設定時，系統會使用預設設定（default_settings.py），而不是我們的自定義設定（simple_scheduler/settings.py）。在預設設定中，HTTP_PORT 被設定為 7777。
5. move base_test.py
    - from `\ndscheduler\corescheduler\datastore\base_test.py`
    - to `\tests\ndscheduler\corescheduler\datastore\test_base.py`
6. move another *_test.py

### cUrl

```bash
curl -X POST http://localhost:8888/api/v1/jobs \
  -H "Content-Type: application/json" \
  -d '{
    "job_class_string": "simple_scheduler.jobs.sample_job.AwesomeJob",
    "name": "API 新增的任務",
    "pub_args": ["API參數1", "API參數2"],
    "minute": "*/5"
  }'
```

### DDL (datastore.db)

```SQL
CREATE TABLE scheduler_jobs (
    id VARCHAR(191) NOT NULL, 
    next_run_time FLOAT, 
    job_state BLOB NOT NULL, 
    PRIMARY KEY (id)
)

CREATE TABLE scheduler_jobauditlog (
    job_id TEXT NOT NULL, 
    job_name TEXT NOT NULL, 
    event INTEGER NOT NULL, 
    user TEXT, 
    created_time DATETIME NOT NULL, 
    description TEXT
)

CREATE TABLE scheduler_execution (
    eid VARCHAR(191) NOT NULL, 
    hostname TEXT, 
    pid INTEGER, 
    state INTEGER NOT NULL, 
    scheduled_time DATETIME NOT NULL, 
    updated_time DATETIME, 
    description TEXT, 
    result TEXT, 
    job_id TEXT NOT NULL, 
    task_id TEXT, 
    PRIMARY KEY (eid)
)
```

### cmd (origin)

```cmd
netstat -ano | findstr :8888

# pytest
uv pip install pytest pytest_asyncio
pytest tests/test_main.py -v
pytest tests/ndscheduler/corescheduler/datastore/test_base.py -v
pytest ndscheduler/server/handlers/executions_test.py -v

# temp
pytest tests/corescheduler/datastore/providers/test_sqlite_async.py -v
pytest tests/integration/test_server.py -v
pytest tests/integration/test_server.py -vv -s
```
