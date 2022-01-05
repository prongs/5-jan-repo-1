package graph

import io.prophecy.libs._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import config.ConfigStore._

object Source_0 {

  def apply(spark: SparkSession): DataFrame = {
    Config.fabricName match {
      case "dev" =>
        spark.read
          .format("csv")
          .option("header",                           true)
          .option("sep",                              ",")
          .schema(StructType(Array(StructField("lkj", StringType, true))))
          .load("dbfs:/a/b/c")
      case _ =>
        throw new Exception("No valid dataset present to read fabric")
    }
  }

}
