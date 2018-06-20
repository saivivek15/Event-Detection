Execution:

	- python parse_json.py
	# output dir: parsed_files 
	# Training Dataset files are parsed
	
	- python semaforAll.py 
	# output dir: output_files 
	# Semafor Tool is executed on all training files
	
	- python parse_semafor.py 
	# output dir: semafor_filter_files 
	# Filter the frames having Victim entities
	
	- python feature_matrix.py 
	# output file: training_data.txt
	# Generate the feature matrix from the filtered news feeds

	Start Kafka and ZooKeeper:
	- bin/zookeeper-server-start.sh config/zookeeper.properties
	- bin/kafka-server-start.sh config/server.properties	

	- python scraper-master/scraper.py 
	# Kafka producer client is started

	- spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.0 consumer.py localhost:2181 news
	# Kafka Consumer is started and semafor frames are generated for real time rss feeds

	- python parse_semafor.py
	# change the input directory to output_test_files
	# parse semafor files
	# generate feature_matrix for test feeds
	
	- python tfidf.py 
	# output dir: tempFile 
	# predict with the built models

Notes:
- Modified the Scraper referenced from below by adding Kafka Producer Client and Connecting it to MongoDB 
- The input_files contain only a sample of training data set for referecne. Please contact me at sai.vivek15@gmail.com, if interested in discussing more about the project

References:

 -> Scraper - https://github.com/openeventdata/scraper 

 -> Semafor Tool(CMU)- https://github.com/Noahs-ARK/semafor
 (http://www.ark.cs.cmu.edu/SEMAFOR)

 -> Dataset: http://eventdata.parusanalytics.com/data.dir/atrocities.html
