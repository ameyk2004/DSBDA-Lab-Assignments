import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object WordCount{
    def main(args: Array[String]): Unit = {

        var spark = SparkSession.builder.appName("word count").master("local[*]").getOrCreate()

        import spark.implicits._

        val lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

        var words = lines.as[String].flatMap(line => line.split(" "))

        var wordCount = words.groupBy("value").count()

        var query = wordCount.writeStream.outputMode("complete").format("console").start()

        query.awaitTermination()

    }
}