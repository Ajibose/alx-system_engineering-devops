-- Create the replication user that can connect from any host in the primary server
CREATE USER IF NOT EXISTS 'replica_user'@'%';
-- Grant appropriate permissions to replicate the primary MySQL server
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
