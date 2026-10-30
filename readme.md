A small project for me to learn how to use postgres with python in Docker containers.
I know it doesn't really have an application, but at least I know how it works now!
# Installation
first clone this repo, and change the `.env.example` filename to `.env`.
then use `docker compose up --build` to build the containers and attach to them, and see the results.
you can change the environment variables and run `docker compose up --build` again to add more rows of information.
# Output
Building the containers with the following .env file:
```
POSTGRES_PASSWORD=postgres
PASS_VALUE_NAME=new person
PASS_VALUE_COMPANY=cat organization
PASS_VALUE_NAME2=newer person
PASS_VALUE_COMPANY2=cattier organization```
Should look something like this:
```bash
[kingissuper@meow python+postgres_docker]$ docker compose up --build
[+] up 17/17
 ✔ Image postgres:15 Pulled                                                                                                     10.9s
WARN[0010] buildx Docker CLI plugin not found: falling back to the classic builder. BuildKit-only build features (multi-arch, secrets, ssh, additional contexts, ...) will not be available 
Sending build context to Docker daemon  9.335MB
Step 1/7 : FROM python:3.14
 ---> 90bdf58a84b9
Step 2/7 : WORKDIR /app
 ---> Running in b6e93144ccfe
 ---> Removed intermediate container b6e93144ccfe
 ---> 81dd91d8ce92
Step 3/7 : COPY requirements.txt .
 ---> 5ecfd933185a
Step 4/7 : RUN pip install -r requirements.txt
 ---> Running in bd52fb4f8fa8
Collecting psycopg2-binary (from -r requirements.txt (line 1))
  Downloading psycopg2_binary-2.9.13-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
Downloading psycopg2_binary-2.9.13-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.3/4.3 MB 19.6 MB/s  0:00:00
Installing collected packages: psycopg2-binary
Successfully installed psycopg2-binary-2.9.13
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
 ---> Removed intermediate container bd52fb4f8fa8
 ---> 1d9866157539
Step 5/7 : COPY /src .
 ---> c883c6c2598e
Step 6/7 : CMD ["python", "main.py"]
 ---> Running in 9e50d5adfe76
 ---> Removed intermediate container 9e50d5adfe76
 ---> e4ab0b138a94
Step 7/7 : LABEL com.docker.compose.image.builder=classic
 ---> Running in 2b5998ebb93c
 ---> Removed intermediate container 2b5998ebb93c
 ---> 2387008039d1
Successfully built 2387008039d1
Successfully tagged pythonpostgres_docker-app:latest
[+] up 22/22
 ✔ Image postgres:15                          Pulled                                                                            10.9s
 ✔ Image pythonpostgres_docker-app            Built                                                                             26.5s
 ✔ Network pythonpostgres_docker_default      Created                                                                            0.1s
 ✔ Volume pythonpostgres_docker_postgres_data Created                                                                            0.0s
 ✔ Container postgres_db                      Created                                                                            0.2s
 ✔ Container terra_script                     Created                                                                            0.1s
Attaching to postgres_db, terra_script
Container postgres_db Waiting 
postgres_db  | The files belonging to this database system will be owned by user "postgres".
postgres_db  | This user must also own the server process.
postgres_db  | 
postgres_db  | The database cluster will be initialized with locale "en_US.utf8".
postgres_db  | The default database encoding has accordingly been set to "UTF8".
postgres_db  | The default text search configuration will be set to "english".
postgres_db  | 
postgres_db  | Data page checksums are disabled.
postgres_db  | 
postgres_db  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
postgres_db  | creating subdirectories ... ok
postgres_db  | selecting dynamic shared memory implementation ... posix
postgres_db  | selecting default max_connections ... 100
postgres_db  | selecting default shared_buffers ... 128MB
postgres_db  | selecting default time zone ... Etc/UTC
postgres_db  | creating configuration files ... ok
postgres_db  | running bootstrap script ... ok
postgres_db  | performing post-bootstrap initialization ... ok
postgres_db  | initdb: warning: enabling "trust" authentication for local connections
postgres_db  | initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
postgres_db  | syncing data to disk ... ok
postgres_db  | 
postgres_db  | 
postgres_db  | Success. You can now start the database server using:
postgres_db  | 
postgres_db  |     pg_ctl -D /var/lib/postgresql/data -l logfile start
postgres_db  | 
postgres_db  | waiting for server to start....2026-10-30 22:25:00.761 UTC [48] LOG:  starting PostgreSQL 15.19 (Debian 15.19-1.pgdg13+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
postgres_db  | 2026-10-30 22:25:00.763 UTC [48] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
postgres_db  | 2026-10-30 22:25:00.770 UTC [51] LOG:  database system was shut down at 2026-10-30 22:24:58 UTC
postgres_db  | 2026-10-30 22:25:00.782 UTC [48] LOG:  database system is ready to accept connections
postgres_db  |  done
postgres_db  | server started
postgres_db  | 
postgres_db  | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
postgres_db  | 
postgres_db  | 2026-10-30 22:25:00.915 UTC [48] LOG:  received fast shutdown request
postgres_db  | waiting for server to shut down....2026-10-30 22:25:00.917 UTC [48] LOG:  aborting any active transactions
postgres_db  | 2026-10-30 22:25:00.921 UTC [48] LOG:  background worker "logical replication launcher" (PID 54) exited with exit code 1
postgres_db  | 2026-10-30 22:25:00.922 UTC [49] LOG:  shutting down
postgres_db  | 2026-10-30 22:25:00.925 UTC [49] LOG:  checkpoint starting: shutdown immediate
postgres_db  | 2026-10-30 22:25:00.939 UTC [49] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.001 s, sync=0.004 s, total=0.018 s; sync files=2, longest=0.002 s, average=0.002 s; distance=0 kB, estimate=0 kB
postgres_db  | 2026-10-30 22:25:00.943 UTC [48] LOG:  database system is shut down
postgres_db  |  done
postgres_db  | server stopped
postgres_db  | 
postgres_db  | PostgreSQL init process complete; ready for start up.
postgres_db  | 
postgres_db  | 2026-10-30 22:25:01.070 UTC [1] LOG:  starting PostgreSQL 15.19 (Debian 15.19-1.pgdg13+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
postgres_db  | 2026-10-30 22:25:01.070 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
postgres_db  | 2026-10-30 22:25:01.071 UTC [1] LOG:  listening on IPv6 address "::", port 5432
postgres_db  | 2026-10-30 22:25:01.073 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
postgres_db  | 2026-10-30 22:25:01.078 UTC [62] LOG:  database system was shut down at 2026-10-30 22:25:00 UTC
postgres_db  | 2026-10-30 22:25:01.086 UTC [1] LOG:  database system is ready to accept connections
Container postgres_db Healthy 
terra_script  | (1, 'new person', 'cat organization', datetime.datetime(2026, 10, 30, 22, 25, 4, 113361))
terra_script  | (2, 'newer person', 'cattier organization', datetime.datetime(2026, 10, 30, 22, 25, 4, 113361))
terra_script exited with code 0```