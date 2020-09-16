import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

/**
 * 判断hdfs中的文件是否存在
 * 
 * @author lingfangyuan
 * @version 1.0
 * @date 2020-9-16 14:18:16
 * @remarks TODO
 *
 */
public class HDFSFileIfExist {
	public static void main(String[] args) {
		try {
			String fileName = "/user/hadoop/input/myLocalFile.txt";
			Configuration conf = new Configuration();
			conf.set("fs.defaultFS", "hdfs://172.30.192.105:9000");
			conf.set("fs.hdfs.impl", "org.apache.hadoop.hdfs.DistributedFileSystem");
			FileSystem fs = FileSystem.get(conf);
			if (fs.exists(new Path(fileName))) {
				System.out.println("文件存在");
			} else {
				System.out.println("文件不存在");
			}

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
