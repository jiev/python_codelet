package logAnalyse;
        
import java.io.IOException;
import java.util.*;
        
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import com.hadoop.mapreduce.LzoTextInputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
        
public class KeywordCount {
        
 public static class Map extends Mapper<LongWritable, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();
    private String tagString = "what=keyword:";
    private int tagStringLength = tagString.length();
        
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = new String(value.getBytes(),0,value.getLength(),"GBK");
        int index = line.indexOf(tagString);
        if( index != -1 )
        { 
            String keyword = line.substring(index + tagStringLength).split("&")[0];
            context.write(new Text(keyword), one);
        }
    }
 } 
        
 public static class Reduce extends Reducer<Text, IntWritable, Text, IntWritable> {

    public void reduce(Text key, Iterable<IntWritable> values, Context context) 
      throws IOException, InterruptedException {
        int sum = 0;
        for (IntWritable val : values) {
            sum += val.get();
        }
        context.write(key, new IntWritable(sum));
    }
 }
        
 public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
        
    Job job = new Job(conf, "eywordcount");
    job.setJarByClass(KeywordCount.class);
    
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
        
    job.setMapperClass(Map.class);
    job.setReducerClass(Reduce.class);
        
    job.setInputFormatClass(LzoTextInputFormat.class);       // 使用lzo 格式文件作为输入
    job.setOutputFormatClass(TextOutputFormat.class);
        
    FileSystem fs = FileSystem.get(conf);
    FileStatus status[] = fs.globStatus(new Path(args[0]));
    for(FileStatus stat:status){
        if(fs.exists(stat.getPath())){
            FileInputFormat.addInputPath(job,stat.getPath());
        }
    }

    FileOutputFormat.setOutputPath(job, new Path(args[1]));
        
    job.waitForCompletion(true);
 }
        
}

