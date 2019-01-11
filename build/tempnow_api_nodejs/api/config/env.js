export default {
    environment: process.env.NODE_ENV || 'dev',
    virtualHost: process.env.VIRTUAL_HOST,
    http: {
      host: process.env.HTTP_HOST || '0.0.0.0',
      port: process.env.HTTP_PORT || '3000'
    },
    mysql_db: {
      server: process.env.MYSQL_DATABASE_SERVER || '127.0.0.1',
      port: process.env.MYSQL_DATABASE_PORT || '3306',
      username: process.env.MYSQL_DATABASE_USERNAME || 'root',
      password: process.env.MYSQL_DATABASE_PASSWORD || 'abc123',
      db: process.env.MYSQL_DATABASE_DATABASE || 'tempnow'
    }
  };
  