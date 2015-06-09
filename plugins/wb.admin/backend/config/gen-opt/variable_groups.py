variable_groups = [ ('abort-slave-event-count', ['Replication/Slave']),
  ('allow-suspicious-udfs', ['Security/Security']),
  ('ansi', ['General/SQL']),
  ('audit-log', ['Logging/Audit']),
  ('audit_log_buffer_size', ['Logging/Audit']),
  ('audit_log_connection_policy', ['Logging/Audit']),
  ('audit_log_exclude_accounts', ['Logging/Audit']),
  ('audit_log_file', ['Logging/Audit']),
  ('audit_log_format', ['Logging/Audit']),
  ('audit_log_include_accounts', ['Logging/Audit']),
  ('audit_log_policy', ['Logging/Audit']),
  ('audit_log_rotate_on_size', ['Logging/Audit']),
  ('audit_log_statement_policy', ['Logging/Audit']),
  ('audit_log_strategy', ['Logging/Audit']),
  ('authentication_windows_log_level', ['Security/Security']),
  ('authentication_windows_use_principal_name', ['Security/Security']),
  ('autocommit', ['General/Transactions']),
  ('avoid_temporal_upgrade', []),
  ('backup_elevation', ['General/Backup']),
  ('backup_history_log', ['General/Backup']),
  ('backup_history_log_file', ['General/Backup']),
  ('backup_progress_log', ['General/Backup']),
  ('backup_progress_log_file', ['General/Backup']),
  ('backupdir', ['General/Backup']),
  ('basedir', ['General/Directories']),
  ('big-tables', ['General/General']),
  ('bind-address', ['Networking/General']),
  ('binlog-checksum', ['Logging/Binlog Options']),
  ('binlog-do-db', ['Logging/Binlog Options']),
  ('binlog-format', ['Logging/Binlog Options']),
  ('binlog-ignore-db', ['Logging/Binlog Options']),
  ('binlog-row-event-max-size', ['Logging/Binlog Options']),
  ('binlog-rows-query-log-events', ['Logging/Binlog Options']),
  ('binlog_cache_size', ['Logging/Binlog Options']),
  ('binlog_direct_non_transactional_updates', ['Logging/Binlog Options']),
  ('binlog_error_action', ['Logging/Binlog Options']),
  ('binlog_group_commit_sync_delay', ['Logging/Binlog Options']),
  ('binlog_group_commit_sync_no_delay_count', ['Logging/Binlog Options']),
  ('binlog_gtid_simple_recovery', ['Logging/Binlog Options']),
  ('binlog_row_image', ['Logging/Binlog Options']),
  ('binlog_stmt_cache_size', ['Logging/Binlog Options']),
  ('binlogging_impossible_mode', ['Logging/Binlog Options']),
  ('block_encryption_mode', ['Security/Security']),
  ('bootstrap', ['Advanced/General']),
  ('bulk_insert_buffer_size', ['Advanced/Various']),
  ('character-set-filesystem', ['General/International']),
  ('character-set-server', ['General/International']),
  ('character-sets-dir', ['General/International']),
  ('check_proxy_users', []),
  ('chroot', ['Advanced/General']),
  ('collation-server', ['General/International']),
  ('completion_type', ['Advanced/Transactions']),
  ('concurrent_insert', ['MyISAM/General']),
  ('connect_timeout', ['Networking/Timeout Settings']),
  ('console', ['Logging/General']),
  ('core-file', ['General/System']),
  ('daemon_memcached_enable_binlog', ['Other/Memcached']),
  ('daemon_memcached_engine_lib_name', ['Other/Memcached']),
  ('daemon_memcached_engine_lib_path', ['Other/Memcached']),
  ('daemon_memcached_option', ['Other/Memcached']),
  ('daemon_memcached_r_batch_size', ['Other/Memcached']),
  ('daemon_memcached_w_batch_size', ['Other/Memcached']),
  ('daemonize', []),
  ('datadir', ['General/Directories']),
  ('debug', ['Advanced/General']),
  ('debug-sync-timeout', ['Advanced/General']),
  ('default-character-set', ['General/International']),
  ('default-collation', ['General/International']),
  ('default-storage-engine', ['General/General']),
  ('default-table-type', ['General/General']),
  ('default-time-zone', ['General/International']),
  ('default_authentication_plugin', ['Security/Authentication']),
  ('default_password_lifetime', ['Security/Authentication']),
  ('default_tmp_storage_engine', ['General/General']),
  ('default_week_format', ['General/International']),
  ('delay-key-write', ['Performance/General']),
  ('delayed_insert_limit', ['Advanced/Insert delayed settings']),
  ('delayed_insert_timeout', ['Advanced/Insert delayed settings']),
  ('delayed_queue_size', ['Advanced/Insert delayed settings']),
  ('des-key-file', ['Security/Security']),
  ('disable_gtid_unsafe_statements', ['Replication/General']),
  ('disconnect-slave-event-count', ['Replication/Slave']),
  ('disconnect_on_expired_password', ['Security/Authentication']),
  ('div_precision_increment', ['Advanced/General']),
  ('enable-locking', ['General/Features']),
  ('enable-named-pipe', ['Networking/General']),
  ('enable-pstack', ['General/Features']),
  ('enforce_gtid_consistency', ['Replication/General']),
  ('engine-condition-pushdown', ['Performance/Optimizer']),
  ('event-scheduler', ['General/Features']),
  ('executed-gtids-compression-period', ['Replication/General']),
  ('exit-info', ['Advanced/General']),
  ('expire_logs_days', ['Logging/Advanced log options']),
  ('explicit_defaults_for_timestamp', ['General/SQL']),
  ('external-locking', ['General/System']),
  ('federated', ['General/Features']),
  ('flush', ['Advanced/General']),
  ('flush_time', ['Advanced/General']),
  ('ft_boolean_syntax', ['MyISAM/Fulltext search']),
  ('ft_max_word_len', ['MyISAM/Fulltext search']),
  ('ft_min_word_len', ['MyISAM/Fulltext search']),
  ('ft_query_expansion_limit', ['MyISAM/Fulltext search']),
  ('ft_stopword_file', ['MyISAM/Fulltext search']),
  ('gdb', ['General/System']),
  ('general-log', ['Logging/General']),
  ('general_log_file', ['Logging/General']),
  ('group_concat_max_len', ['Advanced/Various']),
  ('gtid-executed-compression-period', []),
  ('gtid-mode', ['Replication/General']),
  ('ignore-builtin-innodb', ['InnoDB/General']),
  ('ignore-db-dir', ['General/System']),
  ('init-file', ['General/General']),
  ('init-rpl-role', ['Replication/General']),
  ('init_connect', ['Advanced/General']),
  ('init_slave', ['Advanced/General', 'Replication/Slave']),
  ('initialize', []),
  ('initialize-insecure', []),
  ('innodb-safe-binlog', ['InnoDB/General']),
  ('innodb-status-file', ['InnoDB/General']),
  ('innodb_adaptive_flushing', ['InnoDB/General']),
  ('innodb_adaptive_flushing_lwm', ['InnoDB/General']),
  ('innodb_adaptive_hash_index', ['InnoDB/General']),
  ('innodb_adaptive_max_sleep_delay', ['InnoDB/General']),
  ('innodb_additional_mem_pool_size', ['InnoDB/Memory']),
  ('innodb_api_bk_commit_interval', ['InnoDB/General']),
  ('innodb_api_disable_rowlock', ['InnoDB/General']),
  ('innodb_api_enable_binlog', ['InnoDB/General']),
  ('innodb_api_enable_mdl', ['InnoDB/General']),
  ('innodb_api_trx_level', ['InnoDB/General']),
  ('innodb_autoextend_increment', ['InnoDB/General']),
  ('innodb_autoinc_lock_mode', ['InnoDB/General']),
  ('innodb_buffer_pool_awe_mem_mb', ['InnoDB/Buffer pool']),
  ('innodb_buffer_pool_chunk_size', []),
  ('innodb_buffer_pool_dump_at_shutdown', ['InnoDB/Buffer pool']),
  ('innodb_buffer_pool_dump_now', ['InnoDB/Buffer pool']),
  ('innodb_buffer_pool_dump_pct', ['InnoDB/General']),
  ('innodb_buffer_pool_filename', ['InnoDB/Buffer pool']),
  ('innodb_buffer_pool_instances', ['InnoDB/Buffer pool', 'InnoDB/Memory']),
  ('innodb_buffer_pool_load_abort', ['InnoDB/Buffer pool']),
  ('innodb_buffer_pool_load_at_startup', ['InnoDB/Buffer pool']),
  ('innodb_buffer_pool_load_now', ['InnoDB/Buffer pool']),
  ('innodb_buffer_pool_size', ['InnoDB/Buffer pool', 'InnoDB/Memory']),
  ('innodb_change_buffer_max_size', ['InnoDB/General']),
  ('innodb_change_buffering', ['InnoDB/General']),
  ('innodb_checksum_algorithm', ['InnoDB/General']),
  ('innodb_checksums', ['InnoDB/General']),
  ('innodb_cmp_per_index_enabled', ['InnoDB/General']),
  ('innodb_commit_concurrency', ['InnoDB/General']),
  ('innodb_compression_failure_threshold_pct', ['InnoDB/General']),
  ('innodb_compression_level', ['InnoDB/General']),
  ('innodb_compression_pad_pct_max', ['InnoDB/General']),
  ('innodb_concurrency_tickets', ['InnoDB/General']),
  ('innodb_create_intrinsic', ['InnoDB/General']),
  ('innodb_data_file_path', ['InnoDB/Datafiles']),
  ('innodb_data_home_dir', ['InnoDB/Datafiles']),
  ('innodb_disable_sort_file_cache', ['InnoDB/General']),
  ('innodb_doublewrite', ['InnoDB/General']),
  ('innodb_extra_dirty_writes', ['InnoDB/General']),
  ('innodb_fast_shutdown', ['InnoDB/Various']),
  ('innodb_file_format', ['InnoDB/Datafiles']),
  ('innodb_file_format_check', ['InnoDB/Datafiles']),
  ('innodb_file_format_max', ['InnoDB/Datafiles']),
  ('innodb_file_io_threads', ['InnoDB/General']),
  ('innodb_file_per_table', ['InnoDB/General']),
  ('innodb_fill_factor', ['InnoDB/General']),
  ('innodb_flush_log_at_trx_commit', ['InnoDB/Logfiles']),
  ('innodb_flush_method', ['InnoDB/Logfiles']),
  ('innodb_flush_neighbors', ['InnoDB/Logfiles']),
  ('innodb_flush_sync', []),
  ('innodb_flushing_avg_loops', ['InnoDB/General']),
  ('innodb_force_load_corrupted', ['InnoDB/General']),
  ('innodb_force_recovery', ['InnoDB/General']),
  ('innodb_ft_aux_table', ['InnoDB/Fulltext search']),
  ('innodb_ft_cache_size', ['InnoDB/Fulltext search']),
  ('innodb_ft_enable_diag_print', ['InnoDB/Fulltext search']),
  ('innodb_ft_enable_stopword', ['InnoDB/Fulltext search']),
  ('innodb_ft_max_token_size', ['InnoDB/Fulltext search']),
  ('innodb_ft_min_token_size', ['InnoDB/Fulltext search']),
  ('innodb_ft_num_word_optimize', ['InnoDB/Fulltext search']),
  ('innodb_ft_result_cache_limit', ['InnoDB/Fulltext search']),
  ('innodb_ft_server_stopword_table', ['InnoDB/Fulltext search']),
  ('innodb_ft_sort_pll_degree', ['InnoDB/Fulltext search']),
  ('innodb_ft_total_cache_size', ['InnoDB/Fulltext search']),
  ('innodb_ft_user_stopword_table', ['InnoDB/Fulltext search']),
  ('innodb_io_capacity', ['InnoDB/General']),
  ('innodb_io_capacity_max', ['InnoDB/General']),
  ('innodb_large_prefix', ['InnoDB/General']),
  ('innodb_lock_wait_timeout', ['InnoDB/General']),
  ('innodb_locks_unsafe_for_binlog', ['InnoDB/General']),
  ('innodb_log_arch_dir', ['InnoDB/Logfiles']),
  ('innodb_log_archive', ['InnoDB/Logfiles']),
  ('innodb_log_buffer_size', ['InnoDB/Logfiles']),
  ('innodb_log_checksum_algorithm', []),
  ('innodb_log_compressed_pages', ['InnoDB/Logfiles']),
  ('innodb_log_file_size', ['InnoDB/Logfiles']),
  ('innodb_log_files_in_group', ['InnoDB/Logfiles']),
  ('innodb_log_group_home_dir', ['InnoDB/Logfiles']),
  ('innodb_log_write_ahead_size', ['InnoDB/Logfiles']),
  ('innodb_lru_scan_depth', ['InnoDB/General']),
  ('innodb_max_dirty_pages_pct', ['InnoDB/General']),
  ('innodb_max_dirty_pages_pct_lwm', ['InnoDB/General']),
  ('innodb_max_merged_io', ['InnoDB/General']),
  ('innodb_max_purge_lag', ['InnoDB/General']),
  ('innodb_max_purge_lag_delay', ['InnoDB/General']),
  ('innodb_max_undo_log_size', ['InnoDB/General']),
  ('innodb_mirrored_log_groups', ['InnoDB/Logfiles']),
  ('innodb_monitor_disable', ['InnoDB/General']),
  ('innodb_monitor_enable', ['InnoDB/General']),
  ('innodb_monitor_reset', ['InnoDB/General']),
  ('innodb_monitor_reset_all', ['InnoDB/General']),
  ('innodb_old_blocks_pct', ['InnoDB/General']),
  ('innodb_old_blocks_time', ['InnoDB/General']),
  ('innodb_online_alter_log_max_size', ['InnoDB/General', 'InnoDB/Logfiles']),
  ('innodb_open_files', ['InnoDB/General']),
  ( 'innodb_optimize_fulltext_only',
    ['InnoDB/Fulltext search', 'InnoDB/General']),
  ('innodb_optimize_point_storage', []),
  ('innodb_page_cleaners', ['InnoDB/Memory']),
  ('innodb_page_size', ['InnoDB/Memory']),
  ('innodb_print_all_deadlocks', ['InnoDB/General']),
  ('innodb_purge_batch_size', ['InnoDB/General']),
  ('innodb_purge_rseg_truncate_frequency', []),
  ('innodb_purge_threads', ['InnoDB/General']),
  ('innodb_random_read_ahead', ['InnoDB/General']),
  ('innodb_read_ahead_threshold', ['InnoDB/General']),
  ('innodb_read_io_threads', ['InnoDB/General']),
  ('innodb_read_only', ['InnoDB/General']),
  ('innodb_replication_delay', ['InnoDB/General']),
  ('innodb_rollback_on_timeout', ['InnoDB/General']),
  ('innodb_rollback_segments', ['InnoDB/General']),
  ('innodb_sort_buffer_size', ['InnoDB/General', 'InnoDB/Memory']),
  ('innodb_spin_wait_delay', ['InnoDB/General']),
  ('innodb_stats_auto_recalc', ['InnoDB/General']),
  ('innodb_stats_method', ['InnoDB/General']),
  ('innodb_stats_on_metadata', ['InnoDB/General']),
  ('innodb_stats_persistent', ['InnoDB/General']),
  ('innodb_stats_persistent_sample_pages', ['InnoDB/General']),
  ('innodb_stats_sample_pages', ['InnoDB/General']),
  ('innodb_stats_transient_sample_pages', ['InnoDB/General']),
  ('innodb_status_output', ['InnoDB/General']),
  ('innodb_status_output_locks', ['InnoDB/General']),
  ('innodb_strict_mode', ['InnoDB/General']),
  ('innodb_support_xa', ['InnoDB/General']),
  ('innodb_sync_array_size', ['InnoDB/General']),
  ('innodb_sync_spin_loops', ['InnoDB/General']),
  ('innodb_table_locks', ['InnoDB/General']),
  ('innodb_temp_data_file_path', ['InnoDB/General']),
  ('innodb_thread_concurrency', ['InnoDB/General']),
  ('innodb_thread_concurrency_timer_based', ['InnoDB/General']),
  ('innodb_thread_sleep_delay', ['InnoDB/General']),
  ('innodb_undo_directory', ['InnoDB/General', 'InnoDB/Logfiles']),
  ('innodb_undo_log_truncate', []),
  ('innodb_undo_logs', ['InnoDB/General', 'InnoDB/Logfiles']),
  ('innodb_undo_tablespaces', ['InnoDB/General']),
  ('innodb_use_legacy_cardinality_algorithm', ['InnoDB/General']),
  ('innodb_use_native_aio', ['InnoDB/General']),
  ('innodb_use_sys_malloc', ['InnoDB/General']),
  ('innodb_write_io_threads', ['InnoDB/General']),
  ('interactive_timeout', ['Networking/Timeout Settings']),
  ('internal_tmp_disk_storage_engine', []),
  ('isam', ['General/Features']),
  ('join_buffer_size', ['General/Memory usage']),
  ('join_cache_level', ['General/Memory usage']),
  ('keep_files_on_create', ['MyISAM/General']),
  ('key_buffer_size', ['MyISAM/General']),
  ('key_cache_age_threshold', ['MyISAM/General']),
  ('key_cache_block_size', ['Advanced/Various']),
  ('key_cache_division_limit', ['Advanced/Various']),
  ('language', ['General/International']),
  ('large-pages', ['General/Memory usage']),
  ('lc-messages', ['General/International']),
  ('lc-messages-dir', ['General/International']),
  ('lock_wait_timeout', ['General/General']),
  ('log', ['Logging/General']),
  ('log-backup-output', ['General/Backup']),
  ('log-bin', ['Logging/Binlog Options']),
  ('log-bin-index', ['Logging/Binlog Options']),
  ('log-bin-trust-function-creators', ['Logging/Binlog Options']),
  ('log-bin-trust-routine-creators', ['Logging/Binlog Options']),
  ('log-error', ['Logging/General']),
  ('log-isam', ['Logging/General']),
  ('log-long-format', ['Logging/Advanced log options']),
  ('log-output', ['Logging/General']),
  ('log-queries-not-using-indexes', ['Logging/General']),
  ('log-raw', ['Logging/General']),
  ('log-short-format', ['Logging/General']),
  ('log-slow-admin-statements', ['Logging/Slow query log options']),
  ('log-slow-queries', ['Logging/Slow query log options']),
  ('log-slow-slave-statements', ['Logging/Slow query log options']),
  ('log-tc', ['Logging/Advanced log options']),
  ('log-tc-size', ['Logging/Advanced log options']),
  ('log-warnings', ['Logging/Advanced log options']),
  ('log_backward_compatible_user_definitions', []),
  ('log_bin_use_v1_row_events', ['Logging/Binlog Options']),
  ('log_error_verbosity', ['Logging/General']),
  ('log_slave_updates', ['Logging/General']),
  ('log_syslog', ['Logging/General']),
  ('log_syslog_facility', ['Logging/General']),
  ('log_syslog_include_pid', ['Logging/General']),
  ('log_syslog_tag', ['Logging/General']),
  ('log_timestamps', ['Logging/General']),
  ('long_query_time', ['Logging/Slow query log options']),
  ('low-priority-updates', ['Performance/General']),
  ('lower_case_table_names', ['General/System']),
  ('master-connect-retry', ['Replication/Master']),
  ('master-host', ['Replication/Master']),
  ('master-info-file', ['Replication/Master']),
  ('master-password', ['Replication/Master']),
  ('master-port', ['Replication/Master']),
  ('master-retry-count', ['Replication/Master']),
  ('master-ssl', ['Replication/Master']),
  ('master-ssl-ca', ['Replication/Master']),
  ('master-ssl-capath', ['Replication/Master']),
  ('master-ssl-cert', ['Replication/Master']),
  ('master-ssl-cipher', ['Replication/Master']),
  ('master-ssl-key', ['Replication/Master']),
  ('master-user', ['Replication/Master']),
  ('master-verify-checksum', ['Replication/Master']),
  ('master_info_repository', ['Replication/Master']),
  ('max-binlog-dump-events', ['Logging/Binlog Options']),
  ('max_allowed_packet', ['Networking/Data / Memory size']),
  ('max_binlog_cache_size', ['Logging/Binlog Options']),
  ('max_binlog_size', ['Logging/Binlog Options']),
  ('max_binlog_stmt_cache_size', ['Logging/Binlog Options']),
  ('max_connect_errors', ['Networking/Advanced']),
  ('max_connections', ['Networking/Advanced']),
  ('max_delayed_threads', ['Advanced/Insert delayed settings']),
  ('max_digest_length', ['Advanced/General']),
  ('max_error_count', ['Advanced/General']),
  ('max_heap_table_size', ['Advanced/Various']),
  ('max_join_size', ['Advanced/Various']),
  ('max_length_for_sort_data', ['Advanced/Various']),
  ('max_long_data_size', ['General/General']),
  ('max_prepared_stmt_count', ['Advanced/General']),
  ('max_relay_log_size', ['Replication/Relay Log']),
  ('max_seeks_for_key', ['Advanced/Various']),
  ('max_sort_length', ['Advanced/Various']),
  ('max_sp_recursion_depth', ['Advanced/General']),
  ('max_statement_time', ['General/General']),
  ('max_user_connections', ['Networking/Advanced']),
  ('max_write_lock_count', ['Advanced/Various']),
  ('mecab_rc_file', []),
  ('memlock', ['Advanced/General']),
  ('min-examined-row-limit', ['Advanced/General']),
  ('multi_range_count', ['Advanced/Various']),
  ('mutex-deadlock-detector', ['Advanced/General']),
  ('myisam-block-size', ['MyISAM/Advanced Settings']),
  ('myisam-recover', ['MyISAM/Advanced Settings']),
  ('myisam-recover-options', ['MyISAM/Advanced Settings']),
  ('myisam_data_pointer_size', ['MyISAM/Advanced Settings']),
  ('myisam_max_extra_sort_file_size', ['MyISAM/Advanced Settings']),
  ('myisam_max_sort_file_size', ['MyISAM/Advanced Settings']),
  ('myisam_mmap_size', ['MyISAM/Advanced Settings']),
  ('myisam_repair_threads', ['MyISAM/Advanced Settings']),
  ('myisam_sort_buffer_size', ['MyISAM/Advanced Settings']),
  ('myisam_stats_method', ['MyISAM/Advanced Settings']),
  ('myisam_use_mmap', ['MyISAM/Advanced Settings']),
  ('mysql-backup', ['General/Backup']),
  ('mysql_native_password_proxy_users', []),
  ('mysql_firewall_max_query_size', ['General/Firewall']),
  ('mysql_firewall_mode', ['General/Firewall']),
  ('mysql_firewall_trace', ['General/Firewall']),
  ('ndb-batch-size', ['Other/NDB']),
  ('ndb-blob-read-batch-bytes', ['Other/NDB']),
  ('ndb-blob-write-batch-bytes', ['Other/NDB']),
  ('ndb-cluster-connection-pool', ['Other/NDB']),
  ('ndb-connectstring', ['Other/NDB']),
  ('ndb-log-transaction-id', ['Other/NDB']),
  ('ndb-log-update-as-write', ['Other/NDB']),
  ('ndb-mgmd-host', ['Other/NDB']),
  ('ndb-nodeid', ['Other/NDB']),
  ('ndb-recv-thread-activation-threshold', ['Other/NDB']),
  ('ndb-recv-thread-cpu-mask', ['Other/NDB']),
  ('ndb-wait-connected', ['Other/NDB']),
  ('ndb-wait-setup', ['Other/NDB']),
  ('ndb_autoincrement_prefetch_sz', ['Other/NDB']),
  ('ndb_cache_check_time', ['Other/NDB']),
  ('ndb_deferred_constraints', ['Other/NDB']),
  ('ndb_distribution', ['Other/NDB']),
  ('ndb_eventbuffer_free_percent', ['Other/NDB']),
  ('ndb_eventbuffer_max_alloc', ['Other/NDB']),
  ('ndb_extra_logging', ['Other/NDB']),
  ('ndb_force_send', ['Other/NDB']),
  ('ndb_index_stat_cache_entries', ['Other/NDB']),
  ('ndb_index_stat_enable', ['Other/NDB']),
  ('ndb_index_stat_option', ['Other/NDB']),
  ('ndb_index_stat_update_freq', ['Other/NDB']),
  ('ndb_log_apply_status', ['Other/NDB']),
  ('ndb_log_empty_epochs', ['Other/NDB']),
  ('ndb_log_exclusive_reads', ['Other/NDB']),
  ('ndb_log_orig', ['Other/NDB']),
  ('ndb_log_updated_only', ['Other/NDB']),
  ('ndb_optimized_node_selection', ['Other/NDB']),
  ('ndb_report_thresh_binlog_epoch_slip', ['Other/NDB']),
  ('ndb_report_thresh_binlog_mem_usage', ['Other/NDB']),
  ('ndb_show_foreign_key_mock_tables', ['Other/NDB']),
  ('ndb_slave_conflict_role', ['Other/NDB']),
  ('ndb_use_transactions', ['Other/NDB']),
  ('ndbcluster', ['Other/NDB']),
  ('net_buffer_length', ['Networking/Data / Memory size']),
  ('net_read_timeout', ['Networking/Timeout Settings']),
  ('net_retry_count', ['Networking/Advanced']),
  ('net_write_timeout', ['Networking/Timeout Settings']),
  ('new', ['Advanced/Various']),
  ('ngram_token_size', []),
  ('offline_mode', []),
  ('old', ['General/General']),
  ('old-alter-table', ['Advanced/Deprecated']),
  ('old-protocol', ['Advanced/Deprecated']),
  ('old-style-user-limits', ['Advanced/General']),
  ('old_passwords', ['Security/Authentication']),
  ('one-thread', ['General/General']),
  ('open-files-limit', ['Advanced/General']),
  ('optimizer_join_cache_level', ['Performance/Optimizer']),
  ('optimizer_prune_level', ['Performance/Optimizer']),
  ('optimizer_search_depth', ['Performance/Optimizer']),
  ('optimizer_switch', ['Performance/Optimizer']),
  ('partition', []),
  ( 'performance-schema-consumer-events-stages-current',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-stages-history',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-stages-history-long',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-statements-current',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-statements-history',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-statements-history-long',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-transactions-current',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-transactions-history',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-transactions-history-long',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-waits-current',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-waits-history',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-events-waits-history-long',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-global-instrumentation',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-statements-digest',
    ['Performance/Performance Schema']),
  ( 'performance-schema-consumer-thread-instrumentation',
    ['Performance/Performance Schema']),
  ('performance-schema-instrument', ['Performance/Performance Schema']),
  ('performance_schema', ['Performance/Performance Schema']),
  ('performance_schema_accounts_size', ['Performance/Performance Schema']),
  ('performance_schema_digests_size', ['Performance/Performance Schema']),
  ( 'performance_schema_events_stages_history_long_size',
    ['Performance/Performance Schema']),
  ( 'performance_schema_events_stages_history_size',
    ['Performance/Performance Schema']),
  ( 'performance_schema_events_statements_history_long_size',
    ['Performance/Performance Schema']),
  ( 'performance_schema_events_statements_history_size',
    ['Performance/Performance Schema']),
  ( 'performance_schema_events_transactions_history_long_size',
    ['Performance/Performance Schema']),
  ( 'performance_schema_events_transactions_history_size',
    ['Performance/Performance Schema']),
  ( 'performance_schema_events_waits_history_long_size',
    ['Performance/Performance Schema']),
  ( 'performance_schema_events_waits_history_size',
    ['Performance/Performance Schema']),
  ('performance_schema_hosts_size', ['Performance/Performance Schema']),
  ('performance_schema_max_cond_classes', ['Performance/Performance Schema']),
  ( 'performance_schema_max_cond_instances',
    ['Performance/Performance Schema']),
  ('performance_schema_max_file_classes', ['Performance/Performance Schema']),
  ('performance_schema_max_file_handles', ['Performance/Performance Schema']),
  ( 'performance_schema_max_file_instances',
    ['Performance/Performance Schema']),
  ('performance_schema_max_index_stat', ['Performance/Performance Schema']),
  ( 'performance_schema_max_memory_classes',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_metadata_locks',
    ['Performance/Performance Schema']),
  ('performance_schema_max_mutex_classes', ['Performance/Performance Schema']),
  ( 'performance_schema_max_mutex_instances',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_prepared_statements_instances',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_program_instances',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_rwlock_classes',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_rwlock_instances',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_socket_classes',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_socket_instances',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_sql_text_length',
    ['Performance/Performance Schema']),
  ('performance_schema_max_stage_classes', ['Performance/Performance Schema']),
  ( 'performance_schema_max_statement_classes',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_statement_stack',
    ['Performance/Performance Schema']),
  ('performance_schema_max_table_handles', ['Performance/Performance Schema']),
  ( 'performance_schema_max_table_instances',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_table_lock_stat',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_thread_classes',
    ['Performance/Performance Schema']),
  ( 'performance_schema_max_thread_instances',
    ['Performance/Performance Schema']),
  ( 'performance_schema_session_connect_attrs_size',
    ['Performance/Performance Schema']),
  ('performance_schema_setup_actors_size', ['Performance/Performance Schema']),
  ( 'performance_schema_setup_objects_size',
    ['Performance/Performance Schema']),
  ('performance_schema_users_size', ['Performance/Performance Schema']),
  ('pid-file', ['General/System']),
  ('plugin', ['General/Features']),
  ('plugin-load', ['General/Features']),
  ('plugin-load-add', ['General/Features']),
  ('plugin_dir', ['General/Directories']),
  ('port', ['Networking/General']),
  ('port-open-timeout', ['Networking/General']),
  ('preload_buffer_size', ['Advanced/Various']),
  ('profiling_history_size', ['General/Features', 'Performance/General']),
  ('query_alloc_block_size', ['Advanced/Various', 'General/Memory usage']),
  ('query_cache_limit', ['Performance/Query cache']),
  ('query_cache_min_res_unit', ['Performance/Query cache']),
  ('query_cache_size', ['Performance/Query cache']),
  ('query_cache_type', ['Performance/Query cache']),
  ('query_cache_wlock_invalidate', ['Performance/Query cache']),
  ('query_prealloc_size', ['Advanced/Various']),
  ('range_alloc_block_size', ['Advanced/Various']),
  ('read_buffer_size', ['Advanced/Various']),
  ('read_only', ['Security/Security']),
  ('read_rnd_buffer_size', ['Advanced/Various']),
  ('relay-log', ['Replication/Relay Log']),
  ('relay-log-info-repository', ['Replication/Relay Log']),
  ('relay_log_index', ['Replication/Relay Log']),
  ('relay_log_info_file', ['Replication/Relay Log']),
  ('relay_log_purge', ['Replication/Relay Log']),
  ('relay_log_recovery', ['Replication/Relay Log']),
  ('relay_log_space_limit', ['Replication/Relay Log']),
  ('replicate-do-db', ['Replication/General']),
  ('replicate-do-table', ['Replication/General']),
  ('replicate-ignore-db', ['Replication/General']),
  ('replicate-ignore-table', ['Replication/General']),
  ('replicate-rewrite-db', ['Replication/General']),
  ('replicate-same-server-id', ['Replication/General']),
  ('replicate-wild-do-table', ['Replication/General']),
  ('replicate-wild-ignore-table', ['Replication/General']),
  ('report-host', ['Replication/General']),
  ('report-password', ['Replication/General']),
  ('report-port', ['Replication/General']),
  ('report-user', ['Replication/General']),
  ('restore_disables_events', ['Advanced/General']),
  ('restore_elevation', ['Advanced/General']),
  ('restore_precheck', ['Advanced/General']),
  ('rpl_stop_slave_timeout', ['Replication/Slave']),
  ('safe-mode', ['Security/Security']),
  ('safe-show-database', ['Security/Security']),
  ('safe-user-create', ['Security/Security']),
  ('safemalloc-mem-limit', ['Security/Security']),
  ('secure-auth', ['Security/Security']),
  ('secure-backup-file-priv', ['Security/Security']),
  ('secure-file-priv', ['Security/Security']),
  ('server-id', ['General/Informational']),
  ('server_id_bits', []),
  ('session_track_gtids', ['General/General']),
  ('session_track_schema', ['General/General']),
  ('session_track_state_change', ['General/General']),
  ('session_track_system_variables', ['General/General']),
  ('set-variable', ['Advanced/Deprecated']),
  ('sha256_password_proxy_users', []),
  ('shared_memory', []),
  ('show-slave-auth-info', ['Replication/Slave']),
  ('show_compatibility_56', []),
  ('show_old_temporals', []),
  ('simplified_binlog_gtid_recovery', []),
  ('skip-bdb', ['Other/Storage Engines']),
  ('skip-character-set-client-handshake', ['General/International']),
  ('skip-concurrent-insert', ['Advanced/General']),
  ('skip-falcon', ['Other/Storage Engines']),
  ('skip-grant-tables', ['Security/Security']),
  ('skip-host-cache', ['General/System']),
  ('skip-locking', ['General/System']),
  ('skip-merge', ['Other/Storage Engines']),
  ('skip-name-resolve', ['Networking/General']),
  ('skip-networking', ['Networking/General']),
  ('skip-partition', ['General/Features']),
  ('skip-safemalloc', ['General/System']),
  ('skip-show-database', ['Security/Security']),
  ('skip-slave-start', ['Replication/General']),
  ('skip-stack-trace', ['General/System']),
  ('skip-symlink', ['General/System']),
  ('skip-sync-bdb-logs', ['Other/Storage Engines']),
  ('skip-thread-priority', ['Advanced/General']),
  ('skip_external_locking', ['General/System']),
  ('slave-load-tmpdir', ['Replication/Slave']),
  ('slave-max-allowed-packet', ['Replication/Slave']),
  ('slave-net-timeout', ['Replication/Slave']),
  ('slave-parallel-type', ['Replication/Slave']),
  ('slave-parallel-workers', ['Replication/Slave']),
  ('slave-rows-search-algorithms', ['Replication/Slave']),
  ('slave-skip-errors', ['Replication/Slave']),
  ('slave-sql-verify-checksum', ['Replication/Slave']),
  ('slave_allow_batching', ['Replication/Slave']),
  ('slave_checkpoint_group', ['Replication/Slave']),
  ('slave_checkpoint_period', ['Replication/Slave']),
  ('slave_compressed_protocol', ['Replication/Slave']),
  ('slave_exec_mode', ['Replication/Slave']),
  ('slave_transaction_retries', ['Replication/Slave']),
  ('slave_type_conversions', ['Replication/Slave']),
  ('slow-query-log', ['Logging/General']),
  ('slow-start-timeout', ['Advanced/General']),
  ('slow_launch_time', ['Advanced/Thread specific settings']),
  ('slow_query_log_file', ['Logging/Slow query log options']),
  ('socket', ['Networking/General']),
  ('sort_buffer_size', ['General/Memory usage']),
  ('sporadic-binlog-dump-fail', ['Logging/Binlog Options']),
  ('sql-bin-update-same', ['General/SQL']),
  ('sql-mode', ['General/SQL']),
  ('ssl', ['Networking/SSL']),
  ('ssl-ca', ['Networking/SSL']),
  ('ssl-capath', ['Networking/SSL']),
  ('ssl-cert', ['Networking/SSL']),
  ('ssl-cipher', ['Networking/SSL']),
  ('ssl-crl', ['Networking/SSL']),
  ('ssl-crlpath', ['Networking/SSL']),
  ('ssl-key', ['Networking/SSL']),
  ('standalone', ['Advanced/General']),
  ('stored_program_cache', ['General/General']),
  ('super-large-pages', ['General/General']),
  ('symbolic-links', ['General/System']),
  ('sync_binlog', ['Logging/Binlog Options']),
  ('sync_frm', ['Advanced/General']),
  ('sync_master_info', ['Replication/Master']),
  ('sync_relay_log', ['Replication/Relay Log']),
  ('sync_relay_log_info', ['Replication/Relay Log']),
  ('sysdate-is-now', ['General/System']),
  ('table_cache', []),
  ('table_lock_wait_timeout', []),
  ('tc-heuristic-recover', []),
  ('temp-pool', []),
  ('thread_cache_size', ['Advanced/Thread specific settings']),
  ('thread_concurrency', ['Advanced/Thread specific settings']),
  ('thread_handling', ['Advanced/Thread specific settings']),
  ('thread_pool_algorithm', ['Advanced/Thread specific settings']),
  ( 'thread_pool_high_priority_connection',
    ['Advanced/Thread specific settings']),
  ('thread_pool_max_unused_threads', ['Advanced/Thread specific settings']),
  ('thread_pool_prio_kickup_timer', ['Advanced/Thread specific settings']),
  ('thread_pool_size', ['Advanced/Thread specific settings']),
  ('thread_pool_stall_limit', ['Advanced/Thread specific settings']),
  ('thread_stack', ['Advanced/Thread specific settings']),
  ('timed_mutexes', ['InnoDB/General']),
  ('tmp_table_size', ['Advanced/Various']),
  ('tmpdir', ['General/Directories']),
  ('transaction-isolation', ['Advanced/Transactions']),
  ('transaction-read-only', ['Advanced/Transactions']),
  ('transaction_alloc_block_size', ['Advanced/Transactions']),
  ('transaction_prealloc_size', ['Advanced/Transactions']),
  ('updatable_views_with_limit', ['Advanced/General']),
  ('use-symbolic-links', ['General/System']),
  ('user', ['General/System']),
  ('validate-password', []),
  ('validate_password_dictionary_file', []),
  ('validate_password_length', []),
  ('validate_password_mixed_case_count', []),
  ('validate_password_number_count', []),
  ('validate_password_policy', []),
  ('validate_password_special_char_count', []),
  ('verbose', []),
  ('wait_timeout', ['Networking/Timeout Settings']),
  ('warnings', ['Advanced/Deprecated']),
  ('skip-innodb', ['InnoDB/General'])]
