# Hadoop Word Count

## Dependencies

```xml
<dependencies>
        <!-- Hadoop Common -->
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>3.3.5</version> <!-- choose version according to your Hadoop setup -->
        </dependency>

        <!-- Hadoop MapReduce Client Core -->
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-mapreduce-client-core</artifactId>
            <version>3.3.5</version>
        </dependency>

        <!-- Hadoop MapReduce Client Common -->
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-mapreduce-client-common</artifactId>
            <version>3.3.5</version>
        </dependency>

        <!-- Hadoop MapReduce Client JobClient -->
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-mapreduce-client-jobclient</artifactId>
            <version>3.3.5</version>
        </dependency>

        <!-- Hadoop HDFS Client (for accessing HDFS) -->
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-hdfs</artifactId>
            <version>3.3.5</version>
        </dependency>
    </dependencies>
```

## Mapper Phase

![Mapper Phase](resources/mapper_phase.png)

