from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from extgitpyp1.config.ConfigStore import *
from extgitpyp1.functions import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("ext-git-py-p1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ext-git-py-p1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/ext-git-py-p1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
