import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='oege.ie.hva.nl',
                             user='duinmat',
                             password='$Mo/qdGSnX$MEi',
                             database='zduinmat',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print(connection)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)


df.to_sql("Tweets_unedited_with_vaderSentiment",con = en,if_exists='replace',chunksize=10000)