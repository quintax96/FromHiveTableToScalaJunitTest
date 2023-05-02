# FromHiveTableToScalaJunitTest
This project aims to read a hive table from a file (.txt) and create a text file (.txt) containing the table in Junit format for spark projects written in Scala language (dataFrame)


## Execution

1. Download fromHiveTableToScalaDataframe.exe from [FromHiveTableToScalaJunitTest/bin/fromHiveTableToScalaDataframe.exe](https://github.com/quintax96/FromHiveTableToScalaJunitTest/blob/main/bin/fromHiveTableToScalaDataframe.exe)
2. create a txt file with
    1. table name
    2. a list[("field","dataType")]
    3. hive/impala query result in txt format (the fields has to be the same of the list input)
        ```
        anagrafica
        [("id", "int"),("nome", "string")]
        +-------+------------+
        |id     |nome        |
        +-------+------------+
        |1      |pippo	     |
        |2      |pluto	     |
        |3      |gianni	     |
        |4      |carla	     |
        +-------+------------+
        ```
3. Execute `/path/to/fromHiveTableToScalaDataframe.exe`
4. follow the procedure
5. save the destination txt file
    ```
    val anagrafica = List(
    (1,	"pippo"),
    (2,	"pluto"),
    (3,	"gianni"),
    (4,	"carla")
    ).toDF("id","nome")
    ```
    
## Extra

1. it is possible to add more files for different tables and the output will contain all the dataframes created.
2. it does not accept all datatypes yet
3. do not insert more than 22 fields for one table (Scala dataframe do not accept more than 22 columns)


## Did you like it ?! PayPal me ! 💰

[![Donate with PayPal](https://github.com/quintax96/FromHiveTableToScalaJunitTest/blob/main/images/paypal-donate-button.png?raw=true)](https://paypal.me/quintax96)
