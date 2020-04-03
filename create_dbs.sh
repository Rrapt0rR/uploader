#!/bin/bash
set -e

POSTGRES="psql --username ${POSTGRES_USER}"

$POSTGRES <<EOSQL
CREATE DATABASE master OWNER mastermanager;
EOSQL

psql -U mastermanager master < docker-entrypoint-initdb.d/dev_db/master.sql
